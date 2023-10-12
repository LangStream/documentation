<h1>Assets</h1><p>LangStream Version: <strong>0.2.0</strong></p>



<br><h2 data-full-width="true"><a name="astra-keyspace"></a>Astra keyspace (<code>astra-keyspace</code>)</h2><p data-full-width="true">Manage a DataStax Astra keyspace.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>keyspace</code></td><td>Name of the keyspace to create.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="cassandra-keyspace"></a>Cassandra keyspace (<code>cassandra-keyspace</code>)</h2><p data-full-width="true">Manage a Cassandra keyspace.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the keyspace. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>delete-statements</code></td><td>List of the statement to execute to cleanup the keyspace. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>keyspace</code></td><td>Name of the keyspace to create.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="cassandra-table"></a>Cassandra table (<code>cassandra-table</code>)</h2><p data-full-width="true">Manage a Cassandra table in existing keyspace.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the table. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>delete-statements</code></td><td>List of the statement to execute to cleanup the table. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>keyspace</code></td><td>Name of the keyspace where the table is located.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>table-name</code></td><td>Name of the table.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="jdbc-table"></a>JDBC table (<code>jdbc-table</code>)</h2><p data-full-width="true">Manage a JDBC table.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the table. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>delete-statements</code></td><td>List of the statement to execute to cleanup the table. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'.</td><td>array of string</td><td></td><td></td></tr><tr><td><code>table-name</code></td><td>Name of the table.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>

<br><h2 data-full-width="true"><a name="milvus-collection"></a>Milvus collection (<code>milvus-collection</code>)</h2><p data-full-width="true">Manage a Milvus collection.</p>

<table data-full-width="true"><thead><tr><th></th><th>Description</th><th>Type</th><th>Required</th><th>Default Value</th></tr></thead><tbody><tr><td><code>collection-name</code></td><td>Name of the collection.</td><td>string</td><td>✓</td><td></td></tr><tr><td><code>create-statements</code></td><td>List of the statement to execute to create the collection. They will be executed every time the application is deployed or upgraded.</td><td>array of string</td><td>✓</td><td></td></tr><tr><td><code>database-name</code></td><td>Name of the database where to create the collection.</td><td>string</td><td></td><td></td></tr><tr><td><code>datasource</code></td><td>Reference to a datasource id configured in the application.</td><td>string</td><td>✓</td><td></td></tr></tbody></table>



