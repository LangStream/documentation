# Agents

LangStream Version: **0.1.0**

### Compute chat completions (`ai-chat-completions`) <a href="#ai-chat-completions" id="ai-chat-completions"></a>

Sends the messages to the AI Service to compute chat completions. The result is stored in the specified field.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>ai-service</code></td><td>In case of multiple AI services configured, specify the id of the AI service to use.</td><td>string</td><td></td><td></td></tr><tr><td><code>completion-field</code></td><td>Field to use to store the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value." to write the result in a specific field.</td><td>string</td><td></td><td></td></tr><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>frequency-penalty</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>log-field</code></td><td>Field to use to store the log of the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value." to write the result in a specific field.<br>The log contains useful information for debugging the completion prompts.</td><td>string</td><td></td><td></td></tr><tr><td><code>logit-bias</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>object</td><td></td><td></td></tr><tr><td><code>max-tokens</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>integer</td><td></td><td></td></tr><tr><td><code>messages</code></td><td>Messages to use for chat completions. You can use the Mustache syntax.</td><td><a href="agents.md#ai-chat-completions.messages">array of object</a></td><td>✓</td><td></td></tr><tr><td><code>min-chunks-per-message</code></td><td>Minimum number of chunks to send to the stream-to-topic topic. The chunks are sent as soon as they are available.<br>The chunks are sent in the order they are received from the AI Service.<br>To improve the TTFB (Time-To-First-Byte), the chunk size starts from 1 and doubles until it reaches the max-chunks-per-message value.</td><td>integer</td><td></td><td>20</td></tr><tr><td><code>model</code></td><td>The model to use for chat completions. The model must be available in the AI Service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>presence-penalty</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>stop</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>stream</code></td><td>Enable streaming of the results. Use in conjunction with the stream-to-topic parameter.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>stream-response-completion-field</code></td><td>Field to use to store the completion results in the stream-to-topic topic. Use "value" to write the result without a structured schema. Use "value." to write the result in a specific field.</td><td>string</td><td></td><td></td></tr><tr><td><code>stream-to-topic</code></td><td>Enable streaming of the results. If enabled, the results are streamed to the specified topic in small chunks. The entire messages will be sent to the output topic instead.</td><td>string</td><td></td><td></td></tr><tr><td><code>temperature</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>top-p</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>user</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>string</td><td></td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

#### Compute chat completions (`ai-chat-completions`).messages <a href="#ai-chat-completions.messages" id="ai-chat-completions.messages"></a>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>role</code></td><td>Role of the message. The role is used to identify the speaker in the chat.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>content</code></td><td>Content of the message. You can use the Mustache syntax.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

### Compute text completions (`ai-text-completions`) <a href="#ai-text-completions" id="ai-text-completions"></a>

Sends the text to the AI Service to compute text completions. The result is stored in the specified field.

|                                    | Description                                                                                                                                                                                                                                                                                                                                  | Type            | Required | Default Value |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- | ------------- |
| `ai-service`                       | In case of multiple AI services configured, specify the id of the AI service to use.                                                                                                                                                                                                                                                         | string          |          |               |
| `completion-field`                 | Field to use to store the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value." to write the result in a specific field.                                                                                                                                                         | string          |          |               |
| `composable`                       | Whether this step can be composed with other steps.                                                                                                                                                                                                                                                                                          | boolean         |          | true          |
| `frequency-penalty`                | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | number          |          |               |
| `log-field`                        | <p>Field to use to store the log of the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value." to write the result in a specific field.<br>The log contains useful information for debugging the completion prompts.</p>                                                          | string          |          |               |
| `logit-bias`                       | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | object          |          |               |
| `max-tokens`                       | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | integer         |          |               |
| `min-chunks-per-message`           | <p>Minimum number of chunks to send to the stream-to-topic topic. The chunks are sent as soon as they are available.<br>The chunks are sent in the order they are received from the AI Service.<br>To improve the TTFB (Time-To-First-Byte), the chunk size starts from 1 and doubles until it reaches the max-chunks-per-message value.</p> | integer         |          | 20            |
| `model`                            | The model to use for text completions. The model must be available in the AI Service.                                                                                                                                                                                                                                                        | string          | ✓        |               |
| `presence-penalty`                 | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | number          |          |               |
| `prompt`                           | Prompt to use for text completions. You can use the Mustache syntax.                                                                                                                                                                                                                                                                         | array of string | ✓        |               |
| `stop`                             | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | array of string |          |               |
| `stream`                           | Enable streaming of the results. Use in conjunction with the stream-to-topic parameter.                                                                                                                                                                                                                                                      | boolean         |          | true          |
| `stream-response-completion-field` | Field to use to store the completion results in the stream-to-topic topic. Use "value" to write the result without a structured schema. Use "value." to write the result in a specific field.                                                                                                                                                | string          |          |               |
| `stream-to-topic`                  | Enable streaming of the results. If enabled, the results are streamed to the specified topic in small chunks. The entire messages will be sent to the output topic instead.                                                                                                                                                                  | string          |          |               |
| `temperature`                      | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | number          |          |               |
| `top-p`                            | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | number          |          |               |
| `user`                             | Parameter for the completion request. The parameters are passed to the AI Service as is.                                                                                                                                                                                                                                                     | string          |          |               |
| `when`                             | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p>                                                                                                                               | string          |          |               |

