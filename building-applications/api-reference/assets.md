# Assets

LangStream Version: **0.1.0**





### <a name="astra-keyspace"></a>Astra keyspace (`astra-keyspace`)

Manage a DataStax Astra keyspace.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |
| `keyspace` | Name of the keyspace to create. | string | ✓ |  |


### <a name="cassandra-keyspace"></a>Cassandra keyspace (`cassandra-keyspace`)

Manage a Cassandra keyspace.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `create-statements` | List of the statement to execute to create the keyspace. They will be executed every time the application is deployed or upgraded. | array of string | ✓ |  |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |
| `delete-statements` | List of the statement to execute to cleanup the keyspace. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'. | array of string |  |  |
| `keyspace` | Name of the keyspace to create. | string | ✓ |  |


### <a name="cassandra-table"></a>Cassandra table (`cassandra-table`)

Manage a Cassandra table in existing keyspace.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `create-statements` | List of the statement to execute to create the table. They will be executed every time the application is deployed or upgraded. | array of string | ✓ |  |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |
| `delete-statements` | List of the statement to execute to cleanup the table. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'. | array of string |  |  |
| `keyspace` | Name of the keyspace where the table is located. | string | ✓ |  |
| `table-name` | Name of the table. | string | ✓ |  |


### <a name="jdbc-table"></a>JDBC table (`jdbc-table`)

Manage a JDBC table.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `create-statements` | List of the statement to execute to create the table. They will be executed every time the application is deployed or upgraded. | array of string | ✓ |  |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |
| `delete-statements` | List of the statement to execute to cleanup the table. They will be executed when the application is deleted only if 'deletion-mode' is 'delete'. | array of string |  |  |
| `table-name` | Name of the table. | string | ✓ |  |


### <a name="milvus-collection"></a>Milvus collection (`milvus-collection`)

Manage a Milvus collection.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `collection-name` | Name of the collection. | string | ✓ |  |
| `create-statements` | List of the statement to execute to create the collection. They will be executed every time the application is deployed or upgraded. | array of string | ✓ |  |
| `database-name` | Name of the database where to create the collection. | string |  |  |
| `datasource` | Reference to a datasource id configured in the application. | string | ✓ |  |


