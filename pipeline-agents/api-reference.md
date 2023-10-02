# API Reference

## Agents

| ID | Name | Description |
| --- | --- | --- |
| <a href="#ai-chat-completions">ai-chat-completions</a> |  |  |
| <a href="#ai-text-completions">ai-text-completions</a> |  |  |
| <a href="#cast">cast</a> |  |  |
| <a href="#composite-agent">composite-agent</a> |  |  |
| <a href="#compute">compute</a> |  |  |
| <a href="#compute-ai-embeddings">compute-ai-embeddings</a> |  |  |
| <a href="#document-to-json">document-to-json</a> |  |  |
| <a href="#drop">drop</a> |  |  |
| <a href="#drop-fields">drop-fields</a> | Drop fields from the input record |  |
| <a href="#flatten">flatten</a> |  |  |
| <a href="#identity">identity</a> |  |  |
| <a href="#language-detector">language-detector</a> |  |  |
| <a href="#merge-key-value">merge-key-value</a> |  |  |
| <a href="#noop">noop</a> |  |  |
| <a href="#python-function">python-function</a> |  |  |
| <a href="#python-processor">python-processor</a> |  |  |
| <a href="#python-sink">python-sink</a> |  |  |
| <a href="#python-source">python-source</a> |  |  |
| <a href="#query">query</a> |  |  |
| <a href="#query-vector-db">query-vector-db</a> |  |  |
| <a href="#s3-source">s3-source</a> | S3 Source | Reads data from S3 bucket |
| <a href="#sink">sink</a> |  |  |
| <a href="#source">source</a> |  |  |
| <a href="#text-extractor">text-extractor</a> |  |  |
| <a href="#text-normaliser">text-normaliser</a> |  |  |
| <a href="#text-splitter">text-splitter</a> |  |  |
| <a href="#unwrap-key-value">unwrap-key-value</a> |  |  |
| <a href="#vector-db-sink">vector-db-sink</a> |  |  |
| <a href="#webcrawler-source">webcrawler-source</a> |  |  |


### <a name="drop"></a>drop

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### <a name="drop-fields"></a>drop-fields

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| fields | Fields to drop from the input record. | <a href="#drop-fields.fields">array of object</a> | ✓ |  |
| part | Part to drop. (value or key) | string |  |  |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


#### <a name="drop-fields.fields"></a>drop-fields.fields

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| inner-composable | Whether this step can be composed with other steps. | boolean |  | true |


### <a name="merge-key-value"></a>merge-key-value

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### <a name="s3-source"></a>s3-source

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| access-key | Access key for the S3 server. | string |  | minioadmin |
| bucketName | The name of the bucket to read from. | string |  | langstream-source |
| endpoint | The endpoint of the S3 server. | string |  | http://minio-endpoint.-not-set:9090 |
| file-extensions | Comma separated list of file extensions to filter by. | string |  | pdf,docx,html,htm,md,txt |
| idle-time | Region for the S3 server. | integer |  | 5 |
| region | Region for the S3 server. | string |  |  |
| secret-key | Secret key for the S3 server. | string |  | minioadmin |
