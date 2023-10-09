# LlamaIndex Cassandra sink

LlamaIndex is a tool for building LLM-powered applications over custom data.

Connect this sink to LangStream to sink records to a Cassandra vector database via LlamaIndex.

### Example

This example pipeline receives records from an input topic and sinks the records to a vector database via LlamaIndex.

```yaml
name: "LlamaIndex Cassandra sink"
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "Compute embeddings and store them in Cassandra using LlamaIndex"
    type: "python-sink"
    input: "input-topic"
    configuration:
      className: llamaindex_cassandra.LlamaIndexCassandraSink
      openaiKey: "${ secrets.open-ai.access-key }"
      cassandra:
        username: "${ secrets.astra.clientId }"
        password: "${ secrets.astra.secret }"
        secureBundle: "${ secrets.astra.secureBundle }"
        keyspace: ks1
        table: vs_ll_openai
```

### Topics

**Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

**Output**

* None, it’s a sink.

### Configuration

| Label          | Type   | Description                                                                     |
| -------------- | ------ | ------------------------------------------------------------------------------- |
| `openaiKey`    | String | The API key used to authenticate with the OpenAI service.                       |
| `secureBundle` | String | A base64-encoded secure connect bundle for connecting to the Cassandra cluster. |
| `username`     | String | The username used for authentication to the Cassandra cluster.                  |
| `password`     | String | The password used for authentication to the Cassandra cluster.                  |
| `keyspace`     | String | The keyspace (namespace) in Cassandra to be used.                               |
| `table`        | String | The name of the Cassandra table where the data will be written.                 |
