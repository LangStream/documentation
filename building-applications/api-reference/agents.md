# Agents

LangStream Version: **0.2.0**

\


## Compute chat completions (`ai-chat-completions`) <a href="#ai-chat-completions" id="ai-chat-completions"></a>

Sends the messages to the AI Service to compute chat completions. The result is stored in the specified field.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>ai-service</code></td><td>In case of multiple AI services configured, specify the id of the AI service to use.</td><td>string</td><td></td><td></td></tr><tr><td><code>completion-field</code></td><td>Field to use to store the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.&#x3C;field>" to write the result in a specific field.</td><td>string</td><td></td><td></td></tr><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>frequency-penalty</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>log-field</code></td><td>Field to use to store the log of the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.&#x3C;field>" to write the result in a specific field.<br>The log contains useful information for debugging the completion prompts.</td><td>string</td><td></td><td></td></tr><tr><td><code>logit-bias</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>object</td><td></td><td></td></tr><tr><td><code>max-tokens</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>integer</td><td></td><td></td></tr><tr><td><code>messages</code></td><td>Messages to use for chat completions. You can use the Mustache syntax.</td><td><a href="agents.md#ai-chat-completions.messages">array of object</a></td><td>✓</td><td></td></tr><tr><td><code>min-chunks-per-message</code></td><td>Minimum number of chunks to send to the stream-to-topic topic. The chunks are sent as soon as they are available.<br>The chunks are sent in the order they are received from the AI Service.<br>To improve the TTFB (Time-To-First-Byte), the chunk size starts from 1 and doubles until it reaches the max-chunks-per-message value.</td><td>integer</td><td></td><td>20</td></tr><tr><td><code>model</code></td><td>The model to use for chat completions. The model must be available in the AI Service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>presence-penalty</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>stop</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>stream</code></td><td>Enable streaming of the results. Use in conjunction with the stream-to-topic parameter.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>stream-response-completion-field</code></td><td>Field to use to store the completion results in the stream-to-topic topic. Use "value" to write the result without a structured schema. Use "value.&#x3C;field>" to write the result in a specific field.</td><td>string</td><td></td><td></td></tr><tr><td><code>stream-to-topic</code></td><td>Enable streaming of the results. If enabled, the results are streamed to the specified topic in small chunks. The entire messages will be sent to the output topic instead.</td><td>string</td><td></td><td></td></tr><tr><td><code>temperature</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>top-p</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>user</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>string</td><td></td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


### Compute chat completions (`ai-chat-completions`).messages <a href="#ai-chat-completions.messages" id="ai-chat-completions.messages"></a>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>role</code></td><td>Role of the message. The role is used to identify the speaker in the chat.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>content</code></td><td>Content of the message. You can use the Mustache syntax.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Compute text completions (`ai-text-completions`) <a href="#ai-text-completions" id="ai-text-completions"></a>

