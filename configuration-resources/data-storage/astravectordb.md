### Connecting to DataStax Astra Vector DB

To use DataStax Astra DB as a vector database using the [JSON API](https://docs.datastax.com/en/astra-serverless/docs/develop/dev-with-json.html), you have to create a "vector-database" resource in your configuration.yaml file.

If you want to use the CQL based API then you have to create a "astra" resource. See the documentation [here](./astra.md).


```yaml
resources:
  - type: "vector-database"
    name: "AstraDatasource"
    configuration:
      service: "astra-vector-db"      
      token: "${ secrets.astra-vector-db.token }"
      enviroment: "${ secrets.astra-vector-db.endpoint }"
```

Required parameters:
- token: this is the token provided by the Astra DB service
- endpoint: this is the URL of your database


### Handling Collections as Assets

You can manage a "collection" in your Astra Database using the "astra-collection" asset type. A collection is a logical container for documents.


```yaml
assets:
  - name: "langstream-keyspace"
    asset-type: "astra-collection"
    creation-mode: create-if-not-exists    
    deletion-mode: delete
    config:
      collection-name: "langstream"
      datasource: "AstraDatasource"  
```

With the "astra-collection" asset, you can create a collection in your Astra DB database.

As usual, you can use the `creation-mode` and `deletion-mode` parameters to control the creation and deletion of the collection.


### Querying an Astra DB collection

When you use the "query-vector-db" agent to query Astra, you can use the following parameters:

```yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "AstraDatasource"
      query: |
        {
          "collection-name": "docs",
          "vector": ?,
          "limit": 10,
          "include-similarity:" true,
          "select": ["text"],
          "filter": {
            "language": "en"            
          }
        }
      fields:
        - "value.question_embeddings"
      output-field: "value.related_documents"
```

As usual you can use the '?' symbol as a placeholder for the fields that you specify in the "fields" section.
The "id" field is always returned by default, so you don't need to specify it in the "select" list.
The "similarity" field is returned depedending on the "include-similarity" parameter, the default is "true".
The "vector" field is returned as long as it is it returned by the query, so you don't need to specify it in the "select" list.

The "vector" filter is special, the query uses the "vector" field to perform a similarity search and not an exact match.

### Writing to Astra INSERT/UPDATE/DELETE

You can use the `query-vector-db` agent to write to Astra and update your collections.

This is an example for the "insertOne" action:

```yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
       datasource: "AstraDatasource"
       mode: "execute"
       query: |
        {
            "action": "insertOne",
            "collection-name": "documents",
            "document": {
                "id": "some-id",
                "name": ?,
                "vector": ?,
                "text": "Some text"
            }
        }
       fields:
         - "value.name"
         - "value.question_embeddings" 
```

Similarly you can use the "findOneAndUpdate" action to update an existing document:


```yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
       datasource: "AstraDatasource"
       mode: "execute"
       query: |
        {
            "action": "findOneAndUpdate",
            "collection-name": "documents",
            "filter": {
                "_id": ?
            },
            "update": {
                "$set": {
                    "text": ?
                }
            }
        }
       fields:
         - "value.document_id"
         - "value.new_text" 
```

In delete one or more documents you can use the "deleteOne" and "deleteMany" actions.

```yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
       datasource: "AstraDatasource"
       mode: "execute"
       query: |
        {
            "action": "deleteOne",
            "collection-name": "documents",
            "filter": {
                "_id": ?
            }
        }
       fields:
         - "value.document_id"
```

This is an example for the "deleteMany" action:

```yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
       datasource: "AstraDatasource"
       mode: "execute"
       query: |
        {
            "action": "deleteMany",
            "collection-name": "documents",
            "filter": {
                "userId": ?
            }
        }
       fields:
         - "value.user_id"
```

### Writing to Astra Vector DB using the "vector-db-sink" agent

When you use the "vector-db-sink" agent to write to Astra, you can use the following parameters:

```yaml
  - name: "Write to Astra"
    type: "vector-db-sink"
    configuration:
      datasource: "AstraDatasource"
      collection-name: "documents"
      fields:
        - name: "id"
          expression: "fn:concat(value.filename, '-', value.chunk_id)"
        - name: "vector"
          expression: "value.embeddings_vector"
        - name: "text"
          expression: "value.text"
        - name: "filename"
          expression: "value.filename"
        - name: "chunk_id"
          expression: "value.chunk_id"
```

Set the collection-name to the name of the collection you want to write to. Then you define the fields in the "fields" list. This works similarly to the ['compute' agent](../../pipeline-agents/data-transform/compute.md), and you can use the same syntax to define the fields.


### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#datasource_astra-vector-db).