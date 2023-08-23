# vector-db-sink

This agent writes to a vector database like [Pinecone](https://docs.pinecone.io/) or [AstraDB](https://www.datastax.com/products/datastax-astra).

### Example

The "Write to Pinecone" pipeline step takes embeddings as input from "vectors-topic" and writes them to a Pinecone datasource.

```yaml
name: "Index Products on Vector Database"
topics:
  - name: "vectors-topic"
    creation-mode: create-if-not-exists
errors:
    on-failure: skip
pipeline:
  - name: "compute-embeddings"
    id: "step1"
    type: "compute-ai-embeddings"
    input: "vectors-topic"
    configuration:
      model: "text-embedding-ada-002" # This needs to match the name of the model deployment, not the base model
      embeddings-field: "value.embeddings"
      text: "{{% value.document }}"
  - name: "Write to Pinecone"
    type: "vector-db-sink"
    configuration:
      datasource: "PineconeDatasource"
      vector.id: "value.id"
      vector.vector: "value.embeddings"
      vector.namespace: ""
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

<table><thead><tr><th width="234.33333333333331">Label</th><th width="114">Type</th><th>Description</th></tr></thead><tbody><tr><td>datasource</td><td>String</td><td>The type of datasource</td></tr><tr><td>vector.id</td><td>String</td><td>The vector ID</td></tr><tr><td>vector.vector</td><td>Float</td><td>The vector value</td></tr><tr><td>vector.namespace</td><td>String</td><td>The vector DB's namespace</td></tr><tr><td>vector.metadata</td><td>String</td><td>Filter results by metadata type. For more, see the <a href="https://docs.pinecone.io/docs/metadata-filtering">Pinecone docs</a>.</td></tr></tbody></table>

