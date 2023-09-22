### Connecting to a JDBC Compliant Database

You can connect to any JDBC compliant database using the "datasource" resource type.

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

You are required to provide the `driverClass` class parameter, that is the entry point for bootstrapping the JDBC driver.

## Loading the JDBC driver

In order to load the JDBC driver you have to provide a dependency to the driver jar file.

```yaml
  dependencies:
    - name: "PostGRES JDBC Driver"
      url: "https://jdbc.postgresql.org/download/postgresql-42.6.0.jar"
      sha512sum: "ec3b57d8377715ef6286d457b610a2e056aa99dbf036f750c5e07370fc8b01414b2aef5e0232d561c50f22abf0da961ee432e53734cc193a3e9bdaf6231d4fa1"
      type: "java-library"
```   

With this syntax it is the LangStream CLI that downloads the file and stores it in the `java/lib` folder.

You should add a .gitignore rule to avoid committing the jar file to your git repository.

This is a sample .gitignore file to put at the root of your application directory in order to not commit the jar file to your git repository:


```gitignore
java/lib/*
```

