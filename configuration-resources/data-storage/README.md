# DataSources and Vector Databases

A `datasource` resource used to interact with a database.

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

- [Datastax Astra DB](./astra.md)
- [Apache Cassandra](./cassandra.md)
- [Pinecone](./pinecone.md)
- [Milvus](./milvus.md)
- [JDBC](./jdbc.md)
- [Solr](./solr.md)
- [OpenSearch](./opensearch.md)


### Supporting a new service

If your favourite database is not supported, you can add support for it by creating a new plugin.
Feel free to open an issue on [GitHub](https://github.com/LangStream/langstream/issues) to ask for help or file a feature request.
