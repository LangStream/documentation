# API Reference

- [Resources](#resources)

## Resources

| ID | Name | Description |
| --- | --- | --- |
| <a href="#datasource_astra">datasource</a> | Astra | Connect to DataStax Astra Database service. |
| <a href="#datasource_cassandra">datasource</a> | Cassandra | Connect to Apache cassandra. |
| <a href="#datasource_jdbc">datasource</a> | JDBC | Connect to any JDBC compatible database. The driver must be provided as dependency |
| <a href="#hugging-face-configuration">hugging-face-configuration</a> | Hugging Face | Connect to Hugging Face service. |
| <a href="#open-ai-configuration">open-ai-configuration</a> | Open AI | Connect to OpenAI API or Azure OpenAI API. |
| <a href="#vector-database_astra">datasource</a> | Astra | Connect to DataStax Astra Database service. |
| <a href="#vector-database_cassandra">datasource</a> | Cassandra | Connect to Apache cassandra. |
| <a href="#vector-database_milvus">vector-database</a> | Milvus | Connect to Milvus/Zillis service. |
| <a href="#vector-database_pinecone">vector-database</a> | Pinecone | Connect to Pinecone service. |
| <a href="#vertex-configuration">vertex-configuration</a> | Vertex AI | Connect to VertexAI API. |


### <a name="datasource_astra"></a>Astra (`datasource`)

Connect to DataStax Astra Database service.

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `clientId` | Astra Token clientId to use. | string | ✓ |  |
| `database` | Astra Database name to connect to. If secureBundle is provided, this field is ignored. | string |  |  |
| `environment` | Astra environment. | string |  | PROD |
| `secret` | Astra Token secret to use. | string | ✓ |  |
| `secureBundle` | Secure bundle of the database. Must be encoded in base64. | string |  |  |
| `token` | Astra Token (AstraCS:xxx) for connecting to the database. If secureBundle is provided, this field is ignored. | string |  |  |
| `service` | Service type. Set to 'astra' | string | ✓ |  |


### <a name="datasource_cassandra"></a>Cassandra (`datasource`)

Connect to Apache cassandra.

| Key | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `contact-points` | Contact points of the cassandra cluster. | string | ✓ |  |
| `loadBalancing-localDc` | Load balancing local datacenter. | string | ✓ |  |
| `password` | User password. | string |  |  |
| `port` | Cassandra port. | integer | ✓ |  |
| `username` | User username. | string |  |  |
| `service` | Service type. Set to 'cassandra' | string | ✓ |  |

