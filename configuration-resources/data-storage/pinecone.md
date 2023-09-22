### Connecting to Pinecone.io

To use Pinecone.io as a vector database, create a "vector-database" resource in your configuration.yaml file.

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

Required parameters:
- api-key: your Pinecone API key
- index-name: the name of the index
- project-name: the name of the project
- environment: the environment

You can find the api-key, index-name, project-name and enviroment in the Pinecone.io console.

Optional parameters:
- server-side-timeout-sec: the timeout for any server-side operation (default is 10 seconds)