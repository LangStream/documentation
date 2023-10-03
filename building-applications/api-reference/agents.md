# Agents

LangStream Version: **0.0.23**

| Name | Type |
| --- | --- |
| <a href="#ai-chat-completions">Compute chat completions</a> | ai-chat-completions |
| <a href="#ai-text-completions">Compute text completions</a> | ai-text-completions |
| <a href="#cast">Cast record to another schema</a> | cast |
| <a href="#compute">Compute values from the record</a> | compute |
| <a href="#compute-ai-embeddings">Compute embeddings of the record</a> | compute-ai-embeddings |
| <a href="#document-to-json">Document to JSON</a> | document-to-json |
| <a href="#drop">Drop the record</a> | drop |
| <a href="#drop-fields">Drop fields</a> | drop-fields |
| <a href="#flatten">Flatten record fields</a> | flatten |
| <a href="#identity">Identity function</a> | identity |
| <a href="#language-detector">Language detector</a> | language-detector |
| <a href="#merge-key-value">Merge key-value format</a> | merge-key-value |
| <a href="#python-function">Python custom processor</a> | python-function |
| <a href="#python-processor">Python custom processor</a> | python-processor |
| <a href="#python-sink">Python custom sink</a> | python-sink |
| <a href="#python-source">Python custom source</a> | python-source |
| <a href="#query">Query</a> | query |
| <a href="#query-vector-db">Query a vector database</a> | query-vector-db |
| <a href="#re-rank">Re-rank</a> | re-rank |
| <a href="#s3-source">S3 Source</a> | s3-source |
| <a href="#sink">Kafka Connect Sink agent</a> | sink |
| <a href="#source">Kafka Connect Source agent</a> | source |
| <a href="#text-extractor">Text extractor</a> | text-extractor |
| <a href="#text-normaliser">Text normaliser</a> | text-normaliser |
| <a href="#text-splitter">Text splitter</a> | text-splitter |
| <a href="#unwrap-key-value">Unwrap key-value format</a> | unwrap-key-value |
| <a href="#vector-db-sink">Vector database sink</a> | vector-db-sink |
| <a href="#webcrawler-source">Web crawler source</a> | webcrawler-source |


## <a name="ai-chat-completions"></a>Compute chat completions (`ai-chat-completions`)

Sends the messages to the AI Service to compute chat completions. The result is stored in the specified field.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `ai-service` | In case of multiple AI services configured, specify the id of the AI service to use. | string |  |  |
| `completion-field` | Field to use to store the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.<field>" to write the result in a specific field. | string |  |  |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `frequency-penalty` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `log-field` | Field to use to store the log of the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.<field>" to write the result in a specific field.<br>The log contains useful information for debugging the completion prompts. | string |  |  |
| `logit-bias` | Parameter for the completion request. The parameters are passed to the AI Service as is. | object |  |  |
| `max-tokens` | Parameter for the completion request. The parameters are passed to the AI Service as is. | integer |  |  |
| `messages` | Messages to use for chat completions. You can use the Mustache syntax. | <a href="#ai-chat-completions.messages">array of object</a> | ✓ |  |
| `min-chunks-per-message` | Minimum number of chunks to send to the stream-to-topic topic. The chunks are sent as soon as they are available.<br>The chunks are sent in the order they are received from the AI Service.<br>To improve the TTFB (Time-To-First-Byte), the chunk size starts from 1 and doubles until it reaches the max-chunks-per-message value. | integer |  | 20 |
| `model` | The model to use for chat completions. The model must be available in the AI Service. | string | ✓ |  |
| `presence-penalty` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `stop` | Parameter for the completion request. The parameters are passed to the AI Service as is. | array of string |  |  |
| `stream` | Enable streaming of the results. Use in conjunction with the stream-to-topic parameter. | boolean |  | true |
| `stream-response-completion-field` | Field to use to store the completion results in the stream-to-topic topic. Use "value" to write the result without a structured schema. Use "value.<field>" to write the result in a specific field. | string |  |  |
| `stream-to-topic` | Enable streaming of the results. If enabled, the results are streamed to the specified topic in small chunks. The entire messages will be sent to the output topic instead. | string |  |  |
| `temperature` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `top-p` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `user` | Parameter for the completion request. The parameters are passed to the AI Service as is. | string |  |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### <a name="ai-chat-completions.messages"></a>Compute chat completions (`ai-chat-completions`).messages

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `role` | Role of the message. The role is used to identify the speaker in the chat. | string | ✓ |  |
| `content` | Content of the message. You can use the Mustache syntax. | string | ✓ |  |


