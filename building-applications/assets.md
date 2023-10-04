# Assets

Assets are external resources handled by LangStream at deployment time. You don't want to deal with creating Kafka topics or vector database tables every time you change your application, so LangStream allows you to automate the behavior of assets at deployment, update, and deletion.

The LangStream deployer creates resources during the `app-setup` job. If the job completes, the deployer creates another job called `runtime-deployer` which creates the agent CRDs. When `runtime-deployer` completes successfully, the application status changes to DEPLOYED. (If you get the ERROR\_DEPLOYING status instead, check the logs with `langstream apps logs <my-app-id>).`

For example, when you initialize an Astra DB database, you might want to also create a keyspace and a table to save time. To do this, add the astra-keyspace and cassandra-table as assets to your pipeline.yaml:

```yaml
name: "Write to Astra DB"
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
assets:
  - name: "langstream-keyspace"
    asset-type: "astra-keyspace"
    creation-mode: create-if-not-exists
    config:
      keyspace: "langstream"
      datasource: "AstraDatasource"
  - name: "products-table"
    asset-type: "cassandra-table"
    creation-mode: create-if-not-exists
    config:
      table-name: "products"
      keyspace: "langstream"
      datasource: "AstraDatasource"
      create-statements:
        - "CREATE TABLE IF NOT EXISTS langstream.products (id int PRIMARY KEY,name TEXT,description TEXT);"
pipeline:
  - name: "Write to Astra"
    type: "vector-db-sink"
    input: "input-topic"
    configuration:
      datasource: "AstraDatasource"
      table-name: "products"
      keyspace: "langstream"
      mapping: "id=value.id,description=value.description,name=value.name"
      
```

Notice this pipeline is using `datasource` type `AstraDatasource`. The assets behavior described here is currently only available for [AstraDatasource](../configuration-resources/data-storage/astra.md) and [CassandraDataSource](../configuration-resources/data-storage/cassandra.md).

Other commands available for assets include creating indexes within your tables, and truncating tables, as below.

<pre class="language-yaml"><code class="lang-yaml"><strong>    config:
</strong>      table-name: "products"
      keyspace: "langstream"
      datasource: "AstraDatasource"
      create-statements:
        - "CREATE TABLE IF NOT EXISTS langstream.products (id int PRIMARY KEY,name TEXT,description TEXT, embeddings VECTOR&#x3C;FLOAT,1536>);"
        - "CREATE CUSTOM INDEX IF NOT EXISTS documents_ann_index ON documents.documents(embeddings) USING 'StorageAttachedIndex';"
      delete-statements:
        - "TRUNCATE TABLE langstream.products;"
</code></pre>

For more on how AstraDatasource, CassandraDataSource, and LangStream assets interact at application deployment, see [Data storage.](../configuration-resources/data-storage/)

### Configuration

| Asset Type         | Field             | Type   | Description                                                                                       |
| ------------------ | ----------------- | ------ | ------------------------------------------------------------------------------------------------- |
| cassandra-table    | table-name        | String | Name of the table.                                                                                |
|                    | keyspace          | String | Name of the keyspace.                                                                             |
|                    | create-statements | List   | List of statements to create the table.                                                           |
|                    | delete-statements | List   | List of statements to delete the table. Required only if `deletion-mode` is set to `"delete"`.    |
| cassandra-keyspace | keyspace          | String | Name of the keyspace.                                                                             |
|                    | create-statements | List   | List of statements to create the keyspace.                                                        |
|                    | delete-statements | List   | List of statements to delete the keyspace. Required only if `deletion-mode` is set to `"delete"`. |
|                    | secureBundle      | N/A    | If present, an exception is thrown indicating that `"astra-keyspace"` should be used.             |
|                    | database          | N/A    | If present, an exception is thrown indicating that `"astra-keyspace"` should be used.             |
| astra-keyspace     | keyspace          | String | Name of the keyspace.                                                                             |
|                    | token             | String | Token for accessing AstraDB.                                                                      |
|                    | database          | String | Name of the database in AstraDB.                                                                  |
| All Asset Types    | datasource        | Map    | Nested configuration containing a `configuration` field with datasource-specific configurations.  |