Sends the text to the AI Service to compute text completions. The result is stored in the specified field.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>ai-service</code></td><td>In case of multiple AI services configured, specify the id of the AI service to use.</td><td>string</td><td></td><td></td></tr><tr><td><code>completion-field</code></td><td>Field to use to store the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.&#x3C;field>" to write the result in a specific field.</td><td>string</td><td></td><td></td></tr><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>frequency-penalty</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>log-field</code></td><td>Field to use to store the log of the completion results in the output topic. Use "value" to write the result without a structured schema. Use "value.&#x3C;field>" to write the result in a specific field.<br>The log contains useful information for debugging the completion prompts.</td><td>string</td><td></td><td></td></tr><tr><td><code>logit-bias</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>object</td><td></td><td></td></tr><tr><td><code>logprobs</code></td><td>Logprobs parameter (only valid for OpenAI).</td><td>string</td><td></td><td></td></tr><tr><td><code>logprobs-field</code></td><td>Log probabilities to a field.</td><td>string</td><td></td><td></td></tr><tr><td><code>max-tokens</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>integer</td><td></td><td></td></tr><tr><td><code>min-chunks-per-message</code></td><td>Minimum number of chunks to send to the stream-to-topic topic. The chunks are sent as soon as they are available.<br>The chunks are sent in the order they are received from the AI Service.<br>To improve the TTFB (Time-To-First-Byte), the chunk size starts from 1 and doubles until it reaches the max-chunks-per-message value.</td><td>integer</td><td></td><td>20</td></tr><tr><td><code>model</code></td><td>The model to use for text completions. The model must be available in the AI Service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>presence-penalty</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>prompt</code></td><td>Prompt to use for text completions. You can use the Mustache syntax.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>stop</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>stream</code></td><td>Enable streaming of the results. Use in conjunction with the stream-to-topic parameter.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>stream-response-completion-field</code></td><td>Field to use to store the completion results in the stream-to-topic topic. Use "value" to write the result without a structured schema. Use "value.&#x3C;field>" to write the result in a specific field.</td><td>string</td><td></td><td></td></tr><tr><td><code>stream-to-topic</code></td><td>Enable streaming of the results. If enabled, the results are streamed to the specified topic in small chunks. The entire messages will be sent to the output topic instead.</td><td>string</td><td></td><td></td></tr><tr><td><code>temperature</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>top-p</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>number</td><td></td><td></td></tr><tr><td><code>user</code></td><td>Parameter for the completion request. The parameters are passed to the AI Service as is.</td><td>string</td><td></td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Azure Blob Storage Source (`azure-blob-storage-source`) <a href="#azure-blob-storage-source" id="azure-blob-storage-source"></a>

Reads data from Azure blobs. There are three supported ways to authenticate:\
\- SAS token\
\- Storage account name and key\
\- Storage account connection string

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>container</code></td><td>The name of the Azure econtainer to read from.</td><td>string</td><td></td><td>langstream-azure-source</td></tr><tr><td><code>endpoint</code></td><td>Endpoint to connect to. Usually it's https://&#x3C;storage-account>.blob.core.windows.net.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>file-extensions</code></td><td>Comma separated list of file extensions to filter by.</td><td>string</td><td></td><td>pdf,docx,html,htm,md,txt</td></tr><tr><td><code>idle-time</code></td><td>Time in seconds to sleep after polling for new files.</td><td>integer</td><td></td><td>5</td></tr><tr><td><code>sas-token</code></td><td>Azure SAS token. If not provided, storage account name and key must be provided.</td><td>string</td><td></td><td></td></tr><tr><td><code>storage-account-connection-string</code></td><td>Azure storage account connection string. If not provided, SAS token must be provided.</td><td>string</td><td></td><td></td></tr><tr><td><code>storage-account-key</code></td><td>Azure storage account key. If not provided, SAS token must be provided.</td><td>string</td><td></td><td></td></tr><tr><td><code>storage-account-name</code></td><td>Azure storage account name. If not provided, SAS token must be provided.</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Cast record to another schema (`cast`) <a href="#cast" id="cast"></a>

Transforms the data to a target compatible schema.\
Some step operations like cast or compute involve conversions from a type to another. When this happens the rules are:\
\- timestamp, date and time related object conversions assume UTC time zone if it is not explicit.\
\- date and time related object conversions to/from STRING use the RFC3339 format.\
\- timestamp related object conversions to/from LONG and DOUBLE are done using the number of milliseconds since EPOCH (1970-01-01T00:00:00Z).\
\- date related object conversions to/from INTEGER, LONG, FLOAT and DOUBLE are done using the number of days since EPOCH (1970-01-01).\
\- time related object conversions to/from INTEGER, LONG and DOUBLE are done using the number of milliseconds since midnight (00:00:00).

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>part</code></td><td>When used with KeyValue data, defines if the transformation is done on the key or on the value. If empty, the transformation applies to both the key and the value.</td><td>string</td><td></td><td></td></tr><tr><td><code>schema-type</code></td><td>The target schema type.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Compute values from the record (`compute`) <a href="#compute" id="compute"></a>