## <a name="ai-text-completions"></a>Compute text completions (`ai-text-completions`)

Sends the text to the AI Service to compute text completions. The result is stored in the specified field.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `ai-service` | In case of multiple AI services configured, specify the id of the AI service to use. | string |  |  |
| `completion-field` | Field to use to store the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.<field>" to write the result in a specific field. | string |  |  |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `frequency-penalty` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `log-field` | Field to use to store the log of the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.<field>" to write the result in a specific field.<br>The log contains useful information for debugging the completion prompts. | string |  |  |
| `logit-bias` | Parameter for the completion request. The parameters are passed to the AI Service as is. | object |  |  |
| `max-tokens` | Parameter for the completion request. The parameters are passed to the AI Service as is. | integer |  |  |
| `min-chunks-per-message` | Minimum number of chunks to send to the stream-to-topic topic. The chunks are sent as soon as they are available.<br>The chunks are sent in the order they are received from the AI Service.<br>To improve the TTFB (Time-To-First-Byte), the chunk size starts from 1 and doubles until it reaches the max-chunks-per-message value. | integer |  | 20 |
| `model` | The model to use for text completions. The model must be available in the AI Service. | string | ✓ |  |
| `presence-penalty` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `prompt` | Prompt to use for text completions. You can use the Mustache syntax. | array of string | ✓ |  |
| `stop` | Parameter for the completion request. The parameters are passed to the AI Service as is. | array of string |  |  |
| `stream` | Enable streaming of the results. Use in conjunction with the stream-to-topic parameter. | boolean |  | true |
| `stream-response-completion-field` | Field to use to store the completion results in the stream-to-topic topic. Use "value" to write the result without a structured schema. Use "value.<field>" to write the result in a specific field. | string |  |  |
| `stream-to-topic` | Enable streaming of the results. If enabled, the results are streamed to the specified topic in small chunks. The entire messages will be sent to the output topic instead. | string |  |  |
| `temperature` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `top-p` | Parameter for the completion request. The parameters are passed to the AI Service as is. | number |  |  |
| `user` | Parameter for the completion request. The parameters are passed to the AI Service as is. | string |  |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="cast"></a>Cast record to another schema (`cast`)

Transforms the data to a target compatible schema.<br>Some step operations like cast or compute involve conversions from a type to another. When this happens the rules are:<br>    - timestamp, date and time related object conversions assume UTC time zone if it is not explicit.<br>    - date and time related object conversions to/from STRING use the RFC3339 format.<br>    - timestamp related object conversions to/from LONG and DOUBLE are done using the number of milliseconds since EPOCH (1970-01-01T00:00:00Z).<br>    - date related object conversions to/from INTEGER, LONG, FLOAT and DOUBLE are done using the number of days since EPOCH (1970-01-01).<br>    - time related object conversions to/from INTEGER, LONG and DOUBLE are done using the number of milliseconds since midnight (00:00:00).

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `part` | When used with KeyValue data, defines if the transformation is done on the key or on the value. If empty, the transformation applies to both the key and the value. | string |  |  |
| `schema-type` | The target schema type. | string | ✓ |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="compute"></a>Compute values from the record (`compute`)

