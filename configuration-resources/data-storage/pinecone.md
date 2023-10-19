### Connecting to Pinecone.io

To use Pinecone.io as a vector database, create a "vector-database" resource in your configuration.yaml file.

```yaml
resources:
    - type: "vector-database"
      name: "PineconeDatasource"
      configuration:
        service: "pinecone"
        api-key: "${secrets.pinecone.api-key}"
        environment: "${secrets.pinecone.environment}"
        index-name: "${secrets.pinecone.index-name}"
        project-name: "${secrets.pinecone.project-name}"
        server-side-timeout-sec: 10
      
```

Required parameters:
- api-key: your Pinecone API key
- index-name: the name of the index
- project-name: the name of the project
- environment: the environment

You can find the api-key, index-name, project-name and enviroment in the Pinecone.io console.

Optional parameters:
- server-side-timeout-sec: the timeout for any server-side operation (default is 10 seconds)


### Querying Pinecone

You can query Pinecone using the "vector-db-query" agent in your pipeline.

```yaml
pipeline:
  - name: "Execute Query"
    type: "query-vector-db"
    configuration:
      datasource: "PineconeDatasource"
      query: |
        {
              "vector": ?,
              "topK": 5,
              "filter":
                {"$or": [{"genre": "comedy"}, {"year":2019}]}
         }
      fields:
        - "value.embeddings"
      output-field: "value.query-result"
```

To perform the query, define the JSON for the request to the Pinecone API.
As usual you can use the '?' symbol as a placeholder for the fields that you specify in the "query" section.


### Writing to Pinecone

You can write to Pinecone using the "vector-db-sink" agent in your pipeline.

```yaml
pipeline:
  - name: "Write to Pinecone"
    type: "vector-db-sink"
    configuration:
      datasource: "PineconeDatasource"
      vector.id: "value.id"
      vector.vector: "value.embeddings"
      vector.namespace: ""
      vector.metadata.genre: "value.genre"
```

To write to Pinecone, define the values for the vector.id, vector.vector and vector.metadata fields.
You can add as many vector.metadata fields as you want, but you need to specify the prefix "vector.metadata." for each field.


### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#datasource_pinecone).