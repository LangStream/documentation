# webcrawler-source

The webcrawler-source agent crawls a website and outputs the site's URL and an HTML document. Crawling a website is an ideal first step in a [text embeddings pipeline](https://github.com/LangStream/langstream/tree/main/examples/applications/webcrawler-source).

The S3 bucket only stores metadata about the website and the status of the crawler - it won’t contain a copy of the crawl data, but a single JSON file with a name computed from the name of the agent and the id of the LangStream application.

### Example

Example webcrawler agent in a pipeline:

```yaml
pipeline:
  - name: "Crawl the WebSite"
    type: "webcrawler-source"
    configuration:
      seed-urls: ["https://docs.langstream.ai/"]
      allowed-domains: ["https://docs.langstream.ai"]
      forbidden-paths: []
      min-time-between-requests: 500
      reindex-interval-seconds: 3600
      max-error-count: 5
      max-urls: 1000
      max-depth: 50
      handle-robots-file: true
      user-agent: "" # this is computed automatically, but you can override it
      scan-html-documents: true
      http-timeout: 10000
      handle-cookies: true
      max-unflushed-pages: 100
      bucketName: "${secrets.s3.bucket-name}"
      endpoint: "${secrets.s3.endpoint}"
      access-key: "${secrets.s3.access-key}"
      secret-key: "${secrets.s3.secret}"
      region: "${secrets.s3.region}"
```

#### Multiple URLs in pipeline

Multiple seed-urls and allowed-domains are allowed.

To add them to your pipeline, use this syntax:

```yaml
seed-urls:
  - "http://example1.com"
  - "http://example2.com"
allowed-domains:
  - "http://example1.com"
  - "http://example2.com"  
```

### Topics

**Input**

* None, it’s a source

**Output**

