### Connecting to Apache Cassandra

To use Apache Cassandra as a vector database, create a "vector-database" (or "datasource") resource in your configuration.yaml file.

Support for Vector Search is available since Cassandra 5.0, so you need to use a version of Cassandra >= 5.0 or equivalent.

```yaml
resources:
  - type: "vector-database"
    name: "CassandraDataSource"
    configuration:
      service: "cassandra"
      username: "{{{ secrets.cassandra.username }}}"
      password: "{{{ secrets.cassandra.password }}}"
      port: "{{{ secrets.cassandra.port }}}"
      contact-points: "{{{ secrets.cassandra.contact-points }}}"
      loadBalancing-localDc: "{{{ secrets.cassandra.loadBalancing-localDc }}}"
      
```

Required parameters:
- contact-points: the address to connect to Cassandra
- loadBalancing-localDc: the datacenter to connect to

Optional parameters:
- port: the port to connect to Cassandra (default is 9042)
- username: the username
- password: the password


## Special assets for Cassandra

For "Vector Database" resources based on Astra, you can use special `assets` in your pipeline: "cassandra-keyspace" and "cassandra-table".

```yaml
assets:
  - name: "langstream-keyspace"
    asset-type: "cassandra-keyspace"
    creation-mode: create-if-not-exists    
    config:
      keyspace: "langstream"
      datasource: "CassandraDataSource"
      create-statements:
        - "CREATE KEYSPACE vsearch WITH REPLICATION = {'class' : 'SimpleStrategy','replication_factor' : 1};"
      delete-statements:
        - "DROP KEYSPACE IF EXISTS vsearch;"
  - name: "products-table"
    asset-type: "cassandra-table"
    creation-mode: create-if-not-exists
    deletion-mode: delete
    config:
      table-name: "products"
      keyspace: "langstream"
      datasource: "CassandraDataSource"
      create-statements:
        - "CREATE TABLE IF NOT EXISTS langstream.products (id int PRIMARY KEY,name TEXT,description TEXT, embeddings VECTOR<FLOAT,1536>);"
        - "CREATE CUSTOM INDEX IF NOT EXISTS documents_ann_index ON documents.documents(embeddings) USING 'StorageAttachedIndex';"
      delete-statements:
        - "TRUNCATE TABLE langstream.products;"
```

With the "cassandra-keyspace" asset you can create a keyspace in your Cassandra cluster. The keyspace is a logical container for tables. It is similar to a database in a relational database.

With the "cassandra-table" asset you can create a table in your Astra DB instance. The table is a collection of rows that share a schema of columns. It is similar to a table in a relational database.

