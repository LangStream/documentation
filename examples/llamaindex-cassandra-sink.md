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

This is the code for the python sink:

```python

import base64
import io
from typing import Dict, Any

import openai
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from langstream import Sink, Record
from llama_index import VectorStoreIndex, Document
from llama_index.vector_stores import CassandraVectorStore


class LlamaIndexCassandraSink(Sink):
    def __init__(self):
        self.config = None
        self.session = None
        self.index = None

    def init(self, config: Dict[str, Any]):
        self.config = config
        openai.api_key = config["openaiKey"]

    def start(self):
        secure_bundle = self.config["cassandra"]["secureBundle"]
        secure_bundle = secure_bundle.removeprefix("base64:")
        secure_bundle = base64.b64decode(secure_bundle)
        cluster = Cluster(
            cloud={
                "secure_connect_bundle": io.BytesIO(secure_bundle),
                "use_default_tempdir": True,
            },
            auth_provider=PlainTextAuthProvider(
                self.config["cassandra"]["username"],
                self.config["cassandra"]["password"],
            ),
        )
        self.session = cluster.connect()

        vector_store = CassandraVectorStore(
            session=self.session,
            keyspace=self.config["cassandra"]["keyspace"],
            table=self.config["cassandra"]["table"],
            embedding_dimension=1536,
            insertion_batch_size=15,
        )

        self.index = VectorStoreIndex.from_vector_store(vector_store)

    def write(self, record: Record):
        self.index.insert(Document(text=record.value()))

    def close(self):
        if self.session:
            self.session.shutdown()
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
