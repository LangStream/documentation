# DataSources and Vector Databases

A data source resource used to interact with a database.

You define datasources in the configuration.yaml file.

This is for a Vector Database datasource:

```yaml
resources:
  - type: "vector-database"
    name: "NameOfTheDatasource"
    configuration:
      service: "SERVICE-TYPE"
      ...  other parameters depending on the service type
      
```

This is for a generic datasource:

```yaml
resources:
  - type: "datasource"
    name: "NameOfTheDatasource"
    configuration:
      service: "SERVICE-TYPE"
      ...  other parameters depending on the service type
      
```

### Supported services

- [Datastax Astra DB](astra.md)
- [Apache Cassandra](cassandra.md)
- [Pinecone](pinecone.md)
- [JDBC](jdbc.md)

