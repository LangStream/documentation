# API Reference

## Agents

| ID | Name | Description |
| --- | --- | --- |
| <h3><a href="#ai-chat-completions">ai-chat-completions</a></h3>() |  |  |
| <h3><a href="#ai-text-completions">ai-text-completions</a></h3>() |  |  |
| <h3><a href="#cast">cast</a></h3>() |  |  |
| <h3><a href="#composite-agent">composite-agent</a></h3>() |  |  |
| <h3><a href="#compute">compute</a></h3>() |  |  |
| <h3><a href="#compute-ai-embeddings">compute-ai-embeddings</a></h3>() |  |  |
| <h3><a href="#document-to-json">document-to-json</a></h3>() |  |  |
| <h3><a href="#drop">drop</a></h3>() |  |  |
| <h3><a href="#drop-fields">drop-fields</a></h3>() | Drop fields from the input record |  |
| <h3><a href="#flatten">flatten</a></h3>() |  |  |
| <h3><a href="#identity">identity</a></h3>() |  |  |
| <h3><a href="#language-detector">language-detector</a></h3>() |  |  |
| <h3><a href="#merge-key-value">merge-key-value</a></h3>() |  |  |
| <h3><a href="#noop">noop</a></h3>() |  |  |
| <h3><a href="#python-function">python-function</a></h3>() |  |  |
| <h3><a href="#python-processor">python-processor</a></h3>() |  |  |
| <h3><a href="#python-sink">python-sink</a></h3>() |  |  |
| <h3><a href="#python-source">python-source</a></h3>() |  |  |
| <h3><a href="#query">query</a></h3>() |  |  |
| <h3><a href="#query-vector-db">query-vector-db</a></h3>() |  |  |
| <h3><a href="#s3-source">s3-source</a></h3>() | S3 Source | Reads data from S3 bucket |
| <h3><a href="#sink">sink</a></h3>() |  |  |
| <h3><a href="#source">source</a></h3>() |  |  |
| <h3><a href="#text-extractor">text-extractor</a></h3>() |  |  |
| <h3><a href="#text-normaliser">text-normaliser</a></h3>() |  |  |
| <h3><a href="#text-splitter">text-splitter</a></h3>() |  |  |
| <h3><a href="#unwrap-key-value">unwrap-key-value</a></h3>() |  |  |
| <h3><a href="#vector-db-sink">vector-db-sink</a></h3>() |  |  |
| <h3><a href="#webcrawler-source">webcrawler-source</a></h3>() |  |  |


### drop

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### drop-fields

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| fields | Fields to drop from the input record. | <h3><a href="#drop-fields.fields">array of object</a></h3> | ✓ |  |
| part | Part to drop. (value or key) | string |  |  |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


#### <a name="drop-fields.fields"></a>drop-fields.fields

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| inner-composable | Whether this step can be composed with other steps. | boolean |  | true |


### merge-key-value

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### s3-source

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| access-key | Access key for the S3 server. | string |  | minioadmin |
| bucketName | The name of the bucket to read from. | string |  | langstream-source |
| endpoint | The endpoint of the S3 server. | string |  | http://minio-endpoint.-not-set:9090 |
| file-extensions | Comma separated list of file extensions to filter by. | string |  | pdf,docx,html,htm,md,txt |
| idle-time | Region for the S3 server. | integer |  | 5 |
| region | Region for the S3 server. | string |  |  |
| secret-key | Secret key for the S3 server. | string |  | minioadmin |
