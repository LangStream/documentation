### Connecting to Pinecone.io

In order to use Pinecone.io as a vector database you have to create a "vector-database" resource in your configuration.yaml file.

```yaml
resources:
    - type: "vector-database"
      name: "PineconeDatasource"
      configuration:
        service: "pinecone"
        api-key: "{{{secrets.pinecone.api-key}}}"
        environment: "{{{secrets.pinecone.environment}}}"
        index-name: "{{{secrets.pinecone.index-name}}}"
        project-name: "{{{secrets.pinecone.project-name}}}"
        server-side-timeout-sec: 10
      
```

You are required to provide the following parameters:
- api-key: the addess to connect to Cassandra
- index-name: the name of the index
- project-name: the name of the project
- environment: the environment

You can find the api-key, index-name, project-name and enviroment in the Pinecone.io console.

Optional parameters:
- server-side-timeout-sec: the timeout for any server-side operation (default is 10 seconds)