* Structured text (JSON) [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

| Label                     | Type                   | Description                                                                                              |
| ------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------- |
| seed-urls                 | List of Strings        | The starting URLs for the crawl.                                                                         |
| allowed-domains           | List of Strings        | Domains that the crawler is allowed to access.                                                           |
| forbidden-paths           | List of Strings        | Paths that the crawler is not allowed to access.                                                         |
| min-time-between-requests | Integer (milliseconds) | Minimum time between two requests to the same domain.                                                    |
| reindex-interval-seconds  | Integer (seconds)      | Time interval between reindexing of the pages.                                                           |
| max-error-count           | Integer                | Maximum number of errors allowed before stopping.                                                        |
| max-urls                  | Integer                | Maximum number of URLs that can be crawled. Defaults to 1000.                                            |
| max-depth                 | Integer                | Maximum depth of the crawl.                                                                              |
| handle-robots-file        | Boolean                | Whether to scan the HTML documents to find links to other pages (defaults to true)                       |
| user-agent                | String                 | User-agent string, computed automatically unless overridden. Defaults to "langstream.ai-webcrawler/1.0". |
| scan-html-documents       | Boolean                | Whether to scan HTML documents for links to other sites. Defaults to true.                               |
| http-timeout              | Integer (milliseconds) | Timeout for HTTP requests.                                                                               |
| handle-cookies            | Boolean                | Whether to handle cookies.                                                                               |
| max-unflushed-pages       | Integer                | Maximum number of unflushed pages before the agent persists the crawl data.                              |

### S3 credentials

<table><thead><tr><th width="147.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>bucketName</td><td>string (required)</td><td>The name of the bucket. Defaults to "langstream-source".</td></tr><tr><td>endpoint</td><td>string (required)</td><td>The URL of the S3 service.  Defaults to "<a href="http://minio-endpoint.-not-set:9090">http://minio-endpoint.-not-set:9090</a>".</td></tr><tr><td>access-key</td><td>string (optional)</td><td>Optional user name credential. Defaults to "minioadmin".</td></tr><tr><td>secret-key</td><td>string (optional)</td><td>Optional password credential. Defaults to "minioadmin".</td></tr><tr><td>region</td><td>string </td><td>Region of S3 bucket.</td></tr></tbody></table>

### Webcrawler-status

| Label         | Type   | Description                                                           |
| ------------- | ------ | --------------------------------------------------------------------- |
| pendingUrls   | String | Holds the URLs that have been discovered but are yet to be processed. |
| remainingUrls | String | Holds the URLs that have been discovered but are yet to be processed. |
| visitedUrls   | String | Holds all URLs that have been visited to prevent cyclic crawling.     |

### Example webcrawler workflow

Using the webcrawler source agent as a starting point, this workflow will crawl a website, get a page's raw HTML, and process that information into chunks for embedding in a vector database.\
The complete example code is available in the [LangStream repository.](https://github.com/LangStream/langstream/tree/main/examples/applications/webcrawler-source)

1. Topics necessary for the application are declared: we will later pass the chunked embeddings to a vector database via the Kafka "chunks-topic".

```yaml
name: "Crawl a website"
topics:
  - name: "chunks-topic"
    creation-mode: create-if-not-exists
```

2. The webcrawler source agent configuration is declared. For help finding your credential information, see [Secrets.](../../building-applications/secrets.md) For help configuring the webcrawler-source, see [Configuration.](webcrawler-source.md#configuration)

```yaml
pipeline:
      seed-urls: ["https://docs.langstream.ai/"]
      allowed-domains: ["https://docs.langstream.ai"]
      forbidden-paths: []
      min-time-between-requests: 500
      reindex-interval-seconds: 3600
      max-error-count: 5
      max-urls: 1000
      max-depth: 50
      handle-robots-file: true
      user-agent: "" # this is computed automatically, but you can override it
      scan-html-documents: true
      http-timeout: 10000
      handle-cookies: true
      max-unflushed-pages: 100
      bucketName: "${secrets.s3.bucket-name}"
      endpoint: "${secrets.s3.endpoint}"
      access-key: "${secrets.s3.access-key}"
      secret-key: "${secrets.s3.secret}"
      region: "${secrets.s3.region}"
```

The webcrawler itself uses the [Jsoup](https://jsoup.org/) library to parse HTML with the [WHATWG HTML spec](https://html.spec.whatwg.org/multipage/). The webcrawler explores the web starting from a list of seed URLs and follows links within pages to discover more content.&#x20;

For each seed-url, the webcrawler:

* Sets up a connection using Jsoup.&#x20;
* Catches HTTP status errors and handles retries or skips based on the error code (`HttpStatusException` for HTTP errors and `UnsupportedMimeTypeException` for non-HTML content types)
* If the content is HTML, the webcrawler fetches the links (hrefs) from the page and adds them to the list of URLs to be crawled, if the href passes the allowed-domain rule set in the pipeline configuration.
* Gets the page's HTML and creates a document with the site url as a header and raw HTML as output.

The webcrawler then passes the document on to the next agent.

3. The [text-extractor agent](../text-processors/text-extractor.md) extracts metadata and text from records using Apache Tika.&#x20;

```yaml
  - name: "Extract text"
    type: "text-extractor"
```

4. The [text-normaliser agent](../text-processors/text-normaliser.md) forces the text into lower case and removes leading and trailing spaces.&#x20;

```yaml
  - name: "Normalise text"
    type: "text-normaliser"
    configuration:
      make-lowercase: true
      trim-spaces: true
```

5. The [language detector agent](../text-processors/language-detector.md) identifies a record’s language. In this case, non-English records are skipped, and English records continue to the next step in the pipeline.

```yaml
  - name: "Detect language"
    type: "language-detector"
    configuration:
       allowedLanguages: ["en"]
       property: "language"
```

6. The [text-splitter agent ](../text-processors/text-splitter.md)splits the document into chunks of text. This is an important part of the vectorization pipeline to understand, because it requires balancing between performance and accuracy. chunk\_size controls the maximum number of characters of the chunked documents, and chunk\_overlap controls the amount of overlap between chunks. A little overlap keeps results more consistent. chunk\_size defaults to 1000 characters, and chunk\_overlap defaults to 200 characters.

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

7. The [document-to-json](../text-processors/document-to-json.md) agent converts the unstructured data to structured JSON.&#x20;

```yaml
  - name: "Convert to structured data"
    type: "document-to-json"
    configuration:
        text-field: text
        copy-properties: true
```

8. The [compute agent](../data-transform/compute.md) structures the JSON output into values the final compute step can work with.

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

9. Now that the text is processed and structured, the [compute-ai-embeddings](../ai-actions/compute-ai-embeddings.md) agent computes embeddings and sends them to the Kafka "chunks-topic".

```yaml
  - name: "compute-embeddings"
    id: "step1"
    type: "compute-ai-embeddings"
    output: "chunks-topic"
    configuration:
      model: "text-embedding-ada-002" # This needs to match the name of the model deployment, not the base model
      embeddings-field: "value.embeddings_vector"
      text: "{{ value.text }}"
      batch-size: 10
      flush-interval: 500
```

10\. Where to next? If you've got an [Astra vector database](http://astra.datastax.com), use the [vector-db-sink](vector-db-sink.md) agent to sink the vectorized embeddings via the Kafka "chunks-topic" to your database. From there, you can [query](../text-processors/query-vector-db.md) your vector data, or ask questions with a [chatbot](https://github.com/LangStream/langstream/blob/main/examples/applications/webcrawler-source/chatbot.yaml). It's up to you!

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


### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#webcrawler-source).