Computes new properties, values or field values based on an expression evaluated at runtime. If the field already exists, it will be overwritten.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `fields` | An array of objects describing how to calculate the field values | <a href="#compute.fields">array of object</a> | ✓ |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### <a name="compute.fields"></a>Compute values from the record (`compute`).fields

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `expression` | It is evaluated at runtime and the result of the evaluation is assigned to the field.<br>Refer to the language expression documentation for more information on the expression syntax. | string | ✓ |  |
| `name` | The name of the field to be computed. Prefix with key. or value. to compute the fields in the key or value parts of the message.<br>In addition, you can compute values on the following message headers [destinationTopic, messageKey, properties.].<br>Please note that properties is a map of key/value pairs that are referenced by the dot notation, for example properties.key0. | string | ✓ |  |
| `optional` | If true, it marks the field as optional in the schema of the transformed message. This is useful when null is a possible value of the compute expression. | boolean |  | false |
| `type` | The type of the computed field. This<br> will translate to the schema type of the new field in the transformed message.<br> The following types are currently supported :STRING, INT8, INT16, INT32, INT64, FLOAT, DOUBLE, BOOLEAN, DATE, TIME, TIMESTAMP, LOCAL_DATE_TIME, LOCAL_TIME, LOCAL_DATE, INSTANT.<br>  The type field is not required for the message headers [destinationTopic, messageKey, properties.] and STRING will be used.<br>  For the value and key, if it is not provided, then the type will be inferred from the result of the expression evaluation. | string | ✓ |  |


## <a name="compute-ai-embeddings"></a>Compute embeddings of the record (`compute-ai-embeddings`)

Compute embeddings of the record. The embeddings are stored in the record under a specific field.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `ai-service` | In case of multiple AI services configured, specify the id of the AI service to use. | string |  |  |
| `arguments` | Additional arguments to pass to the AI Service. (HuggingFace only) | object |  |  |
| `batch-size` | Batch size for submitting the embeddings requests. | integer |  | 10 |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `concurrency` | Max number of concurrent requests to the AI Service. | integer |  | 4 |
| `embeddings-field` | Field where to store the embeddings. | string | ✓ |  |
| `flush-interval` | Flushing is disabled by default in order to avoid latency spikes.<br>You should enable this feature in the case of background processing. | integer |  | 0 |
| `model` | Model to use for the embeddings. The model must be available in the configured AI Service. | string |  | text-embedding-ada-002 |
| `modelUrl` | URL of the model to use. (HuggingFace only). The default is computed from the model: "djl://ai.djl.huggingface.pytorch{model}" | string |  |  |
| `options` | Additional options to pass to the AI Service. (HuggingFace only) | object |  |  |
| `text` | Text to create embeddings from. You can use Mustache syntax to compose multiple fields into a single text. Example:<br>text: "{{{ value.field1 }}} {{{ value.field2 }}}" | string | ✓ |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="document-to-json"></a>Document to JSON (`document-to-json`)

Convert raw text document to JSON. The result will be a JSON object with the text content in the specified field.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `copy-properties` | Whether to copy the message properties/headers in the output message. | boolean |  | true |
| `text-field` | Field name to write the text content to. | string |  | text |


## <a name="drop"></a>Drop the record (`drop`)

Drops the record from further processing. Use in conjunction with when to selectively drop records.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="drop-fields"></a>Drop fields (`drop-fields`)

Drops the record fields.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `fields` | Fields to drop from the input record. | array of string | ✓ |  |
| `part` | Part to drop. (value or key) | string |  |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="flatten"></a>Flatten record fields (`flatten`)

Converts structured nested data into a new single-hierarchy-level structured data. The names of the new fields are built by concatenating the intermediate level field names.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `delimiter` | The delimiter to use when concatenating the field names. | string |  | _ |
| `part` | When used with KeyValue data, defines if the transformation is done on the key or on the value. If empty, the transformation applies to both the key and the value. | string |  |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="identity"></a>Identity function (`identity`)

Simple agent to move data from the input to the output. Could be used for testing or sample applications.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |


## <a name="language-detector"></a>Language detector (`language-detector`)

Detect the language of a message’s data and limit further processing based on language codes.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `allowedLanguages` | Define a list of allowed language codes. If the message language is not in this list, the message is dropped. | array of string |  |  |
| `property` | The name of the message header to write the language code to. | string |  | language |


