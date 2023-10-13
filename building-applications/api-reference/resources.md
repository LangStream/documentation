<<<<<<< HEAD
# Resources

LangStream Version: **0.2.0**

\
=======
<h1>Resources</h1><p>LangStream Version: <strong>0.2.1-SNAPSHOT</strong></p>
>>>>>>> d816e58 (Agents API Ref: add vector database as single agents)


## Astra (`datasource`) <a href="#datasource_astra" id="datasource_astra"></a>

Connect to DataStax Astra Database service.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>clientId</code></td><td>Astra Token clientId to use.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>database</code></td><td>Astra Database name to connect to. If secureBundle is provided, this field is ignored.</td><td>string</td><td></td><td></td></tr><tr><td><code>environment</code></td><td>Astra environment.</td><td>string</td><td></td><td>PROD</td></tr><tr><td><code>password</code></td><td>DEPRECATED: use secret instead.</td><td>string</td><td></td><td></td></tr><tr><td><code>secret</code></td><td>Astra Token secret to use.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>secureBundle</code></td><td>Secure bundle of the database. Must be encoded in base64.</td><td>string</td><td></td><td></td></tr><tr><td><code>service</code></td><td>Service type. Set to 'astra'</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>token</code></td><td>Astra Token (AstraCS:xxx) for connecting to the database. If secureBundle is provided, this field is ignored.</td><td>string</td><td></td><td></td></tr><tr><td><code>username</code></td><td>DEPRECATED: use clientId instead.</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Cassandra (`datasource`) <a href="#datasource_cassandra" id="datasource_cassandra"></a>

Connect to Apache cassandra.

<<<<<<< HEAD
<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>contact-points</code></td><td>Contact points of the cassandra cluster.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>loadBalancing-localDc</code></td><td>Load balancing local datacenter.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>password</code></td><td>User password.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Cassandra port.</td><td>integer</td><td></td><td>9042</td></tr><tr><td><code>service</code></td><td>Service type. Set to 'cassandra'</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>username</code></td><td>User username.</td><td>string</td><td></td><td></td></tr></tbody></table>
=======
<br><h2 data-full-width="true"><a name="datasource_opensearch"></a>OpenSearch (<code>datasource</code>)</h2><p data-full-width="true">Connect to OpenSearch service or AWS OpenSearch Service/Serverless.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>host</code></td><td>Host parameter for connecting to OpenSearch.<br>Valid both for OpenSearch and AWS OpenSearch Service/Serverless.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>https</code></td><td>Whether to use https or not.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>password</code></td><td>Basic authentication for connecting to OpenSearch.<br>In case of AWS OpenSearch Service/Serverless, this is the secret key.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Port parameter for connecting to OpenSearch service.</td><td>integer</td><td></td><td>9200</td></tr><tr><td><code>region</code></td><td>Region parameter for connecting to AWS OpenSearch Service/Serveless.</td><td>string</td><td></td><td></td></tr><tr><td><code>service</code></td><td>Service type. Set to &#x27;opensearch&#x27;</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>username</code></td><td>Basic authentication for connecting to OpenSearch.<br>In case of AWS OpenSearch Service/Serverless, this is the access key.</td><td>string</td><td></td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="hugging-face-configuration"></a>Hugging Face (<code>hugging-face-configuration</code>)</h2><p data-full-width="true">Connect to Hugging Face service.</p>
>>>>>>> d816e58 (Agents API Ref: add vector database as single agents)

\


## JDBC (`datasource`) <a href="#datasource_jdbc" id="datasource_jdbc"></a>

Connect to any JDBC compatible database. The driver must be provided as dependency. All the extra configuration properties are passed as is to the JDBC driver.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>driverClass</code></td><td>JDBC entry-point driver class.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>service</code></td><td>Service type. Set to 'jdbc'</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>url</code></td><td>JDBC connection url.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Hugging Face (`hugging-face-configuration`) <a href="#hugging-face-configuration" id="hugging-face-configuration"></a>

