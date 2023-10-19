# OpenSearch

LangStream allows you to use OpenSearch as a vector database. 

You can find more about how to perform Vector Search with OpenSearch in the [official documentation](https://opensearch.org/docs/latest/search-plugins/knn/index/)

> Only OpenSearch 2.x is officially supported.

### Connecting to OpenSearch 

Create a `vector-database` resource in your configuration.yaml file.
A single resource is bound to a single index.

```yaml
resources:
    - type: "vector-database"
      name: "OpenSearch"
      configuration:
        service: "opensearch"        
        username: "${secrets.opensearch.username}"
        password: "${secrets.opensearch.password}"
        host: "${secrets.opensearch.host}"
        port: "${secrets.opensearch.port}"
        index-name: "my-index-000"
```

### Connecting to AWS OpenSearch service 

```yaml
resources:
    - type: "vector-database"
      name: "OpenSearch"
      configuration:
        service: "opensearch"
        username: "${secrets.opensearch.username}"
        password: "${secrets.opensearch.password}"
        host: "${secrets.opensearch.host}"
        region: "${secrets.opensearch.region}"
        index-name: "my-index-000"
```

- `username` is the AWS Access Key.
- `password` is the AWS Secret Key.
- `host` is the endpoint provided by AWS. e.g. for AWS OpenSearch serverless it looks like this: xxxx.<region>.aoss.amazonaws.com
- `region` is the AWS region. It has to match with the one used in the endpoint.



#### Declare an index as asset

To bind the application startup to the OpenSearch index creation, you need to use the `opensearch-index` asset type.

You can configure `settings` and `mappings` as you prefer. Other configuration fields are not supported.

This is an example mixing normal fields with vector fields. The `knn` plugin is required in the target OpenSearch instance.
```yaml
- name: "os-index"
  asset-type: "opensearch-index"
  creation-mode: create-if-not-exists
  config:
    datasource: "OpenSearch"
    settings: |
      {
            "index": {
                  "knn": true,
                  "knn.algo_param.ef_search": 100
            }
        }
    mappings: |
      {
            "properties": {
                  "content": {
                        "type": "text"
                  },
                  "embeddings": {
                        "type": "knn_vector",
                        "dimension": 1536
                  }
            }
        }
```

Refer to the [settings](https://opensearch.org/docs/latest/im-plugin/index-settings/) documentation for the `settings` field.
Refer to the [mappings](https://opensearch.org/docs/latest/field-types/index/) documentation for the `mappings` field.


#### Search

Use the `query-vector-db` agent to perform searches on the index, with the following parameters:

```yaml
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "OpenSearch"
      query: |
        {
          "size": 1,
          "query": {
            "knn": {
              "embeddings": {
                "vector": ?,
                "k": 1
              }
            }
          }
        }
      fields:
        - "value.question_embeddings"
      output-field: "value.related_documents"
```

As usual you can use the '?' symbol as a placeholder for the fields.

The `query` is the body sent to OpenSearch. Refer to the [documentation](https://opensearch.org/docs/latest/query-dsl/index/) to learn which parameters are supported.
Note that the query will be executed on the configured index. Multi-indexes queries are not supported, altough you can declare multiple datasources and deal with different indexes in the same application.

The `output-field` will contain the result. 
The result is in form of array, where each item contains:
- `id`: the document ID
- `document`: the document source 
- `score`: the document score
- `index`: the index name

For example, if you want keep only a relevant field from the first result you can use the `compute` agent after the search:

```yaml
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "OpenSearch"
      query: |
        {
          "size": 1,
          "query": {
            "match_all": {}
          }
        }
      output-field: "value.related_documents"
      only-first: true
  - name: "Format response"
    type: compute
    configuration:
      fields:
        - name: "value"
          type: STRING
          expression: "value.related_documents.document.content"
```


### Indexing

Use the `vector-db-sink` agent to index data, with the following parameters:

```yaml
  - name: "Write to Solr"
    type: "vector-db-sink"
    input: chunks-topic
    configuration:
      datasource: "OpenSearch"
      bulk-parameters:
        timeout: 2m
      fields:
        - name: "id"
          expression: "fn:concat(value.filename, value.chunk_id)"
        - name: "embeddings"
          expression: "fn:toListOfFloat(value.embeddings_vector)"
        - name: "text"
          expression: "value.text"
```


All the indexes are performed using the Bulk operation.
You can customize the [bulk parameters](https://opensearch.org/docs/latest/api-reference/document-apis/bulk/#url-parameters) with the `bulk-parameters` property.

The request will be flushed depending on `flush-interval` and `batch-size` parameters.

### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#datasource_opensearch).