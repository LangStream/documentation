# Vector Databases

Vector databases are a crucial part of the generative AI workflow. Vector databases store vector representations (embeddings) of text, images, sound, etc. They include search tools to enable similarity search across the vector representations to find semantically similar data.

Vector databases are typically used as part of retrieval augmented generation (RAG). In the RAG workflow, relevant documents or passages are retrieved from a vector database based on their semantic relevance. These documents or passages are then included in the LLM prompt to provide additional context for the LLM to use when generating a response. This pattern is used to:

* Reduce AI hallucinations
* Provide more accurate, up-to-date, and context-aware responses
* Extend the knowledge base of the LLM

LangStream makes it easy to build applications using the [RAG pattern](../patterns/rag-pattern.md). It currently has native support for [DataStax Astra DB](https://www.datastax.com/products/vector-search), [Pinecone](https://www.pinecone.io/), [Milvus/Zilliz](https://milvus.io/), [OpenSearch](https://opensearch.org/docs/latest/) and [Apache Cassandra](https://cassandra.apache.org).

When working with a vector database you will either be writing vector embeddings to a vector database or performing semantic similarity queries across the vectors in the database. Check out the [vector-db-sink agent](../pipeline-agents/input-and-output/vector-db-sink.md) for writing to vector databases and the [query-vector-db agent](../pipeline-agents/text-processors/query-vector-db.md) for querying.

There is also built-in support for querying and writing to any database which has a [JDBC](https://docs.oracle.com/javase/tutorial/jdbc/overview/index.html) driver.

Please refer to the [Data Storage section](../configuration-resources/data-storage/) for more information on how to configure your vector database.

You can also write to any database with an available [Kafka Connect](https://docs.confluent.io/platform/current/connect/index.html) connector.

### Vectorization example

An embedding model, such as OpenAI's `text-embedding-ada-002`, converts each document into a vector representation. These document vectors are stored in a vector database designed for similarity search.

A user enters a query text related to a news article about technology trends. The query text is processed using the same embedding model to obtain a vector representation.

A similarity search with this query is performed in the vector database. This involves calculating the cosine similarity or another suitable distance metric between the query vector and the vectors of all stored documents.

The system retrieves the top N documents with the highest similarity scores to the query vector, and the retrieved documents are presented to the user, providing articles that are thematically or contextually similar to the query text.

{% hint style="info" %}
[Vectorization refers to the process of converting data into vectors, while embeddings are a form of vectorization specifically for natural language processing.](vector-databases.md#user-content-fn-1)\[^1]
{% endhint %}

### Similarity search application

Let’s put this similarity search example in the context of a LangStream application - for example, we have a bucket full of PDFs (unstructured data) and we want to turn them into meaningful embeddings.

A LangStream application is a series of steps called a pipeline. At each step, an agent acts on messages streamed through the application.

Here’s how you would make a text similarity search application in LangStream. The full pipeline yaml is available [here](https://github.com/LangStream/langstream/tree/main/examples/applications/docker-chatbot).

The first section names the pipeline and declares a “chunks-topic” Kafka topic for message transport into the pipeline.

```yaml
name: "Extract and manipulate text"
topics:
  - name: "chunks-topic"
    creation-mode: create-if-not-exists
```

The first step of the pipeline is to read our data from an S3 bucket.

This part of the pipeline pulls credentials from a secrets.yaml file with references to secrets.

```yaml
pipeline:
  - name: "Read from S3"
    type: "s3-source"
    configuration:
      bucketName: "${secrets.s3-credentials.bucket-name}"
      endpoint: "${secrets.s3-credentials.endpoint}"
      access-key: "${secrets.s3-credentials.access-key}"
      secret-key: "${secrets.s3-credentials.secret}"
      region: "${secrets.s3-credentials.region}"
      idle-time: 5
```

In the second step the agent extracts metadata and text from records using Apache Tika. The records don’t have to be PDFs - Tika supports thousands of formats.

```yaml
  - name: "Extract text"
    type: "text-extractor"
```

The text normaliser agent forces the text into lower case and removes leading and trailing spaces.

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

This agent converts the unstructured data to structured JSON.

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
          expression: "properties.url"
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
    output: chunks-topic
    configuration:
      model: "text-embedding-ada-002" # This needs to match the name of the model deployment, not the base model
      embeddings-field: "value.embeddings_vector"
      text: "{{ value.text }}"
      batch-size: 10
      flush-interval: 500
```

The final agent takes the embeddings from the "chunks-topic" and writes them to an Astra vector database. As with the S3 agent, these credentials are pulled from secrets.yaml.

```yaml
  - name: "Write to Astra"
    type: "vector-db-sink"
    input: "chunks-topic"
    resources:
      size: 2
    configuration:
      datasource: "AstraDatasource"
      table-name: "documents"
      keyspace: "documents"
      mapping: "filename=value.filename, chunk_id=value.chunk_id, language=value.language, text=value.text, embeddings_vector=value.embeddings_vector, num_tokens=value.chunk_num_tokens"
```

Now, all the information from your PDFs is embedded in a vector database. Try setting up a chatbot and asking questions about all the information you've made available!

### What’s next?

Do you have a website lying around just waiting to be turned into useful, vectorized text?\
This complete pipeline is available in the [LangStream repo](https://github.com/LangStream/langstream/tree/main/examples/applications/docker-chatbot), and running it on your own is no sweat.