## <a name="merge-key-value"></a>Merge key-value format (`merge-key-value`)

Merges the fields of KeyValue records where both the key and value are structured types of the same schema type. Only AVRO and JSON are supported.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="python-function"></a>Python custom processor (`python-function`)

Run a your own Python processor.<br>All the configuration properties are available the class init method.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓ |  |


## <a name="python-processor"></a>Python custom processor (`python-processor`)

Run a your own Python processor.<br>All the configuration properties are available the class init method.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓ |  |


## <a name="python-sink"></a>Python custom sink (`python-sink`)

Run a your own Python sink.<br>All the configuration properties are available in the class init method.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓ |  |


## <a name="python-source"></a>Python custom source (`python-source`)

Run a your own Python source.<br>All the configuration properties are available in the class init method.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓ |  |


## <a name="query"></a>Query (`query`)

Perform a vector search or simple query against a datasource.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |
| `fields` | Fields of the record to use as input parameters for the query. | array of string |  |  |
| `only-first` | If true, only the first result of the query is stored in the output field. | boolean |  | false |
| `output-field` | The name of the field to use to store the query result. | string | ✓ |  |
| `query` | The query to use to extract the data. | string | ✓ |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="query-vector-db"></a>Query a vector database (`query-vector-db`)

Query a vector database using Vector Search capabilities.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |
| `fields` | Fields of the record to use as input parameters for the query. | array of string |  |  |
| `only-first` | If true, only the first result of the query is stored in the output field. | boolean |  | false |
| `output-field` | The name of the field to use to store the query result. | string | ✓ |  |
| `query` | The query to use to extract the data. | string | ✓ |  |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="re-rank"></a>Re-rank (`re-rank`)

Agent for re-ranking documents based on a query.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `algorithm` | Algorithm to use for re-ranking. 'none' or 'MMR'. | string |  | none |
| `b` | Parameter for B25 algorithm. | number |  | 0.75 |
| `embeddings-field` | Result field for the embeddings. | string |  |  |
| `field` | The field that contains the documents to sort. | string | ✓ |  |
| `k1` | Parameter for B25 algorithm. | number |  | 1.5 |
| `lambda` | Parameter for MMR algorithm. | number |  | 0.5 |
| `max` | Maximum number of documents to keep. | integer |  | 100 |
| `output-field` | The field that will hold the results, it can be the same as "field" to override it. | string | ✓ |  |
| `query-embeddings` | Field that contains the embeddings of the documents to sort. | string |  |  |
| `query-text` | Field that already contains the text that has been embedded. | string |  |  |
| `text-field` | Result field for the text. | string |  |  |


## <a name="s3-source"></a>S3 Source (`s3-source`)

Reads data from S3 bucket

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `access-key` | Access key for the S3 server. | string |  | minioadmin |
| `bucketName` | The name of the bucket to read from. | string |  | langstream-source |
| `endpoint` | The endpoint of the S3 server. | string |  | http://minio-endpoint.-not-set:9090 |
| `file-extensions` | Comma separated list of file extensions to filter by. | string |  | pdf,docx,html,htm,md,txt |
| `idle-time` | Region for the S3 server. | integer |  | 5 |
| `region` | Region for the S3 server. | string |  |  |
| `secret-key` | Secret key for the S3 server. | string |  | minioadmin |


## <a name="sink"></a>Kafka Connect Sink agent (`sink`)

Run any Kafka Connect Sink.<br>    All the configuration properties are passed to the Kafka Connect Sink.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `connector.class` | Java main class for the Kafka Sink connector. | string | ✓ |  |


## <a name="source"></a>Kafka Connect Source agent (`source`)

Run any Kafka Connect Source.<br>    All the configuration properties are passed to the Kafka Connect Source.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `connector.class` | Java main class for the Kafka Source connector. | string | ✓ |  |


## <a name="text-extractor"></a>Text extractor (`text-extractor`)

Extracts text content from different document formats like PDF, JSON, XML, ODF, HTML and many others.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |


