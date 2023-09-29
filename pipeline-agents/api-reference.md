# API Reference

## Agents

| ID | Name | Description |
| --- | --- | --- |
| [ai-chat-completions](#my-anchor) |  |  |
| [ai-text-completions](#ai-text-completions) |  |  |
| [cast](#cast) |  |  |
| [composite-agent](#composite-agent) |  |  |
| [compute](#compute) |  |  |
| [compute-ai-embeddings](#compute-ai-embeddings) |  |  |
| [document-to-json](#document-to-json) |  |  |
| [drop](#drop) |  |  |
| [drop-fields](#drop-fields) | Drop fields from the input record |  |
| [flatten](#flatten) |  |  |
| [identity](#identity) |  |  |
| [language-detector](#language-detector) |  |  |
| [merge-key-value](#merge-key-value) |  |  |
| [noop](#noop) |  |  |
| [python-function](#python-function) |  |  |
| [python-processor](#python-processor) |  |  |
| [python-sink](#python-sink) |  |  |
| [python-source](#python-source) |  |  |
| [query](#query) |  |  |
| [query-vector-db](../get-started.md) |  |  |
| [s3-source](../pipeline-agents/api-reference.md#agents) | S3 Source | Reads data from S3 bucket |
| [sink](../pipeline-agents/api-reference.md) |  |  |
| [source](#source) |  |  |
| [text-extractor](#text-extractor) |  |  |
| [text-normaliser](#text-normaliser) |  |  |
| [text-splitter](#text-splitter) |  |  |
| [unwrap-key-value](#unwrap-key-value) |  |  |
| [vector-db-sink](#vector-db-sink) |  |  |
| [webcrawler-source](#webcrawler-source) |  |  |


### drop

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


### drop-fields

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| composable | Whether this step can be composed with other steps. | boolean |  | true |
| fields | Fields to drop from the input record. | array of [object](#drop-fields.fields) | ✓ |  |
| part | Part to drop. (value or key) | string |  |  |
| when | Execute the step only when the condition is met.<br>You can use the expression language to reference the message.<br>Example: when: "value.first == 'f1' && value.last.toUpperCase() == 'L1'" | string |  |  |


#### <a name="drop-fields.fields"></a>drop-fields.fields

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| inner-composable | Whether this step can be composed with other steps. | boolean |  | true |


### merge-key-value {#my-anchor}

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