### Cast record to another schema (`cast`) <a href="#cast" id="cast"></a>

Transforms the data to a target compatible schema.\
Some step operations like cast or compute involve conversions from a type to another. When this happens the rules are:\
\- timestamp, date and time related object conversions assume UTC time zone if it is not explicit.\
\- date and time related object conversions to/from STRING use the RFC3339 format.\
\- timestamp related object conversions to/from LONG and DOUBLE are done using the number of milliseconds since EPOCH (1970-01-01T00:00:00Z).\
\- date related object conversions to/from INTEGER, LONG, FLOAT and DOUBLE are done using the number of days since EPOCH (1970-01-01).\
\- time related object conversions to/from INTEGER, LONG and DOUBLE are done using the number of milliseconds since midnight (00:00:00).

|               | Description                                                                                                                                                                                                    | Type    | Required | Default Value |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------- |
| `composable`  | Whether this step can be composed with other steps.                                                                                                                                                            | boolean |          | true          |
| `part`        | When used with KeyValue data, defines if the transformation is done on the key or on the value. If empty, the transformation applies to both the key and the value.                                            | string  |          |               |
| `schema-type` | The target schema type.                                                                                                                                                                                        | string  | ✓        |               |
| `when`        | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string  |          |               |

### Compute values from the record (`compute`) <a href="#compute" id="compute"></a>

Computes new properties, values or field values based on an expression evaluated at runtime. If the field already exists, it will be overwritten.

