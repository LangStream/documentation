### Connecting to a JDBC Compliant Database

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
        user: "{{secrets.postgres.user}}"
        password: "{{secrets.postgres.password}}"
  dependencies:
    - name: "PostGRES JDBC Driver"
      url: "https://jdbc.postgresql.org/download/postgresql-42.6.0.jar"
      sha512sum: "ec3b57d8377715ef6286d457b610a2e056aa99dbf036f750c5e07370fc8b01414b2aef5e0232d561c50f22abf0da961ee432e53734cc193a3e9bdaf6231d4fa1"
      type: "java-library"
      
```

The `driverClass` class parameter is required - it is the entry point for bootstrapping the JDBC driver.

## Loading the JDBC driver

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

### Querying a JDBC datasource

You can query a JDBC datasource using the "query" or the "query-vector-db" agent in your pipeline.

```yaml
pipeline:
  - name: "Execute Query"
    type: "query-vector-db"
    input: "input-topic"
    output: "output-topic"    
    configuration:
      datasource: "PGDataSource"
      query: "SELECT * FROM products WHERE id = ?"
      fields:
        - "value.id"
      output-field: "value.query-result"
```

As usual you can use the '?' symbol as a placeholder for the fields that you specify in the "query" section.