# query-vector-db

This agent enables submitting queries to a vector datasource (like [Pinecone](https://docs.pinecone.io/) or [AstraDB](https://www.datastax.com/products/datastax-astra)) and outputting the results.

### Example

Follow the [Pinecone Quickstart docs](https://docs.pinecone.io/docs/quickstart) to create your Pinecone API key, environment, vector index name, and project name, and add them to your secrets.yaml file. These values are required.

Specify a datasource in configuration.yaml:

```yaml
configuration:
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

Reference the "vector-database" datasource and submit a query using input message values in pipeline.yaml:

```yaml
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

The query language depends on the underlying vector database. For example, Pinecone uses a JSON query language. See the [Pinecone Query Language docs](https://docs.pinecone.io/docs/query-language) for more information.

Please refer to the documentation of the vector database you are using for more information on how to write queries:

- [Astra DB](../../configuration-resources/data-storage/astra.md)
- [Apache Cassandra](../../configuration-resources/data-storage/cassandra.md)
- [Pinecone.io](../../configuration-resources/data-storage/pinecone.md)
- [Milvus.io](../../configuration-resources/data-storage/milvus.md)
- [JDBC](../../configuration-resources/data-storage/jdbc.md)


### **Topics**

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="155.33333333333331">Label</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td>datasource</td><td>string</td><td>A reference to the datasource name declared in resources.datasources of the configuration.yaml manifest.</td></tr><tr><td>query</td><td>string</td><td><p>The query statement to run. Each placeholder “?” will be replaced with fields value in order.<br></p><p>Example:</p><pre><code>{
"vector": ?,
"topK": 5,
"filter":
{"$or": [{"genre": "comedy"}, {"year":2019}]}
}
</code></pre></td></tr><tr><td>fields</td><td>string[]</td><td><p>A collection of field values. Each value will be used in order to replace placeholders in the query (do not include mustache brackets, this not a templated value).<br></p><p>Example collection:</p><ul><li>“value.embeddings”</li></ul></td></tr><tr><td>output-field</td><td>string</td><td><p>The name of an additional field to be added to message data containing query result (do not include mustache brackets, this is not a templated value).</p><p></p><p>Provide in the form: “value.&#x3C;field-name>”</p></td></tr></tbody></table>

### What's next?

For more on vector databases, see [Vector Databases](../../building-applications/vector-databases.md).

For more on the datasource resource, see [Datasource](../../configuration-resources/data-storage/datasource.md).
