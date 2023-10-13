# Milvus

#### Connecting to Milvus.io

To use Milvus.io as a vector database, create a "vector-database" resource in your configuration.yaml file.

```yaml
resources:
    - type: "vector-database"
      name: "MilvusDatasource"
      configuration:
        service: "milvus"
        ## OSS Milvus
        username: "${ secrets.milvus.username }"
        password: "${ secrets.milvus.password }"
        host: "${ secrets.milvus.host }"
        port: "${ secrets.milvus.port }"
        ## Set to "upsert" for OSS Milvus, on Zilliz use "delete-insert"
        write-mode: "${ secrets.milvus.write-mode }"
        ## Zillis
        url: "${ secrets.milvus.url }"
        token: "${ secrets.milvus.token }"
      
```

Depending on the Milvus version you are using, you need to set different authentication parameters.

If you are on Milvus Cloud you need to set:

* url: the url of the Milvus Cloud instance (it should be something like https://milvus-cloud-xxxxx.milvuscloud.com)
* token: the token to use to authenticate

You can find the URL and the token in the Milvus Cloud console.

If you are on OSS Milvus you need to set:

* username: the username
* password: the password
* host: the host
* port: the port

Recent versions of Milvus (like 2.3+) support Upserts but older versions do not. If you are using an older version of Milvus, you need to set the write-mode to "delete-insert".

The values for **write-mode**:

* "upsert": use upserts
* "delete-insert": delete the document and then insert it again

#### Special assets for Milvus

You can automatically create Collections and Indexes in Milvus as part of the deployment of your LangStream application.

In order to do that, you need to create special assets in your pipeline: "milvus-collection".

```yaml
assets:
  - name: "documents-table"
    asset-type: "milvus-collection"
    creation-mode: create-if-not-exists
    deletion-mode: delete
    config:
      collection-name: "docs"
      database-name: "default"
      datasource: "MilvusDatasource"
      create-statements:
        - |
          {
              "command": "create-collection",
              "collection-name": "docs",
              "database-name": "default",
              "field-types": [
                 {
                    "name": "filename_and_chunkid",
                    "primary-key": true,
                    "data-type": "Varchar",
                    "max-length": 1024
                 },                
                 {
                    "name": "text",
                    "data-type": "Varchar",
                    "max-length": 65535
                 },
                {
                    "name": "language",
                    "data-type": "Varchar",
                    "max-length": 3
                 },
                 {
                    "name": "vector",
                    "data-type": "FloatVector",
                    "dimension": 1536
                 }
              ]
          }
        - |
          {
             "command": "create-index",
             "collection-name": "docs",
             "database-name": "default",
             "field-name": "vector",
             "index-name": "vector_index",
             "index-type": "AUTOINDEX",
             "metric-type": "L2"
          }
        - |
          {
             "command": "load-collection"
          }
```

As you can see in the "create-statements" section above, you can configure a number of "commands" that translate to Milvus API calls. The available commands are:

* create-collection: create a collection using the CreateCollection API
* create-simple-collection: create a collection using the CreateSimpleCollection API. This doesn't need to explicitly specify the field types, just create the index on the vector field and load the collection
* load-collection: load the collection in Milvus, to allow searches
* create-index: create a Vector index, this is required if you are using the "create-collection" command

#### Querying Milvus

When you use the "query-vector-db" agent to query Milvus, you can use the following parameters:

````yaml
pipeline:
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "MilvusDatasource"
      query: |
        {
          "collection-name": "docs",
          "vectors": ?,
          "top-k": 10,
          "output-fields": ["text"]
        }
      fields:
        - "value.question_embeddings"
      output-field: "value.related_documents"
``

As usual you can use the '?' symbol as a placeholder for the fields that you specify in the "fields" section.

### Writing to Milvus

When you use the "vector-db-sink" agent to write to Milvus, you can use the following parameters:

```yaml
  - name: "Write to Milvus"
    type: "vector-db-sink"
    input: chunks-topic
    configuration:
      datasource: "MilvusDatasource"
      collection-name: "docs"
      fields:
        - name: "filename_and_chunkid"
          expression: "fn:concat(value.filename, value.chunk_id)"
        - name: "vector"
          expression: "fn:toListOfFloat(value.embeddings_vector)"
        - name: "language"
          expression: "value.language"
        - name: "text"
          expression: "value.text"
        - name: "num_tokens"
          expression: "value.chunk_num_tokens"
````

Set the collection-name to the name of the collection you want to write to. Then you define the fields in the "fields" list. This works similarly to the ['compute' agent](broken-reference), and you can use the same syntax to define the fields.
