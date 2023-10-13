<<<<<<< HEAD
# Assets

LangStream Version: **0.2.0**

\
=======
<h1>Assets</h1><p>LangStream Version: <strong>0.2.1-SNAPSHOT</strong></p>
>>>>>>> d816e58 (Agents API Ref: add vector database as single agents)


## Astra keyspace (`astra-keyspace`) <a href="#astra-keyspace" id="astra-keyspace"></a>

Manage a DataStax Astra keyspace.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>keyspace</code></td><td>Name of the keyspace to create.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Cassandra keyspace (`cassandra-keyspace`) <a href="#cassandra-keyspace" id="cassandra-keyspace"></a>

Manage a Cassandra keyspace.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the keyspace. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>delete-statements</code></td><td>List of the statement to execute to cleanup the keyspace. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>keyspace</code></td><td>Name of the keyspace to create.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Cassandra table (`cassandra-table`) <a href="#cassandra-table" id="cassandra-table"></a>

Manage a Cassandra table in existing keyspace.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the table. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>delete-statements</code></td><td>List of the statement to execute to cleanup the table. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>keyspace</code></td><td>Name of the keyspace where the table is located.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>table-name</code></td><td>Name of the table.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## JDBC table (`jdbc-table`) <a href="#jdbc-table" id="jdbc-table"></a>

Manage a JDBC table.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the table. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>delete-statements</code></td><td>List of the statement to execute to cleanup the table. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>table-name</code></td><td>Name of the table.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

\


## Milvus collection (`milvus-collection`) <a href="#milvus-collection" id="milvus-collection"></a>

Manage a Milvus collection.

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>collection-name</code></td><td>Name of the collection.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the collection. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>database-name</code></td><td>Name of the database where to create the collection.</td><td>string</td><td></td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>
<<<<<<< HEAD
=======

<br><h2 data-full-width="true"><a name="opensearch-index"></a>OpenSearch index (<code>opensearch-index</code>)</h2><p data-full-width="true">Manage OpenSearch index.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>index-name</code></td><td>Index name.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>mappings</code></td><td>JSON containing index mappings configuration.</td><td>string</td><td></td><td></td></tr><tr><td><code>settings</code></td><td>JSON containing index settings configuration.</td><td>string</td><td></td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="solr-collection"></a>Solr collection (<code>solr-collection</code>)</h2><p data-full-width="true">Manage a Solr collection.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the collection. They will be executed every time the application is deployed or upgraded.</td><td><a href="#solr-collection.create-statements">array of object</a></td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

<br><h3 data-full-width="true"><a name="solr-collection.create-statements"></a>Solr collection (<code>solr-collection</code>).create-statements</h3><table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>method</code></td><td></td><td>string</td><td></td><td></td></tr><tr><td><code>api</code></td><td></td><td>string</td><td></td><td></td></tr><tr><td><code>body</code></td><td></td><td>string</td><td></td><td></td></tr></tbody></table>



>>>>>>> d816e58 (Agents API Ref: add vector database as single agents)