Computes new properties, values or field values based on an expression evaluated at runtime. If the field already exists, it will be overwritten.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>fields</code></td><td>An array of objects describing how to calculate the field values</td><td><a href="agents.md#compute.fields">array of object</a></td><td>✓</td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


### Compute values from the record (`compute`).fields <a href="#compute.fields" id="compute.fields"></a>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>expression</code></td><td>It is evaluated at runtime and the result of the evaluation is assigned to the field.<br>Refer to the language expression documentation for more information on the expression syntax.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>name</code></td><td>The name of the field to be computed. Prefix with key. or value. to compute the fields in the key or value parts of the message.<br>In addition, you can compute values on the following message headers [destinationTopic, messageKey, properties.].<br>Please note that properties is a map of key/value pairs that are referenced by the dot notation, for example properties.key0.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>optional</code></td><td>If true, it marks the field as optional in the schema of the transformed message. This is useful when null is a possible value of the compute expression.</td><td>boolean</td><td></td><td>false</td></tr><tr><td><code>type</code></td><td>The type of the computed field. This<br>will translate to the schema type of the new field in the transformed message.<br>The following types are currently supported :STRING, INT8, INT16, INT32, INT64, FLOAT, DOUBLE, BOOLEAN, DATE, TIME, TIMESTAMP, LOCAL_DATE_TIME, LOCAL_TIME, LOCAL_DATE, INSTANT.<br>The type field is not required for the message headers [destinationTopic, messageKey, properties.] and STRING will be used.<br>For the value and key, if it is not provided, then the type will be inferred from the result of the expression evaluation.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Compute embeddings of the record (`compute-ai-embeddings`) <a href="#compute-ai-embeddings" id="compute-ai-embeddings"></a>

Compute embeddings of the record. The embeddings are stored in the record under a specific field.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>ai-service</code></td><td>In case of multiple AI services configured, specify the id of the AI service to use.</td><td>string</td><td></td><td></td></tr><tr><td><code>arguments</code></td><td>Additional arguments to pass to the AI Service. (HuggingFace only)</td><td>object</td><td></td><td></td></tr><tr><td><code>batch-size</code></td><td>Batch size for submitting the embeddings requests.</td><td>integer</td><td></td><td>10</td></tr><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>concurrency</code></td><td>Max number of concurrent requests to the AI Service.</td><td>integer</td><td></td><td>4</td></tr><tr><td><code>embeddings-field</code></td><td>Field where to store the embeddings.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>flush-interval</code></td><td>Flushing is disabled by default in order to avoid latency spikes.<br>You should enable this feature in the case of background processing.</td><td>integer</td><td></td><td>0</td></tr><tr><td><code>loop-over</code></td><td>Execute the agent over a list of documents</td><td>string</td><td></td><td></td></tr><tr><td><code>model</code></td><td>Model to use for the embeddings. The model must be available in the configured AI Service.</td><td>string</td><td></td><td>text-embedding-ada-002</td></tr><tr><td><code>modelUrl</code></td><td>URL of the model to use. (HuggingFace only). The default is computed from the model: "djl://ai.djl.huggingface.pytorch{model}"</td><td>string</td><td></td><td></td></tr><tr><td><code>options</code></td><td>Additional options to pass to the AI Service. (HuggingFace only)</td><td>object</td><td></td><td></td></tr><tr><td><code>text</code></td><td>Text to create embeddings from. You can use Mustache syntax to compose multiple fields into a single text. Example:<br>text: "{{{ value.field1 }}} {{{ value.field2 }}}"</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Dispatch agent (`dispatch`) <a href="#dispatch" id="dispatch"></a>

