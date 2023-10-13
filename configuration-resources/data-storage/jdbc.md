# JDBC

#### Connecting to a JDBC Compliant Database

Connect to any JDBC-compliant database using the "datasource" resource type.

```yaml
configuration:
  resources:
    - type: "datasource"
      name: "PGDataSource"
      configuration:
        service: "jdbc"
        driverClass: "org.postgresql.Driver"
        url: "jdbc:postgresql://postgresql.default.svc.cluster.local:5432/"
        user: "${secrets.postgres.user}"
        password: "${secrets.postgres.password}"
  resources:
    - type: "datasource"
      name: "JdbcDatasource"
      configuration:
        service: "jdbc"
        driverClass: "herddb.jdbc.Driver"
        url: "jdbc:herddb:server:localhost:7000"
  dependencies:
    - name: "PostGRES JDBC Driver"
      url: "https://jdbc.postgresql.org/download/postgresql-42.6.0.jar"
      sha512sum: "ec3b57d8377715ef6286d457b610a2e056aa99dbf036f750c5e07370fc8b01414b2aef5e0232d561c50f22abf0da961ee432e53734cc193a3e9bdaf6231d4fa1"
      type: "java-library"
  dependencies:
    - name: "HerdDB.org JDBC Driver"
      url: "https://repo1.maven.org/maven2/org/herddb/herddb-jdbc/0.28.0/herddb-jdbc-0.28.0-thin.jar"
      sha512sum: "d8ea8fbb12eada8f860ed660cbc63d66659ab3506bc165c85c420889aa8a1dac53dab7906ef61c4415a038c5a034f0d75900543dd0013bdae50feafd46f51c8e"
      type: "java-library"
```

The `driverClass` class parameter is required - it is the entry point for bootstrapping the JDBC driver.

### Loading the JDBC driver

To load the JDBC driver, provide a dependency to the driver jar file.

```yaml
  dependencies:
    - name: "PostGRES JDBC Driver"
      url: "https://jdbc.postgresql.org/download/postgresql-42.6.0.jar"
      sha512sum: "ec3b57d8377715ef6286d457b610a2e056aa99dbf036f750c5e07370fc8b01414b2aef5e0232d561c50f22abf0da961ee432e53734cc193a3e9bdaf6231d4fa1"
      type: "java-library"
```

With this syntax, the LangStream CLI downloads the file and stores it in the `java/lib` folder.

Add a .gitignore rule to avoid committing the jar file to your git repository.

This is a sample .gitignore file to put at the root of your application directory in order to not commit the jar file to your git repository:

```gitignore
java/lib/*
```

#### Querying a JDBC datasource

You can query a JDBC datasource using the "query" or the "query-vector-db" agent in your pipeline.

```yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "JdbcDatasource"
      query: "SELECT text FROM documents ORDER BY cosine_similarity(embeddings_vector, CAST(? as FLOAT ARRAY)) DESC LIMIT 5"
      fields:
        - "value.question_embeddings"
```

As usual you can use the '?' symbol as a placeholder for the fields that you specify in the "query" section. The syntax for performing an Approximate Nearest Neighbor search is specific to the database you are using, in the example above we are using the HerdDB syntax.

### Special assets for JDBC datasources

You can automatically manage the tables on your JDBC datasource using the "jdbc-table" asset type.

```yaml
assets:
  - name: "documents-table"
    asset-type: "jdbc-table"
    creation-mode: create-if-not-exists
    deletion-mode: delete
    config:
      table-name: "documents"    
      datasource: "JdbcDatasource"
      create-statements:
        - |
          CREATE TABLE documents (
          filename TEXT,
          chunk_id int,
          num_tokens int,
          lang TEXT,
          text TEXT,
          embeddings_vector FLOATA,
          PRIMARY KEY (filename, chunk_id));
      delete-statements:
        - "DROP TABLE IF EXISTS documents"
```

You can specify any number of statements in the "create-statements" and in the "delete-statements" sections, for instance to create indexes or other objects.

#### Writing to a JDBC datasource

Use the "vector-db-sink" agent with the following parameters to write to a JDBC database:

```yaml
  - name: "Write"
    type: "vector-db-sink"
    input: chunks-topic
    configuration:
      datasource: "JdbcDatasource"
      table-name: "documents"
      fields:
        - name: "filename"
          expression: "value.filename"
          primary-key: true
        - name: "chunk_id"
          expression: "value.chunk_id"
          primary-key: true
        - name: "embeddings_vector"
          expression: "fn:toListOfFloat(value.embeddings_vector)"
        - name: "lang"
          expression: "value.language"
        - name: "text"
          expression: "value.text"
        - name: "num_tokens"
          expression: "value.chunk_num_tokens"
```

Set the table-name to the name of the table you want to write to. Define the fields in the "fields" list. This works similarly to the ['compute' agent](broken-reference), and you can use the same syntax to define the fields. It is important that you tag the fields that are part of the primary key of the table with "primary-key: true". This is needed to correctly manage upserts and deletion from the table.