<<<<<<< HEAD
Connect to Hugging Face service.
=======
<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>host</code></td><td>Host parameter for connecting to Milvus.</td><td>string</td><td></td><td></td></tr><tr><td><code>password</code></td><td>Password parameter for connecting to Milvus.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Port parameter for connecting to Milvus.</td><td>integer</td><td></td><td>19530</td></tr><tr><td><code>service</code></td><td>Service type. Set to &#x27;milvus&#x27;</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>token</code></td><td>Token parameter for connecting to Zillis service.</td><td>string</td><td></td><td></td></tr><tr><td><code>url</code></td><td>Url parameter for connecting to Zillis service.</td><td>string</td><td></td><td></td></tr><tr><td><code>user</code></td><td>User parameter for connecting to Milvus.</td><td>string</td><td></td><td>default</td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="vector-database_opensearch"></a>OpenSearch (<code>vector-database</code>)</h2><p data-full-width="true">Connect to OpenSearch service or AWS OpenSearch Service/Serverless.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>host</code></td><td>Host parameter for connecting to OpenSearch.<br>Valid both for OpenSearch and AWS OpenSearch Service/Serverless.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>https</code></td><td>Whether to use https or not.</td><td>boolean</td><td></td><td>true</td></tr><tr><td><code>password</code></td><td>Basic authentication for connecting to OpenSearch.<br>In case of AWS OpenSearch Service/Serverless, this is the secret key.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Port parameter for connecting to OpenSearch service.</td><td>integer</td><td></td><td>9200</td></tr><tr><td><code>region</code></td><td>Region parameter for connecting to AWS OpenSearch Service/Serveless.</td><td>string</td><td></td><td></td></tr><tr><td><code>service</code></td><td>Service type. Set to &#x27;opensearch&#x27;</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>username</code></td><td>Basic authentication for connecting to OpenSearch.<br>In case of AWS OpenSearch Service/Serverless, this is the access key.</td><td>string</td><td></td><td></td></tr></tbody></table>
>>>>>>> d816e58 (Agents API Ref: add vector database as single agents)

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>access-key</code></td><td>The access key to use for "api" provider.</td><td>string</td><td></td><td></td></tr><tr><td><code>api-url</code></td><td>The URL of the Hugging Face API. Relevant only if provider is "api".</td><td>string</td><td></td><td>https://api-inference.huggingface.co/pipeline/feature-extraction/</td></tr><tr><td><code>model-check-url</code></td><td>The model url to use. Relevant only if provider is "api".</td><td>string</td><td></td><td>https://huggingface.co/api/models/</td></tr><tr><td><code>provider</code></td><td>The provider to use. Either "local" or "api".</td><td>string</td><td></td><td>api</td></tr></tbody></table>

\

<<<<<<< HEAD

## Open AI (`open-ai-configuration`) <a href="#open-ai-configuration" id="open-ai-configuration"></a>

Connect to OpenAI API or Azure OpenAI API.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>access-key</code></td><td>The access key to use.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>provider</code></td><td>The provider to use. Either "openai" or "azure".</td><td>string</td><td></td><td>openai</td></tr><tr><td><code>url</code></td><td>Url for Azure OpenAI API. Required only if provider is "azure".</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Astra (`vector-database`) <a href="#vector-database_astra" id="vector-database_astra"></a>

Connect to DataStax Astra Database service.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>clientId</code></td><td>Astra Token clientId to use.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>database</code></td><td>Astra Database name to connect to. If secureBundle is provided, this field is ignored.</td><td>string</td><td></td><td></td></tr><tr><td><code>environment</code></td><td>Astra environment.</td><td>string</td><td></td><td>PROD</td></tr><tr><td><code>password</code></td><td>DEPRECATED: use secret instead.</td><td>string</td><td></td><td></td></tr><tr><td><code>secret</code></td><td>Astra Token secret to use.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>secureBundle</code></td><td>Secure bundle of the database. Must be encoded in base64.</td><td>string</td><td></td><td></td></tr><tr><td><code>service</code></td><td>Service type. Set to 'astra'</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>token</code></td><td>Astra Token (AstraCS:xxx) for connecting to the database. If secureBundle is provided, this field is ignored.</td><td>string</td><td></td><td></td></tr><tr><td><code>username</code></td><td>DEPRECATED: use clientId instead.</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Cassandra (`vector-database`) <a href="#vector-database_cassandra" id="vector-database_cassandra"></a>

