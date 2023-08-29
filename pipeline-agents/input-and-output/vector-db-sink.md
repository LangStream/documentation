# vector-db-sink

This agent writes to a vector database like [AstraDB](https://www.datastax.com/products/datastax-astra) or [Pinecone](https://docs.pinecone.io/).

Different vector databases are configured slightly differently, but the LangStream declaration of configuration and pipeline in the application remains the same.

### Astra DB example

The Astra DB vector database connection is defined in configuration.yaml:

```yaml
configuration:
  resources:
    - type: "vector-database"
      name: "AstraDatasource"
      configuration:
        service: "astra"
        username: "{{{ secrets.astra.username }}}"
        password: "{{{ secrets.astra.password }}}"
        secureBundle: "{{{ secrets.astra.secureBundle }}}"
```

The "Write to Astra DB" pipeline step takes embeddings as input from "input-topic" and writes them to the configured datasource "AstraDatasource":

```yaml
name: "Write to Astra DB"
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "Write to Cassandra"
    type: "vector-db-sink"
    input: "input-topic"
    configuration:
      datasource: "AstraDatasource"
      table: "vsearch.products"
      mapping: "id=value.id,description=value.description,name=value.name"
```

### Pinecone Example

The "Write to Pinecone" pipeline step takes embeddings as input from "vectors-topic" and writes them to a Pinecone datasource.

The Pinecone vector database connection is defined in configuration.yaml:

```yaml
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

The "Write to Pinecone" pipeline step takes embeddings as input from "input-topic" and writes them to the configured datasource "PineconeDatasource":

```yaml
name: "Write to Pinecone DB"
topics:
  - name: "vectors-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "Write to Pinecone"
    type: "vector-db-sink"
    configuration:
      datasource: "PineconeDatasource"
      vector.id: "value.id"
      vector.vector: "value.embeddings"
      vector.namespace: "value.namespace"
      vector.metadata.genre: "value.genre"
```

### Topics

**Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

**Output**

* None, it’s a sink.

### Configuration

<table><thead><tr><th width="234.33333333333331">Label</th><th width="114">Type</th><th>Description</th></tr></thead><tbody><tr><td>datasource</td><td>String</td><td>The datasource is defined in the Resources section of configuration.yaml.</td></tr><tr><td>vector.id</td><td>String</td><td>Expression specifying how to extract the ID from the data record</td></tr><tr><td>vector.vector</td><td>String</td><td>Expression specifying how to extract the vector data from the data record.</td></tr><tr><td>vector.namespace</td><td>String</td><td>Expression specifying how to extract the namespace from the data record.</td></tr><tr><td>vector.metadata.{metadataField}</td><td>String</td><td>Expression specifying how to extract metadata fields from the data record.</td></tr></tbody></table>