Dispatches messages to different destinations based on conditions.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>routes</code></td><td>Routes.</td><td><a href="agents.md#dispatch.routes">array of object</a></td><td></td><td></td></tr></tbody></table>

\


### Dispatch agent (`dispatch`).routes <a href="#dispatch.routes" id="dispatch.routes"></a>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>destination</code></td><td>Destination of the message.</td><td>string</td><td></td><td></td></tr><tr><td><code>action</code></td><td>Action on the message. Possible values are "dispatch" or "drop".</td><td>string</td><td></td><td>dispatch</td></tr><tr><td><code>when</code></td><td>Condition to activate the route. This is a standard EL expression.</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Document to JSON (`document-to-json`) <a href="#document-to-json" id="document-to-json"></a>

Convert raw text document to JSON. The result will be a JSON object with the text content in the specified field.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>copy-properties</code></td><td>Whether to copy the message properties/headers in the output message.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>text-field</code></td><td>Field name to write the text content to.</td><td>string</td><td></td><td>text</td></tr></tbody></table>

\


## Drop the record (`drop`) <a href="#drop" id="drop"></a>

Drops the record from further processing. Use in conjunction with when to selectively drop records.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Drop fields (`drop-fields`) <a href="#drop-fields" id="drop-fields"></a>

Drops the record fields.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>fields</code></td><td>Fields to drop from the input record.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>part</code></td><td>Part to drop. (value or key)</td><td>string</td><td></td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Flare Controller (`flare-controller`) <a href="#flare-controller" id="flare-controller"></a>

Apply to the Flare pattern to enhance the quality of text completion results.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>logprobs-field</code></td><td>The field that contains the logprobs of tokens returned by the ai-text-completion agent.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>loop-topic</code></td><td>Name of the topic to forward the message in case of requesting more documents.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>retrieve-documents-field</code></td><td>Name of the field to set in order to request the retrival of more documents.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>tokens-field</code></td><td>The field that contains the list of tokens returned by the ai-text-completion agent.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Flatten record fields (`flatten`) <a href="#flatten" id="flatten"></a>

Converts structured nested data into a new single-hierarchy-level structured data. The names of the new fields are built by concatenating the intermediate level field names.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>delimiter</code></td><td>The delimiter to use when concatenating the field names.</td><td>string</td><td></td><td>_</td></tr><tr><td><code>part</code></td><td>When used with KeyValue data, defines if the transformation is done on the key or on the value. If empty, the transformation applies to both the key and the value.</td><td>string</td><td></td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Http Request (`http-request`) <a href="#http-request" id="http-request"></a>

Agent for enriching data with an HTTP request.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>allow-redirects</code></td><td>Whether or not to follow redirects.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>body</code></td><td>Body to send with the request. You can use the Mustache syntax to inject value from the context.</td><td>string</td><td></td><td></td></tr><tr><td><code>handle-cookies</code></td><td>Whether or not to handle cookies during the redirects.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>headers</code></td><td>Headers to send with the request. You can use the Mustache syntax to inject value from the context.</td><td>object</td><td></td><td></td></tr><tr><td><code>method</code></td><td>Http method to use for the request.</td><td>string</td><td></td><td>GET</td></tr><tr><td><code>output-field</code></td><td>The field that will hold the results, it can be the same as "field" to override it.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>query-string</code></td><td>Query string to append to the url. You can use the Mustache syntax to inject value from the context.<br>Note that the values will be automatically escaped.</td><td>object</td><td></td><td></td></tr><tr><td><code>url</code></td><td>Url to send the request to. For adding query string parameters, use the `query-string` field.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Identity function (`identity`) <a href="#identity" id="identity"></a>

Simple agent to move data from the input to the output. Could be used for testing or sample applications.

\


## Language detector (`language-detector`) <a href="#language-detector" id="language-detector"></a>