Connect to Apache cassandra.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>contact-points</code></td><td>Contact points of the cassandra cluster.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>loadBalancing-localDc</code></td><td>Load balancing local datacenter.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>password</code></td><td>User password.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Cassandra port.</td><td>integer</td><td></td><td>9042</td></tr><tr><td><code>service</code></td><td>Service type. Set to 'cassandra'</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>username</code></td><td>User username.</td><td>string</td><td></td><td></td></tr></tbody></table>

\


## Milvus (`vector-database`) <a href="#vector-database_milvus" id="vector-database_milvus"></a>

Connect to Milvus/Zillis service.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>host</code></td><td>Host parameter for connecting to Milvus.</td><td>string</td><td></td><td></td></tr><tr><td><code>index-name</code></td><td>Url parameter for connecting to Zillis service.</td><td>string</td><td></td><td></td></tr><tr><td><code>password</code></td><td>Password parameter for connecting to Milvus.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Port parameter for connecting to Milvus.</td><td>integer</td><td></td><td>19530</td></tr><tr><td><code>service</code></td><td>Service type. Set to 'milvus'</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>token</code></td><td>Token parameter for connecting to Zillis service.</td><td>string</td><td></td><td></td></tr><tr><td><code>user</code></td><td>User parameter for connecting to Milvus.</td><td>string</td><td></td><td>default</td></tr></tbody></table>

\


## Pinecone (`vector-database`) <a href="#vector-database_pinecone" id="vector-database_pinecone"></a>

Connect to Pinecone service.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>api-key</code></td><td>Api key for connecting to the Pinecone service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>endpoint</code></td><td>Endpoint of the Pinecone service.</td><td>string</td><td></td><td></td></tr><tr><td><code>environment</code></td><td>Environment parameter for connecting to the Pinecone service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>index-name</code></td><td>Index name parameter for connecting to the Pinecone service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>project-name</code></td><td>Project name parameter for connecting to the Pinecone service.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>server-side-timeout-sec</code></td><td>Server side timeout parameter for connecting to the Pinecone service.</td><td>integer</td><td></td><td>10</td></tr><tr><td><code>service</code></td><td>Service type. Set to 'pinecone'</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Vertex AI (`vertex-configuration`) <a href="#vertex-configuration" id="vertex-configuration"></a>

Connect to VertexAI API.
=======
<br><h2 data-full-width="true"><a name="vector-database_solr"></a>Solr (<code>vector-database</code>)</h2><p data-full-width="true">Connect to Solr or Solr Cloud service.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>collection-name</code></td><td>Collection to use in Solr.</td><td>string</td><td></td><td></td></tr><tr><td><code>host</code></td><td>Host parameter for connecting to Solr.</td><td>string</td><td></td><td></td></tr><tr><td><code>password</code></td><td>Password parameter for connecting to Solr.</td><td>string</td><td></td><td></td></tr><tr><td><code>port</code></td><td>Port parameter for connecting to Solr.</td><td>integer</td><td></td><td>8983</td></tr><tr><td><code>service</code></td><td>Service type. Set to &#x27;solr&#x27;</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>user</code></td><td>Username parameter for connecting to Solr.</td><td>string</td><td></td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="vertex-configuration"></a>Vertex AI (<code>vertex-configuration</code>)</h2><p data-full-width="true">Connect to VertexAI API.</p>
>>>>>>> d816e58 (Agents API Ref: add vector database as single agents)

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>project</code></td><td>GCP project name for the Vertex API.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>region</code></td><td>GCP region for the Vertex API.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>serviceAccountJson</code></td><td>Specify service account credentials. Refer to the GCP documentation on how to download it</td><td>string</td><td></td><td></td></tr><tr><td><code>token</code></td><td>Access key for the Vertex API.</td><td>string</td><td></td><td></td></tr><tr><td><code>url</code></td><td>URL connection for the Vertex API.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>
