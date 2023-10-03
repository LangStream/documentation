# Resources

LangStream Version: **0.0.23**

| Type | Name | Description |
| --- | --- | --- |
| <a href="#datasource_astra">datasource</a> | Astra | Connect to DataStax Astra Database service. |
| <a href="#datasource_cassandra">datasource</a> | Cassandra | Connect to Apache cassandra. |
| <a href="#datasource_jdbc">datasource</a> | JDBC | Connect to any JDBC compatible database. The driver must be provided as dependency. All the extra configuration properties are passed as is to the JDBC driver. |
| <a href="#hugging-face-configuration">hugging-face-configuration</a> | Hugging Face | Connect to Hugging Face service. |
| <a href="#open-ai-configuration">open-ai-configuration</a> | Open AI | Connect to OpenAI API or Azure OpenAI API. |
| <a href="#vector-database_astra">datasource</a> | Astra | Connect to DataStax Astra Database service. |
| <a href="#vector-database_cassandra">datasource</a> | Cassandra | Connect to Apache cassandra. |
| <a href="#vector-database_milvus">vector-database</a> | Milvus | Connect to Milvus/Zillis service. |
| <a href="#vector-database_pinecone">vector-database</a> | Pinecone | Connect to Pinecone service. |
| <a href="#vertex-configuration">vertex-configuration</a> | Vertex AI | Connect to VertexAI API. |


### <a name="datasource_astra"></a>Astra (`datasource`)

Connect to DataStax Astra Database service.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `clientId` | Astra Token clientId to use. | string | ✓ |  |
| `database` | Astra Database name to connect to. If secureBundle is provided, this field is ignored. | string |  |  |
| `environment` | Astra environment. | string |  | PROD |
| `password` | DEPRECATED: use secret instead. | string |  |  |
| `secret` | Astra Token secret to use. | string | ✓ |  |
| `secureBundle` | Secure bundle of the database. Must be encoded in base64. | string |  |  |
| `service` | Service type. Set to 'astra' | string | ✓ |  |
| `token` | Astra Token (AstraCS:xxx) for connecting to the database. If secureBundle is provided, this field is ignored. | string |  |  |
| `username` | DEPRECATED: use clientId instead. | string |  |  |


### <a name="datasource_cassandra"></a>Cassandra (`datasource`)

Connect to Apache cassandra.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `contact-points` | Contact points of the cassandra cluster. | string | ✓ |  |
| `loadBalancing-localDc` | Load balancing local datacenter. | string | ✓ |  |
| `password` | User password. | string |  |  |
| `port` | Cassandra port. | integer |  | 9042 |
| `service` | Service type. Set to 'cassandra' | string | ✓ |  |
| `username` | User username. | string |  |  |


### <a name="datasource_jdbc"></a>JDBC (`datasource`)

Connect to any JDBC compatible database. The driver must be provided as dependency. All the extra configuration properties are passed as is to the JDBC driver.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `driverClass` | JDBC entry-point driver class. | string | ✓ |  |
| `service` | Service type. Set to 'jdbc' | string | ✓ |  |
| `url` | JDBC connection url. | string | ✓ |  |


### <a name="hugging-face-configuration"></a>Hugging Face (`hugging-face-configuration`)

Connect to Hugging Face service.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `access-key` | The access key to use for "api" provider. | string |  |  |
| `api-url` | The URL of the Hugging Face API. Relevant only if provider is "api". | string |  | https://api-inference.huggingface.co/pipeline/feature-extraction/ |
| `model-check-url` | The model url to use. Relevant only if provider is "api". | string |  | https://huggingface.co/api/models/ |
| `provider` | The provider to use. Either "local" or "api". | string |  | api |


### <a name="open-ai-configuration"></a>Open AI (`open-ai-configuration`)

Connect to OpenAI API or Azure OpenAI API.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `access-key` | The access key to use. | string | ✓ |  |
| `provider` | The provider to use. Either "openai" or "azure". | string |  | openai |
| `url` | Url for Azure OpenAI API. Required only if provider is "azure". | string |  |  |


### <a name="vector-database_astra"></a>Astra (`datasource`)

Connect to DataStax Astra Database service.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `clientId` | Astra Token clientId to use. | string | ✓ |  |
| `database` | Astra Database name to connect to. If secureBundle is provided, this field is ignored. | string |  |  |
| `environment` | Astra environment. | string |  | PROD |
| `password` | DEPRECATED: use secret instead. | string |  |  |
| `secret` | Astra Token secret to use. | string | ✓ |  |
| `secureBundle` | Secure bundle of the database. Must be encoded in base64. | string |  |  |
| `service` | Service type. Set to 'astra' | string | ✓ |  |
| `token` | Astra Token (AstraCS:xxx) for connecting to the database. If secureBundle is provided, this field is ignored. | string |  |  |
| `username` | DEPRECATED: use clientId instead. | string |  |  |


### <a name="vector-database_cassandra"></a>Cassandra (`datasource`)

Connect to Apache cassandra.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `contact-points` | Contact points of the cassandra cluster. | string | ✓ |  |
| `loadBalancing-localDc` | Load balancing local datacenter. | string | ✓ |  |
| `password` | User password. | string |  |  |
| `port` | Cassandra port. | integer |  | 9042 |
| `service` | Service type. Set to 'cassandra' | string | ✓ |  |
| `username` | User username. | string |  |  |


### <a name="vector-database_milvus"></a>Milvus (`vector-database`)

Connect to Milvus/Zillis service.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `host` | Host parameter for connecting to Milvus. | string |  |  |
| `index-name` | Url parameter for connecting to Zillis service. | string |  |  |
| `password` | Password parameter for connecting to Milvus. | string |  |  |
| `port` | Port parameter for connecting to Milvus. | integer |  | 19530 |
| `service` | Service type. Set to 'milvus' | string | ✓ |  |
| `token` | Token parameter for connecting to Zillis service. | string |  |  |
| `user` | User parameter for connecting to Milvus. | string |  | default |


### <a name="vector-database_pinecone"></a>Pinecone (`vector-database`)

Connect to Pinecone service.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `api-key` | Api key for connecting to the Pinecone service. | string | ✓ |  |
| `endpoint` | Endpoint of the Pinecone service. | string |  |  |
| `environment` | Environment parameter for connecting to the Pinecone service. | string | ✓ |  |
| `index-name` | Index name parameter for connecting to the Pinecone service. | string | ✓ |  |
| `project-name` | Project name parameter for connecting to the Pinecone service. | string | ✓ |  |
| `server-side-timeout-sec` | Server side timeout parameter for connecting to the Pinecone service. | integer |  | 10 |
| `service` | Service type. Set to 'pinecone' | string | ✓ |  |


### <a name="vertex-configuration"></a>Vertex AI (`vertex-configuration`)

Connect to VertexAI API.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `project` | GCP project name for the Vertex API. | string | ✓ |  |
| `region` | GCP region for the Vertex API. | string | ✓ |  |
| `serviceAccountJson` | Specify service account credentials. Refer to the GCP documentation on how to download it | string |  |  |
| `token` | Access key for the Vertex API. | string |  |  |
| `url` | URL connection for the Vertex API. | string | ✓ |  |