## <a name="text-normaliser"></a>Text normaliser (`text-normaliser`)

Apply normalisation to the text.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `make-lowercase` | Whether to make the text lowercase. | boolean |  | true |
| `trim-spaces` | Whether to trim spaces from the text. | boolean |  | true |


## <a name="text-splitter"></a>Text splitter (`text-splitter`)

Split message content in chunks.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `chunk_overlap` | RecursiveCharacterTextSplitter splitter option. Chunk overlap of the previous message.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details. | integer |  | 100 |
| `chunk_size` | RecursiveCharacterTextSplitter splitter option. Chunk size of each message.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details. | integer |  | 200 |
| `keep_separator` | RecursiveCharacterTextSplitter splitter option. Whether or not to keep separators.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details. | boolean |  | false |
| `length_function` | RecursiveCharacterTextSplitter splitter option. Options are: r50k_base, p50k_base, p50k_edit and cl100k_base.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details. | string |  | cl100k_base |
| `separators` | RecursiveCharacterTextSplitter splitter option. The separator to use for splitting.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details. | array of string |  | "\n\n", "\n", " ", "" |
| `splitter_type` | Splitter implementation to use. Currently supported: RecursiveCharacterTextSplitter. | string |  | RecursiveCharacterTextSplitter |


## <a name="unwrap-key-value"></a>Unwrap key-value format (`unwrap-key-value`)

If the record value is in KeyValue format, extracts the KeyValue's key or value and make it the record value.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `composable` | Whether this step can be composed with other steps. | boolean |  | true |
| `unwrapKey` | Whether to unwrap the key instead of the value. | boolean |  | false |
| `when` | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


## <a name="vector-db-sink"></a>Vector database sink (`vector-db-sink`)

Store vectors in a vector database.<br>Configuration properties depends on the vector database implementation, specified by the "datasource" property.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `datasource` | The defined datasource ID to use to store the vectors. | string | ✓ |  |


## <a name="webcrawler-source"></a>Web crawler source (`webcrawler-source`)

Crawl a website and extract the content of the pages.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `access-key` | Configuration for handling the agent status.<br>Access key for the S3 server. | string |  | minioadmin |
| `allowed-domains` | Domains that the crawler is allowed to access. | array of string |  |  |
| `bucketName` | Configuration for handling the agent status.<br>The name of the bucket. | string |  | langstream-source |
| `endpoint` | Configuration for handling the agent status.<br>The S3 endpoint. | string |  | http://minio-endpoint.-not-set:9090 |
| `forbidden-paths` | Paths that the crawler is not allowed to access. | array of string |  |  |
| `handle-cookies` | Whether to handle cookies. | boolean |  | true |
| `handle-robots-file` | Whether to scan the HTML documents to find links to other pages. | boolean |  | true |
| `http-timeout` | Timeout for HTTP requests. (in milliseconds) | integer |  | 10000 |
| `max-depth` | Maximum depth of the crawl. | integer |  | 50 |
| `max-error-count` | Maximum number of errors allowed before stopping. | integer |  | 5 |
| `max-unflushed-pages` | Maximum number of unflushed pages before the agent persists the crawl data. | integer |  | 100 |
| `max-urls` | Maximum number of URLs that can be crawled. | integer |  | 1000 |
| `min-time-between-requests` | Minimum time between two requests to the same domain. (in milliseconds) | integer |  | 500 |
| `region` | Configuration for handling the agent status.<br>Region for the S3 server. | string |  |  |
| `reindex-interval-seconds` | Time interval between reindexing of the pages. | integer |  | 86400 |
| `scan-html-documents` | Whether to scan HTML documents for links to other sites. | boolean |  | true |
| `secret-key` | Configuration for handling the agent status.<br>Secret key for the S3 server. | string |  | minioadmin |
| `seed-urls` | The starting URLs for the crawl. | array of string |  |  |
| `user-agent` | User agent to use for the requests. | string |  | Mozilla/5.0 (compatible; LangStream.ai/0.1; +https://langstream.ai) |