Detect the language of a message’s data and limit further processing based on language codes.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>allowedLanguages</code></td><td>Define a list of allowed language codes. If the message language is not in this list, the message is dropped.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>property</code></td><td>The name of the message header to write the language code to.</td><td>string</td><td></td><td>language</td></tr></tbody></table>

\


## Merge key-value format (`merge-key-value`) <a href="#merge-key-value" id="merge-key-value"></a>

Merges the fields of KeyValue records where both the key and value are structured types of the same schema type. Only AVRO and JSON are supported.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Python custom processor (`python-function`) <a href="#python-function" id="python-function"></a>

Run a your own Python processor.\
All the configuration properties are available the class init method.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>className</code></td><td>Python class name to instantiate. This class must be present in the application's "python" files.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Python custom processor (`python-processor`) <a href="#python-processor" id="python-processor"></a>

Run a your own Python processor.\
All the configuration properties are available the class init method.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>className</code></td><td>Python class name to instantiate. This class must be present in the application's "python" files.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Python custom sink (`python-sink`) <a href="#python-sink" id="python-sink"></a>

Run a your own Python sink.\
All the configuration properties are available in the class init method.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>className</code></td><td>Python class name to instantiate. This class must be present in the application's "python" files.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Python custom source (`python-source`) <a href="#python-source" id="python-source"></a>

Run a your own Python source.\
All the configuration properties are available in the class init method.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>className</code></td><td>Python class name to instantiate. This class must be present in the application's "python" files.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Query (`query`) <a href="#query" id="query"></a>

Perform a vector search or simple query against a datasource.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>fields</code></td><td>Fields of the record to use as input parameters for the query.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>loop-over</code></td><td>Loop over a list of items taken from the record. For instance value.documents.<br>It must refer to a list of maps. In this case the output-field parameter<br>but be like "record.fieldname" in order to replace or set a field in each record<br>with the results of the query. In the query parameters you can refer to the<br>record fields using "record.field".</td><td>string</td><td></td><td></td></tr><tr><td><code>only-first</code></td><td>If true, only the first result of the query is stored in the output field.</td><td>boolean</td><td></td><td>false</td></tr><tr><td><code>output-field</code></td><td>The name of the field to use to store the query result.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>query</code></td><td>The query to use to extract the data.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Query a vector database (`query-vector-db`) <a href="#query-vector-db" id="query-vector-db"></a>

Query a vector database using Vector Search capabilities.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>fields</code></td><td>Fields of the record to use as input parameters for the query.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>loop-over</code></td><td>Loop over a list of items taken from the record. For instance value.documents.<br>It must refer to a list of maps. In this case the output-field parameter<br>but be like "record.fieldname" in order to replace or set a field in each record<br>with the results of the query. In the query parameters you can refer to the<br>record fields using "record.field".</td><td>string</td><td></td><td></td></tr><tr><td><code>only-first</code></td><td>If true, only the first result of the query is stored in the output field.</td><td>boolean</td><td></td><td>false</td></tr><tr><td><code>output-field</code></td><td>The name of the field to use to store the query result.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>query</code></td><td>The query to use to extract the data.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Re-rank (`re-rank`) <a href="#re-rank" id="re-rank"></a>

Agent for re-ranking documents based on a query.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>algorithm</code></td><td>Algorithm to use for re-ranking. 'none' or 'MMR'.</td><td>string</td><td></td><td>none</td></tr><tr><td><code>b</code></td><td>Parameter for B25 algorithm.</td><td>number</td><td></td><td>0.75</td></tr><tr><td><code>embeddings-field</code></td><td>Result field for the embeddings.</td><td>string</td><td></td><td></td></tr><tr><td><code>field</code></td><td>The field that contains the documents to sort.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>k1</code></td><td>Parameter for B25 algorithm.</td><td>number</td><td></td><td>1.5</td></tr><tr><td><code>lambda</code></td><td>Parameter for MMR algorithm.</td><td>number</td><td></td><td>0.5</td></tr><tr><td><code>max</code></td><td>Maximum number of documents to keep.</td><td>integer</td><td></td><td>100</td></tr><tr><td><code>output-field</code></td><td>The field that will hold the results, it can be the same as "field" to override it.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>query-embeddings</code></td><td>Field that contains the embeddings of the documents to sort.</td><td>string</td><td></td><td></td></tr><tr><td><code>query-text</code></td><td>Field that already contains the text that has been embedded.</td><td>string</td><td></td><td></td></tr><tr><td><code>text-field</code></td><td>Result field for the text.</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## S3 Source (`s3-source`) <a href="#s3-source" id="s3-source"></a>

