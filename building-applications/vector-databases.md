# Vector Databases

Vector databases are a crucial part of the generative AI workflow. They’re particularly suited for similarity searches, where an application searches for similar items like text, images, or audio.&#x20;

Vectorization feeds text to a machine learning algorithm, which vectorizes the data so that the more similar the words are, the closer their vectors. This creates context for the search query, instead of just trying to match a string, and returns more useful results.&#x20;

LangStream currently supports any database that supports [Kafka Connect](https://docs.confluent.io/platform/current/connect/index.html) or [JDBC](https://docs.oracle.com/javase/tutorial/jdbc/overview/index.html).

### Vectorization example

\
A natural language processing (NLP) technique converts each document into a vector representation. These document vectors are stored in a vector database designed for similarity search.

A user enters a query text related to a news article about technology trends. The query text is processed using the same NLP technique to obtain a vector representation.

A similarity search with this query is performed in the vector database. This involves calculating the cosine similarity or another suitable distance metric between the query vector and the vectors of all stored documents.

The system retrieves the top N documents with the highest similarity scores to the query vector, and the retrieved documents are presented to the user, providing articles that are thematically or contextually similar to the query text.

{% hint style="info" %}
[Vectorization refers to the process of converting data into vectors, while embeddings are a form of vectorization specifically for natural language processing.](#user-content-fn-1)[^1]
{% endhint %}

### Similarity search application

Let’s put this similarity search example in the context of a LangStream application - for example, we have a bucket full of PDFs (unstructured data) and we want to turn them into meaningful embeddings.&#x20;

A LangStream application is a series of steps called a pipeline. At each step, an agent acts on messages streamed through the application.&#x20;

Here’s how you would make a text similarity search application in LangStream. The full pipeline yaml is available [here](https://github.com/LangStream/langstream/blob/main/examples/applications/text-processing/extract-text.yaml).

The first section names the pipeline and declares a “chunks-topic” Kafka topic for message transport into the pipeline.

```yaml
name: "Extract and manipulate text"
topics:
  - name: "chunks-topic"
    creation-mode: create-if-not-exists
```

The first step of the pipeline is to read our data from an S3 bucket.

This part of the pipeline pulls credentials from a secrets.yaml file with Mustache templating.

```yaml
pipeline:
  - name: "Read from S3"
    type: "s3-source"
    configuration:
      bucketName: "{{{secrets.s3-credentials.bucket-name}}}"
      endpoint: "{{{secrets.s3-credentials.endpoint}}}"
      access-key: "{{{secrets.s3-credentials.access-key}}}"
      secret-key: "{{{secrets.s3-credentials.secret}}}"
      region: "{{{secrets.s3-credentials.region}}}"
      idle-time: 5
```

In the second step the agent extracts metadata and text from records using Apache Tika. The records don’t have to be PDFs - Tika supports thousands of formats.

```yaml
  - name: "Extract text"
    type: "text-extractor"
```

The text normaliser agent forces the text into lower case and removes leading and trailing spaces.&#x20;

```yaml
  - name: "Normalise text"
    type: "text-normaliser"
    configuration:
      make-lowercase: true
      trim-spaces: true
```

The language detector agent identifies a record’s language. In this case, non-English records are skipped, and English records continue to the next step in the pipeline.

```yaml
  - name: "Detect language"
    type: "language-detector"
    configuration:
       allowedLanguages: ["en"]
       property: "language"
```

The records are split into chunks of text. This is an important part of the vectorization pipeline to understand, because it requires balancing between performance and accuracy. chunk\_size controls the maximum number of characters of the chunked documents, and chunk\_overlap controls the amount of overlap between chunks. A little overlap keeps results more consistent. chunk\_size defaults to 1000 characters, and chunk\_overlap defaults to 200 characters.

```yaml
  - name: "Split into chunks"
    type: "text-splitter"
    configuration:
      splitter_type: "RecursiveCharacterTextSplitter"
      chunk_size: 400
      separators: ["\n\n", "\n", " ", ""]
      keep_separator: false
      chunk_overlap: 100
      length_function: "cl100k_base"
```

This agent converts the unstructured data to structured JSON.&#x20;

```yaml
  - name: "Convert to structured data"
    type: "document-to-json"
    configuration:
        text-field: text
        copy-properties: true
```

The compute agent structures the output into values the final compute step can work with.

```yaml
  - name: "prepare-structure"
    type: "compute"
    configuration:
      fields:
         - name: "value.filename"
           expression: "properties.name"
           type: STRING
         - name: "value.chunk_id"
           expression: "properties.chunk_id"
           type: STRING
         - name: "value.language"
           expression: "properties.language"
           type: STRING
         - name: "value.chunk_num_tokens"
           expression: "properties.chunk_num_tokens"
           type: STRING
```

Now that the text is processed and structured, an agent computes embeddings and sends them to the Kafka "chunks-topic".

```yaml
  - name: "compute-embeddings"
    id: "step1"
    type: "compute-ai-embeddings"
    output: "chunks-topic"
    configuration:
      model: "text-embedding-ada-002" 
      embeddings-field: "value.embeddings_vector"
      text: "{{% value.text }}"
```

The final agent takes the embeddings from the "chunks-topic" and writes them to an Astra vector database. As with the S3 agent, these credentials are pulled from secrets.yaml.

```yaml
 - name: "Write to AstraDB"
    type: "sink"
    input: "chunks-topic"
    configuration:
      connector.class: com.datastax.oss.kafka.sink.CassandraSinkConnector
      key.converter: org.apache.kafka.connect.storage.StringConverter
      value.converter: org.apache.kafka.connect.storage.StringConverter
      cloud.secureConnectBundle: "{{{ secrets.cassandra.secure-connect-bundle }}}"
      auth.username: "{{{ secrets.cassandra.username }}}"
      auth.password: "{{{ secrets.cassandra.password }}}"
      topic.chunks-topic.documents.documents.mapping: "filename=value.filename, chunk_id=value.chunk_id, language=value.language, text=value.text, embeddings_vector=value.embeddings_vector, num_tokens=value.chunk_num_tokens"
      name: cassandra-sink
```

Now, all the information from your PDFs is embedded in a vector database. Try setting up a chatbot and asking questions about all the information you've made available!

### What’s next?

Do you have a bunch of PDFs lying around, just waiting to be turned into useful, vectorized text?\
This complete pipeline is available in the [LangStream repo](https://github.com/LangStream/langstream/blob/main/examples/applications/text-processing/extract-text.yaml), and running it on your own is no sweat.&#x20;

\
\
\


[^1]: 
