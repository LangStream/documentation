### Connecting to DataStax Astra DB

To use DataStax Astra DB as a vector database, you have to create a "vector-database" resource in your configuration.yaml file.

If you want to use the JSON based API then you have to create a "astra-vector-db" resource. See the documentation [here](./astra-vector-db.md).


```yaml
resources:
  - type: "vector-database"
    name: "AstraDatasource"
    configuration:
      service: "astra"
      clientId: "${ secrets.astra.clientId }"
      secret: "${ secrets.astra.secret }"
      secureBundle: "${ secrets.astra.secureBundle }"
      database: "${ secrets.astra.database }"
      token: "${ secrets.astra.token }"
      environment: "${ secrets.astra.environment }"
```

Required parameters:
- clientId: this is the clientId provided by the Astra DB service
- secret: this is the secret provided by the Astra DB service
- token: this is the token provided by the Astra DB service
- database: this is the database name provided by the Astra DB service

Optional parameters:
- secureBundle: this is the secure bundle provided by the Astra DB service
- environment: this is the environment provided by the Astra DB service, it can be PROD, STAGING or DEV, depending on the environment you are using (default is PROD, the other values are useful only for Astra developers)


### Handling the secure bundle zip file

The secure bundle is a file that contains some TLS certificates and endpoint information to connect to the Astra DB service.

This is an optional parameter, as LangStream is able to download it for you when you provide the token and database parameters.

It must be a base64-encoded string like this:

```yaml
   secureBundle: "base64:AAAAA2131232133123122313...."
```

But you can also provide the secure bundle as a file, in this case you have to use the following syntax:

```yaml
   secureBundle: "<file:secure-bundle.zip>"
```

With this syntax the LangStream CLI will read the file and encode it in base64 for you. The path name is relative to the file that mentions this value.
This syntax works only if used in a secrets.yaml file or an instance.yaml file. It doesn't work directly in a configuration.yaml file, because
it is not recommended to store secrets in a configuration file, but only references to secrets (`${secrets.xxx}`) and to global variables (`${globals.xxx}`).



### Special assets for Astra

For "Vector Database" resources based on Astra, you can use special `assets`in your pipeline file: "astra-keyspace" and "cassandra-table".

```yaml
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
    deletion-mode: delete
    config:
      table-name: "products"
      keyspace: "langstream"
      datasource: "AstraDatasource"
      create-statements:
        - "CREATE TABLE IF NOT EXISTS langstream.products (id int PRIMARY KEY,name TEXT,description TEXT, embeddings VECTOR<FLOAT,1536>);"
        - "CREATE CUSTOM INDEX IF NOT EXISTS documents_ann_index ON documents.documents(embeddings) USING 'StorageAttachedIndex';"
      delete-statements:
        - "TRUNCATE TABLE langstream.products;"
```

With the "astra-keyspace" asset, you can create a keyspace in your Astra DB instance. The keyspace is a logical container for tables. It is similar to a database in a relational database.

With the "cassandra-table" asset you can create a table in your Astra DB instance. The table is a collection of rows that share a schema of columns. It is similar to a table in a relational database.


### Reading and writing to Astra

Astra is compatible with Cassandra, so you can use the same agents you use for Cassandra to read and write to Astra. See the documentation [here](./cassandra.md).

### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#datasource_astra).