Reads data from S3 bucket

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>access-key</code></td><td>Access key for the S3 server.</td><td>string</td><td></td><td>minioadmin</td></tr><tr><td><code>bucketName</code></td><td>The name of the bucket to read from.</td><td>string</td><td></td><td>langstream-source</td></tr><tr><td><code>endpoint</code></td><td>The endpoint of the S3 server.</td><td>string</td><td></td><td>http://minio-endpoint.-not-set:9090</td></tr><tr><td><code>file-extensions</code></td><td>Comma separated list of file extensions to filter by.</td><td>string</td><td></td><td>pdf,docx,html,htm,md,txt</td></tr><tr><td><code>idle-time</code></td><td>Time in seconds to sleep after polling for new files.</td><td>integer</td><td></td><td>5</td></tr><tr><td><code>region</code></td><td>Region for the S3 server.</td><td>string</td><td></td><td></td></tr><tr><td><code>secret-key</code></td><td>Secret key for the S3 server.</td><td>string</td><td></td><td>minioadmin</td></tr></tbody></table>

\


## Kafka Connect Sink agent (`sink`) <a href="#sink" id="sink"></a>

Run any Kafka Connect Sink.\
All the configuration properties are passed to the Kafka Connect Sink.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>connector.class</code></td><td>Java main class for the Kafka Sink connector.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Kafka Connect Source agent (`source`) <a href="#source" id="source"></a>

Run any Kafka Connect Source.\
All the configuration properties are passed to the Kafka Connect Source.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>connector.class</code></td><td>Java main class for the Kafka Source connector.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Text extractor (`text-extractor`) <a href="#text-extractor" id="text-extractor"></a>

Extracts text content from different document formats like PDF, JSON, XML, ODF, HTML and many others.

\


## Text normaliser (`text-normaliser`) <a href="#text-normaliser" id="text-normaliser"></a>

Apply normalisation to the text.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>make-lowercase</code></td><td>Whether to make the text lowercase.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>trim-spaces</code></td><td>Whether to trim spaces from the text.</td><td>boolean</td><td></td><td>true</td></tr></tbody></table>

\


## Text splitter (`text-splitter`) <a href="#text-splitter" id="text-splitter"></a>

Split message content in chunks.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>chunk_overlap</code></td><td>RecursiveCharacterTextSplitter splitter option. Chunk overlap of the previous message.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</td><td>integer</td><td></td><td>100</td></tr><tr><td><code>chunk_size</code></td><td>RecursiveCharacterTextSplitter splitter option. Chunk size of each message.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</td><td>integer</td><td></td><td>200</td></tr><tr><td><code>keep_separator</code></td><td>RecursiveCharacterTextSplitter splitter option. Whether or not to keep separators.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</td><td>boolean</td><td></td><td>false</td></tr><tr><td><code>length_function</code></td><td>RecursiveCharacterTextSplitter splitter option. Options are: r50k_base, p50k_base, p50k_edit and cl100k_base.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</td><td>string</td><td></td><td>cl100k_base</td></tr><tr><td><code>separators</code></td><td>RecursiveCharacterTextSplitter splitter option. The separator to use for splitting.<br>Checkout https://github.com/knuddelsgmbh/jtokkit for more details.</td><td>array of string</td><td></td><td>"\n\n", "\n", " ", ""</td></tr><tr><td><code>splitter_type</code></td><td>Splitter implementation to use. Currently supported: RecursiveCharacterTextSplitter.</td><td>string</td><td></td><td>RecursiveCharacterTextSplitter</td></tr></tbody></table>

