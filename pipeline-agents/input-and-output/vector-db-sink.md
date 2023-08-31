# vector-db-sink

This agent writes vector data to vector databases.
LangStream currently supports [AstraDB](https://www.datastax.com/products/datastax-astra) and [Pinecone](https://docs.pinecone.io/).

Astra DB and Pinecone are both of the type "vector-db-sink" in a LangStream pipeline, but the databases require different configuration values to map the vector data from the sink into the database.

## Astra DB example

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

### AstraDB Topics

**Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

**Output**

* None, it’s a sink.

### AstraDB Configuration

<table><thead><tr><th width="234.33333333333331">Label</th><th width="114">Type</th><th>Description</th></tr></thead><tbody><tr><td>datasource</td><td>String</td><td>The datasource is defined in the Resources section of configuration.yaml.</td></tr><tr><td>table</td><td>String</td><td>The `keyspace.table-name` the vector data will be written to</td></tr><tr><td>mapping</td><td>String</td><td>How the data from the input records will be mapped to the corresponding columns in the database table. "id=value.id" maps the "id" value in the input record to the "id" value of the database. </td></tr></tbody></table>

## Pinecone Example

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

### Pinecone Topics

**Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

**Output**

* None, it’s a sink.

### Pinecone Configuration

<table><thead><tr><th width="234.33333333333331">Label</th><th width="114">Type</th><th>Description</th></tr></thead><tbody><tr><td>datasource</td><td>String</td><td>The datasource is defined in the Resources section of configuration.yaml.</td></tr><tr><td>vector.id</td><td>String</td><td>Maps id to vector.id</td></tr><tr><td>vector.vector</td><td>String</td><td>Maps the input value "vector" to "vector.vector" in the database.</td></tr><tr><td>vector.namespace</td><td>String</td><td>Maps the input value "namespace" to "vector.namespace" in the database.</td></tr><tr><td>vector.metadata.{metadataField}</td><td>String</td><td>Maps the input value "metadata.{metadataField}" to "vector.metadata.{metadataField}"</td></tr></tbody></table>