|              | Description                                                                                                                                                                                                    | Type                                        | Required | Default Value |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | -------- | ------------- |
| `composable` | Whether this step can be composed with other steps.                                                                                                                                                            | boolean                                     |          | true          |
| `fields`     | An array of objects describing how to calculate the field values                                                                                                                                               | [array of object](agents.md#compute.fields) | ✓        |               |
| `when`       | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string                                      |          |               |

#### Compute values from the record (`compute`).fields <a href="#compute.fields" id="compute.fields"></a>

|              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type    | Required | Default Value |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------- | ------------- |
| `expression` | <p>It is evaluated at runtime and the result of the evaluation is assigned to the field.<br>Refer to the language expression documentation for more information on the expression syntax.</p>                                                                                                                                                                                                                                                                                                                                                                                  | string  | ✓        |               |
| `name`       | <p>The name of the field to be computed. Prefix with key. or value. to compute the fields in the key or value parts of the message.<br>In addition, you can compute values on the following message headers [destinationTopic, messageKey, properties.].<br>Please note that properties is a map of key/value pairs that are referenced by the dot notation, for example properties.key0.</p>                                                                                                                                                                                  | string  | ✓        |               |
| `optional`   | If true, it marks the field as optional in the schema of the transformed message. This is useful when null is a possible value of the compute expression.                                                                                                                                                                                                                                                                                                                                                                                                                      | boolean |          | false         |
| `type`       | <p>The type of the computed field. This<br>will translate to the schema type of the new field in the transformed message.<br>The following types are currently supported :STRING, INT8, INT16, INT32, INT64, FLOAT, DOUBLE, BOOLEAN, DATE, TIME, TIMESTAMP, LOCAL_DATE_TIME, LOCAL_TIME, LOCAL_DATE, INSTANT.<br>The type field is not required for the message headers [destinationTopic, messageKey, properties.] and STRING will be used.<br>For the value and key, if it is not provided, then the type will be inferred from the result of the expression evaluation.</p> | string  | ✓        |               |

### Compute embeddings of the record (`compute-ai-embeddings`) <a href="#compute-ai-embeddings" id="compute-ai-embeddings"></a>

Compute embeddings of the record. The embeddings are stored in the record under a specific field.

|                    | Description                                                                                                                                                                                                    | Type    | Required | Default Value          |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ---------------------- |
| `ai-service`       | In case of multiple AI services configured, specify the id of the AI service to use.                                                                                                                           | string  |          |                        |
| `arguments`        | Additional arguments to pass to the AI Service. (HuggingFace only)                                                                                                                                             | object  |          |                        |
| `batch-size`       | Batch size for submitting the embeddings requests.                                                                                                                                                             | integer |          | 10                     |
| `composable`       | Whether this step can be composed with other steps.                                                                                                                                                            | boolean |          | true                   |
| `concurrency`      | Max number of concurrent requests to the AI Service.                                                                                                                                                           | integer |          | 4                      |
| `embeddings-field` | Field where to store the embeddings.                                                                                                                                                                           | string  | ✓        |                        |
| `flush-interval`   | <p>Flushing is disabled by default in order to avoid latency spikes.<br>You should enable this feature in the case of background processing.</p>                                                               | integer |          | 0                      |
| `model`            | Model to use for the embeddings. The model must be available in the configured AI Service.                                                                                                                     | string  |          | text-embedding-ada-002 |
| `modelUrl`         | URL of the model to use. (HuggingFace only). The default is computed from the model: "djl://ai.djl.huggingface.pytorch{model}"                                                                                 | string  |          |                        |
| `options`          | Additional options to pass to the AI Service. (HuggingFace only)                                                                                                                                               | object  |          |                        |
| `text`             | <p>Text to create embeddings from. You can use Mustache syntax to compose multiple fields into a single text. Example:<br>text: "{{{ value.field1 }}} {{{ value.field2 }}}"</p>                                | string  | ✓        |                        |
| `when`             | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string  |          |                        |

### Document to JSON (`document-to-json`) <a href="#document-to-json" id="document-to-json"></a>

Convert raw text document to JSON. The result will be a JSON object with the text content in the specified field.

|                   | Description                                                           | Type    | Required | Default Value |
| ----------------- | --------------------------------------------------------------------- | ------- | -------- | ------------- |
| `copy-properties` | Whether to copy the message properties/headers in the output message. | boolean |          | true          |
| `text-field`      | Field name to write the text content to.                              | string  |          | text          |

### Drop the record (`drop`) <a href="#drop" id="drop"></a>

Drops the record from further processing. Use in conjunction with when to selectively drop records.

|              | Description                                                                                                                                                                                                    | Type    | Required | Default Value |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------- |
| `composable` | Whether this step can be composed with other steps.                                                                                                                                                            | boolean |          | true          |
| `when`       | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string  |          |               |

### Drop fields (`drop-fields`) <a href="#drop-fields" id="drop-fields"></a>

Drops the record fields.

|              | Description                                                                                                                                                                                                    | Type            | Required | Default Value |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- | ------------- |
| `composable` | Whether this step can be composed with other steps.                                                                                                                                                            | boolean         |          | true          |
| `fields`     | Fields to drop from the input record.                                                                                                                                                                          | array of string | ✓        |               |
| `part`       | Part to drop. (value or key)                                                                                                                                                                                   | string          |          |               |
| `when`       | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string          |          |               |

### Flatten record fields (`flatten`) <a href="#flatten" id="flatten"></a>

Converts structured nested data into a new single-hierarchy-level structured data. The names of the new fields are built by concatenating the intermediate level field names.

|              | Description                                                                                                                                                                                                    | Type    | Required | Default Value |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------- |
| `composable` | Whether this step can be composed with other steps.                                                                                                                                                            | boolean |          | true          |
| `delimiter`  | The delimiter to use when concatenating the field names.                                                                                                                                                       | string  |          | \_            |
| `part`       | When used with KeyValue data, defines if the transformation is done on the key or on the value. If empty, the transformation applies to both the key and the value.                                            | string  |          |               |
| `when`       | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string  |          |               |

### Identity function (`identity`) <a href="#identity" id="identity"></a>

Simple agent to move data from the input to the output. Could be used for testing or sample applications.

### Language detector (`language-detector`) <a href="#language-detector" id="language-detector"></a>

Detect the language of a message’s data and limit further processing based on language codes.

|                    | Description                                                                                                   | Type            | Required | Default Value |
| ------------------ | ------------------------------------------------------------------------------------------------------------- | --------------- | -------- | ------------- |
| `allowedLanguages` | Define a list of allowed language codes. If the message language is not in this list, the message is dropped. | array of string |          |               |
| `property`         | The name of the message header to write the language code to.                                                 | string          |          | language      |

### Merge key-value format (`merge-key-value`) <a href="#merge-key-value" id="merge-key-value"></a>

Merges the fields of KeyValue records where both the key and value are structured types of the same schema type. Only AVRO and JSON are supported.

|              | Description                                                                                                                                                                                                    | Type    | Required | Default Value |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------- |
| `composable` | Whether this step can be composed with other steps.                                                                                                                                                            | boolean |          | true          |
| `when`       | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string  |          |               |

### Python custom processor (`python-function`) <a href="#python-function" id="python-function"></a>

Run a your own Python processor.\
All the configuration properties are available the class init method.

|             | Description                                                                                       | Type   | Required | Default Value |
| ----------- | ------------------------------------------------------------------------------------------------- | ------ | -------- | ------------- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓        |               |

### Python custom processor (`python-processor`) <a href="#python-processor" id="python-processor"></a>

Run a your own Python processor.\
All the configuration properties are available the class init method.

|             | Description                                                                                       | Type   | Required | Default Value |
| ----------- | ------------------------------------------------------------------------------------------------- | ------ | -------- | ------------- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓        |               |

### Python custom sink (`python-sink`) <a href="#python-sink" id="python-sink"></a>

Run a your own Python sink.\
All the configuration properties are available in the class init method.

|             | Description                                                                                       | Type   | Required | Default Value |
| ----------- | ------------------------------------------------------------------------------------------------- | ------ | -------- | ------------- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓        |               |

### Python custom source (`python-source`) <a href="#python-source" id="python-source"></a>

Run a your own Python source.\
All the configuration properties are available in the class init method.

|             | Description                                                                                       | Type   | Required | Default Value |
| ----------- | ------------------------------------------------------------------------------------------------- | ------ | -------- | ------------- |
| `className` | Python class name to instantiate. This class must be present in the application's "python" files. | string | ✓        |               |

### Query (`query`) <a href="#query" id="query"></a>

Perform a vector search or simple query against a datasource.

|                | Description                                                                                                                                                                                                    | Type            | Required | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- | ------------- |
| `composable`   | Whether this step can be composed with other steps.                                                                                                                                                            | boolean         |          | true          |
| `datasource`   | Reference to a datasource id configured in the application.                                                                                                                                                    | string          | ✓        |               |
| `fields`       | Fields of the record to use as input parameters for the query.                                                                                                                                                 | array of string |          |               |
| `only-first`   | If true, only the first result of the query is stored in the output field.                                                                                                                                     | boolean         |          | false         |
| `output-field` | The name of the field to use to store the query result.                                                                                                                                                        | string          | ✓        |               |
| `query`        | The query to use to extract the data.                                                                                                                                                                          | string          | ✓        |               |
| `when`         | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string          |          |               |

### Query a vector database (`query-vector-db`) <a href="#query-vector-db" id="query-vector-db"></a>

Query a vector database using Vector Search capabilities.

|                | Description                                                                                                                                                                                                    | Type            | Required | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------- | ------------- |
| `composable`   | Whether this step can be composed with other steps.                                                                                                                                                            | boolean         |          | true          |
| `datasource`   | Reference to a datasource id configured in the application.                                                                                                                                                    | string          | ✓        |               |
| `fields`       | Fields of the record to use as input parameters for the query.                                                                                                                                                 | array of string |          |               |
| `only-first`   | If true, only the first result of the query is stored in the output field.                                                                                                                                     | boolean         |          | false         |
| `output-field` | The name of the field to use to store the query result.                                                                                                                                                        | string          | ✓        |               |
| `query`        | The query to use to extract the data.                                                                                                                                                                          | string          | ✓        |               |
| `when`         | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string          |          |               |

### Re-rank (`re-rank`) <a href="#re-rank" id="re-rank"></a>

Agent for re-ranking documents based on a query.

|                    | Description                                                                         | Type    | Required | Default Value |
| ------------------ | ----------------------------------------------------------------------------------- | ------- | -------- | ------------- |
| `algorithm`        | Algorithm to use for re-ranking. 'none' or 'MMR'.                                   | string  |          | none          |
| `b`                | Parameter for B25 algorithm.                                                        | number  |          | 0.75          |
| `embeddings-field` | Result field for the embeddings.                                                    | string  |          |               |
| `field`            | The field that contains the documents to sort.                                      | string  | ✓        |               |
| `k1`               | Parameter for B25 algorithm.                                                        | number  |          | 1.5           |
| `lambda`           | Parameter for MMR algorithm.                                                        | number  |          | 0.5           |
| `max`              | Maximum number of documents to keep.                                                | integer |          | 100           |
| `output-field`     | The field that will hold the results, it can be the same as "field" to override it. | string  | ✓        |               |
| `query-embeddings` | Field that contains the embeddings of the documents to sort.                        | string  |          |               |
| `query-text`       | Field that already contains the text that has been embedded.                        | string  |          |               |
| `text-field`       | Result field for the text.                                                          | string  |          |               |

### S3 Source (`s3-source`) <a href="#s3-source" id="s3-source"></a>

Reads data from S3 bucket

|                   | Description                                           | Type    | Required | Default Value                       |
| ----------------- | ----------------------------------------------------- | ------- | -------- | ----------------------------------- |
| `access-key`      | Access key for the S3 server.                         | string  |          | minioadmin                          |
| `bucketName`      | The name of the bucket to read from.                  | string  |          | langstream-source                   |
| `endpoint`        | The endpoint of the S3 server.                        | string  |          | http://minio-endpoint.-not-set:9090 |
| `file-extensions` | Comma separated list of file extensions to filter by. | string  |          | pdf,docx,html,htm,md,txt            |
| `idle-time`       | Region for the S3 server.                             | integer |          | 5                                   |
| `region`          | Region for the S3 server.                             | string  |          |                                     |
| `secret-key`      | Secret key for the S3 server.                         | string  |          | minioadmin                          |

### Kafka Connect Sink agent (`sink`) <a href="#sink" id="sink"></a>

Run any Kafka Connect Sink.\
All the configuration properties are passed to the Kafka Connect Sink.

|                   | Description                                   | Type   | Required | Default Value |
| ----------------- | --------------------------------------------- | ------ | -------- | ------------- |
| `connector.class` | Java main class for the Kafka Sink connector. | string | ✓        |               |

### Kafka Connect Source agent (`source`) <a href="#source" id="source"></a>

Run any Kafka Connect Source.\
All the configuration properties are passed to the Kafka Connect Source.

|                   | Description                                     | Type   | Required | Default Value |
| ----------------- | ----------------------------------------------- | ------ | -------- | ------------- |
| `connector.class` | Java main class for the Kafka Source connector. | string | ✓        |               |

### Text extractor (`text-extractor`) <a href="#text-extractor" id="text-extractor"></a>

Extracts text content from different document formats like PDF, JSON, XML, ODF, HTML and many others.

### Text normaliser (`text-normaliser`) <a href="#text-normaliser" id="text-normaliser"></a>

Apply normalisation to the text.

|                  | Description                           | Type    | Required | Default Value |
| ---------------- | ------------------------------------- | ------- | -------- | ------------- |
| `make-lowercase` | Whether to make the text lowercase.   | boolean |          | true          |
| `trim-spaces`    | Whether to trim spaces from the text. | boolean |          | true          |

### Text splitter (`text-splitter`) <a href="#text-splitter" id="text-splitter"></a>

Split message content in chunks.

|                   | Description                                                                                                                                                                                | Type            | Required | Default Value                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | -------- | ------------------------------ |
| `chunk_overlap`   | <p>RecursiveCharacterTextSplitter splitter option. Chunk overlap of the previous message.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</p>                        | integer         |          | 100                            |
| `chunk_size`      | <p>RecursiveCharacterTextSplitter splitter option. Chunk size of each message.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</p>                                   | integer         |          | 200                            |
| `keep_separator`  | <p>RecursiveCharacterTextSplitter splitter option. Whether or not to keep separators.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</p>                            | boolean         |          | false                          |
| `length_function` | <p>RecursiveCharacterTextSplitter splitter option. Options are: r50k_base, p50k_base, p50k_edit and cl100k_base.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</p> | string          |          | cl100k\_base                   |
| `separators`      | <p>RecursiveCharacterTextSplitter splitter option. The separator to use for splitting.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</p>                           | array of string |          | "\n\n", "\n", " ", ""          |
| `splitter_type`   | Splitter implementation to use. Currently supported: RecursiveCharacterTextSplitter.                                                                                                       | string          |          | RecursiveCharacterTextSplitter |

### Unwrap key-value format (`unwrap-key-value`) <a href="#unwrap-key-value" id="unwrap-key-value"></a>

If the record value is in KeyValue format, extracts the KeyValue's key or value and make it the record value.

|              | Description                                                                                                                                                                                                    | Type    | Required | Default Value |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ------------- |
| `composable` | Whether this step can be composed with other steps.                                                                                                                                                            | boolean |          | true          |
| `unwrapKey`  | Whether to unwrap the key instead of the value.                                                                                                                                                                | boolean |          | false         |
| `when`       | <p>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</p> | string  |          |               |

### Vector database sink (`vector-db-sink`) <a href="#vector-db-sink" id="vector-db-sink"></a>

Store vectors in a vector database.\
Configuration properties depends on the vector database implementation, specified by the "datasource" property.

|              | Description                                            | Type   | Required | Default Value |
| ------------ | ------------------------------------------------------ | ------ | -------- | ------------- |
| `datasource` | The defined datasource ID to use to store the vectors. | string | ✓        |               |

### Web crawler source (`webcrawler-source`) <a href="#webcrawler-source" id="webcrawler-source"></a>

Crawl a website and extract the content of the pages.

|                             | Description                                                                          | Type            | Required | Default Value                                                       |
| --------------------------- | ------------------------------------------------------------------------------------ | --------------- | -------- | ------------------------------------------------------------------- |
| `access-key`                | <p>Configuration for handling the agent status.<br>Access key for the S3 server.</p> | string          |          | minioadmin                                                          |
| `allowed-domains`           | Domains that the crawler is allowed to access.                                       | array of string |          |                                                                     |
| `bucketName`                | <p>Configuration for handling the agent status.<br>The name of the bucket.</p>       | string          |          | langstream-source                                                   |
| `endpoint`                  | <p>Configuration for handling the agent status.<br>The S3 endpoint.</p>              | string          |          | http://minio-endpoint.-not-set:9090                                 |
| `forbidden-paths`           | Paths that the crawler is not allowed to access.                                     | array of string |          |                                                                     |
| `handle-cookies`            | Whether to handle cookies.                                                           | boolean         |          | true                                                                |
| `handle-robots-file`        | Whether to scan the HTML documents to find links to other pages.                     | boolean         |          | true                                                                |
| `http-timeout`              | Timeout for HTTP requests. (in milliseconds)                                         | integer         |          | 10000                                                               |
| `max-depth`                 | Maximum depth of the crawl.                                                          | integer         |          | 50                                                                  |
| `max-error-count`           | Maximum number of errors allowed before stopping.                                    | integer         |          | 5                                                                   |
| `max-unflushed-pages`       | Maximum number of unflushed pages before the agent persists the crawl data.          | integer         |          | 100                                                                 |
| `max-urls`                  | Maximum number of URLs that can be crawled.                                          | integer         |          | 1000                                                                |
| `min-time-between-requests` | Minimum time between two requests to the same domain. (in milliseconds)              | integer         |          | 500                                                                 |
| `region`                    | <p>Configuration for handling the agent status.<br>Region for the S3 server.</p>     | string          |          |                                                                     |
| `reindex-interval-seconds`  | Time interval between reindexing of the pages.                                       | integer         |          | 86400                                                               |
| `scan-html-documents`       | Whether to scan HTML documents for links to other sites.                             | boolean         |          | true                                                                |
| `secret-key`                | <p>Configuration for handling the agent status.<br>Secret key for the S3 server.</p> | string          |          | minioadmin                                                          |
| `seed-urls`                 | The starting URLs for the crawl.                                                     | array of string |          |                                                                     |
| `user-agent`                | User agent to use for the requests.                                                  | string          |          | Mozilla/5.0 (compatible; LangStream.ai/0.1; +https://langstream.ai) |