\


## Unwrap key-value format (`unwrap-key-value`) <a href="#unwrap-key-value" id="unwrap-key-value"></a>

If the record value is in KeyValue format, extracts the KeyValue's key or value and make it the record value.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>composable</code></td><td>Whether this step can be composed with other steps.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>unwrapKey</code></td><td>Whether to unwrap the key instead of the value.</td><td>boolean</td><td></td><td>false</td></tr><tr><td><code>when</code></td><td>Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' &#x26;&#x26; value.last.toUpperCase() == 'L1'"</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Vector database sink (`vector-db-sink`) <a href="#vector-db-sink" id="vector-db-sink"></a>

Store vectors in a vector database.\
Configuration properties depends on the vector database implementation, specified by the "datasource" property.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>datasource</code></td><td>The defined datasource ID to use to store the vectors.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Web crawler source (`webcrawler-source`) <a href="#webcrawler-source" id="webcrawler-source"></a>

Crawl a website and extract the content of the pages.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>access-key</code></td><td>Configuration for handling the agent status.<br>Access key for the S3 server.</td><td>string</td><td></td><td>minioadmin</td></tr><tr><td><code>allowed-domains</code></td><td>Domains that the crawler is allowed to access.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>bucketName</code></td><td>Configuration for handling the agent status.<br>The name of the bucket.</td><td>string</td><td></td><td>langstream-source</td></tr><tr><td><code>endpoint</code></td><td>Configuration for handling the agent status.<br>The S3 endpoint.</td><td>string</td><td></td><td>http://minio-endpoint.-not-set:9090</td></tr><tr><td><code>forbidden-paths</code></td><td>Paths that the crawler is not allowed to access.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>handle-cookies</code></td><td>Whether to handle cookies.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>handle-robots-file</code></td><td>Whether to scan the HTML documents to find links to other pages.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>http-timeout</code></td><td>Timeout for HTTP requests. (in milliseconds)</td><td>integer</td><td></td><td>10000</td></tr><tr><td><code>max-depth</code></td><td>Maximum depth of the crawl.</td><td>integer</td><td></td><td>50</td></tr><tr><td><code>max-error-count</code></td><td>Maximum number of errors allowed before stopping.</td><td>integer</td><td></td><td>5</td></tr><tr><td><code>max-unflushed-pages</code></td><td>Maximum number of unflushed pages before the agent persists the crawl data.</td><td>integer</td><td></td><td>100</td></tr><tr><td><code>max-urls</code></td><td>Maximum number of URLs that can be crawled.</td><td>integer</td><td></td><td>1000</td></tr><tr><td><code>min-time-between-requests</code></td><td>Minimum time between two requests to the same domain. (in milliseconds)</td><td>integer</td><td></td><td>500</td></tr><tr><td><code>region</code></td><td>Configuration for handling the agent status.<br>Region for the S3 server.</td><td>string</td><td></td><td></td></tr><tr><td><code>reindex-interval-seconds</code></td><td>Time interval between reindexing of the pages.</td><td>integer</td><td></td><td>86400</td></tr><tr><td><code>scan-html-documents</code></td><td>Whether to scan HTML documents for links to other sites.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>secret-key</code></td><td>Configuration for handling the agent status.<br>Secret key for the S3 server.</td><td>string</td><td></td><td>minioadmin</td></tr><tr><td><code>seed-urls</code></td><td>The starting URLs for the crawl.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>user-agent</code></td><td>User agent to use for the requests.</td><td>string</td><td></td><td>Mozilla/5.0 (compatible; LangStream.ai/0.1; +https://langstream.ai)</td></tr></tbody></table>
