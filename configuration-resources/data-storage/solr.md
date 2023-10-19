# apache Solr

LangStream allows you to use Apache Solr as a vector database. This is useful if you want to use a vector database that is hosted on-premises or in your own cloud environment.

You can find more about how to perform Vector Search in Apache Solr in the [official documentation](https://solr.apache.org/guide/solr/latest/query-guide/dense-vector-search.html)

### Connecting to Solr

To use Apache Solr as a vector database, create a "vector-database" resource in your configuration.yaml file.

```yaml
resources:
    - type: "vector-database"
      name: "SolrDatasource"
      configuration:
        service: "solr"        
        username: "${ secrets.solr.username }"
        password: "${ secrets.solr.password }"
        host: "${ secrets.solr.host }"
        port: "${ secrets.solr.port }"  
        collection-name: "${ secrets.solr.collection-name }"  
      
```

Explanation for the parameters:

* username: the username
* password: the password
* host: the host
* port: the port, usually it is 8983
* collection-name: the name of the collection to connect to

Currently LangStream supports connecting to one Collection at a time, so you need to create a separate resource for each Collection.

LangStream uses the official Apache Solr Java client to connect to Solr.


### Special assets for Apache Solr Cloud

You can use both Solr and Solr Cloud. If you use Solr Cloud then you can also manage the collections using the Solr Cloud API.

To do that, you need to create special assets in your pipeline: "solr-collection".

Here is an example of creating a collection named "documents" with a dense vector, as required to perform Vector Similarity Searches:

```yaml
assets:
  - name: "documents-table"
    asset-type: "solr-collection"
    creation-mode: create-if-not-exists
    deletion-mode: delete
    config:
      collection-name: "documents"
      datasource: "SolrDataSource"
      create-statements:
        - api: "/api/collections"
          method: "POST"
          body: |
            {
              "name": "documents",
              "numShards": 1,
              "replicationFactor": 1
             }
        - "api": "/schema"
          "body": |
            {
             "add-field-type" : {
                   "name": "knn_vector",
                   "class": "solr.DenseVectorField",
                   "vectorDimension": "1536",
                   "similarityFunction": "cosine"
              }
             }

        - "api": "/schema"
          "body": |
            {
              "add-field":{
                "name":"embeddings",
                "type":"knn_vector",
                "stored":true,
                "indexed":true
                }
            }
        - "api": "/schema"
          "body": |
            {
               "add-field":{
                   "name":"text",
                   "type":"string",
                   "stored":true,
                   "indexed":false,
                   "multiValued": false
               }
            }
```

As you can see in the "create-statements" section above, you can configure a number of "commands" that translate to Solr API calls.
You can invoke any of the APIs, for each command you have to declare:
- the "api" you want to call: "/schema" or "/api/collections"
- the body of the HTTP Request, as a JSON string
- you can also set the HTTP method, if you want to use something different than "POST"

If you set "api" to "/schema" then you are using the [Solr Schema API](https://solr.apache.org/guide/solr/latest/indexing-guide/schema-api.html).
If you set "api" to "/api/collections" then you are using the [Solr Collections API](https://solr.apache.org/guide/solr/latest/configuration-guide/collections-api.html).


### Querying Solr

Use the "query-vector-db" agent to query Solr with the following parameters:

```yaml
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "SolrDataSource"
      query: |
        {
          "q": "{!knn f=embeddings topK=10}?"
        }
      fields:
        - "fn:toListOfFloat(value.question_embeddings)"
      output-field: "value.related_documents"
```

As usual you can use the '?' symbol as a placeholder for the fields that you specify in the "q" section.

For Apache Solr, the "query" field requires a JSON that describes the parameters to pass in the Solr query.
Usually you provide a value for "q" for the main query string, and then add other parameters.

In the example above, we are using the "knn" query parser to perform a [Vector Similarity Search](https://solr.apache.org/guide/solr/latest/query-guide/dense-vector-search.html).


### Writing to Solr

Use the "vector-db-sink" agent to write to Solr with the following parameters:

```yaml
  - name: "Write to Solr"
    type: "vector-db-sink"
    input: chunks-topic
    configuration:
      datasource: "SolrDataSource"
      collection-name: "documents"
      fields:
        - name: "id"
          expression: "fn:concat(value.filename, value.chunk_id)"
        - name: "embeddings"
          expression: "fn:toListOfFloat(value.embeddings_vector)"
        - name: "text"
          expression: "value.text"
```

Set the collection-name to the name of the collection you want to write to, and define the fields in the "fields" list. This works similarly to the ['compute' agent](../../pipeline-agents/data-transform/compute.md), where you define the name of the field and the expression to compute the value of the field.


### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#datasource_solr).