### Connecting to DataStax Astra DB

In order to use DataStax Astra DB as a vector database you have to create a "vector-database" resource in your configuration.yaml file.

```yaml
resources:
  - type: "vector-database"
    name: "AstraDatasource"
    configuration:
      service: "astra"
      clientId: "{{{ secrets.astra.clientId }}}"
      secret: "{{{ secrets.astra.secret }}}"
      secureBundle: "{{{ secrets.astra.secureBundle }}}"
      database: "{{{ secrets.astra.database }}}"
      token: "{{{ secrets.astra.token }}}"
      environment: "{{{ secrets.astra.environment }}}"
```

You are required to provide the following parameters:
- clientId: this is the clientId provided by the Astra DB service
- secret: this is the secret provided by the Astra DB service
- token: this is the token provided by the Astra DB service
- database: this is the database name provided by the Astra DB service

Optional parameters:
- secureBundle: this is the secure bundle provided by the Astra DB service
- environment: this is the environment provided by the Astra DB service, it can be PROD, STAGING or DEV, depending on the environment you are using (default is PROD, the other values are useful only for Astra developers)


## Handling the secure bundle zip file

The secure bundle is a file that contains some TLS certificates and endpoint information to connect to the Astra DB service.

This is an optional parameter, as LangStream is able to download it for you when you provide the token and database parameters.

It must be a base64 encoded string like this:

```yaml
   secureBundle: "base64:AAAAA2131232133123122313...."
```

But you can also provide the secure bundle as a file, in this case you have to use the following syntax:

```yaml
   secureBundle: "<file:secure-bundle.zip>"
```

With this syntax the LangStream CLI will read the file and encode it in base64 for you. The path name is relative to the file that mentions this value.
This syntax works only if used in a secrets.yaml file or an instance.yaml file. It doesn't work directly in a configuration.yaml file, this is because
it is not expected to store directly secrets in a configuration file, but only references to secrets (`{{{secrets.xxx}}}`) and to global variables (`{{{globals.xxx}}}`).



## Special assets for Astra

For a "Vector Database" resources based on Astra you can use the following special assets: "astra-keyspace" and "cassandra-table".

```yaml
assets:
  - name: "lagstream-keyspace"
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
        # optional, let's delete the records, but not the table
        - "TRUNCATE TABLE langstream.products;"
```

With the "astra-keyspace" asset you can create a keyspace in your Astra DB instance. The keyspace is a logical container for tables. It is similar to a database in a relational database.

With the "cassandra-table" asset you can create a table in your Astra DB instance. The table is a collection of rows that share a schema of columns. It is similar to a table in a relational database.

