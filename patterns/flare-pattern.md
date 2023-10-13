# FLARE pattern

The Flare pattern is an extension of the [The Retrieval Augmented Generation (RAG) pattern](./rag-pattern.md) that adds a feedback loop to improve the quality of the answers provided by the LLM.

You can read the original paper describing the FLARE pattern [here](https://arxiv.org/abs/2305.06983).

Please note that FLARE can currently be implemented only with OpenAI models and the [ai-text-completions](../pipeline-agents/ai-actions/ai-text-completions.md) agent because it requires the probability of correctness (logprobs) for each token.

### How does Flare work ?

The idea behind Flare is quite simple: using the Completions API, the LLM returns a "probability" for each token in the generated text. With this information, we can identify the tokens that are more likely to be wrong and retrieve more pieces of information (documents) to automatically build a better prompt for the LLM.

This is the flow of a Flare pipeline:

1. Start with a query text
2. Add the query text to the list of queries for the vector database ("documents to retrieve")
3. Compute the embeddings for each document to retrieve
4. Lookup relevant documents from a [vector database](vector-databases.md)
5. Add the results to the list of documents to use to build the prompt
6. Build a prompt with the query text and the most relevant documents
7. [Query the LLM](../pipeline-agents/ai-actions/ai-text-completions.md) with the prompt to get the final response, and the logprobs for each token
8. Build a list of "Uncertain spans" (sequences of tokens with low probability)
9. If there is at least one uncertain span, add them to the "documents to retrieve" list and go back to step 3
10. If there is no uncertain span or we did too many iterations, return the response to the user

As you can see at point 6, there is a feedback loop that allows us to improve the quality of the answer.

In LangStream we implement the loop by sending the current record to the topic that is used as input for the pipeline at step 3.

This is pretty easy and intuitive and allows you to implement a Flare pipeline with just a few lines of code.

\### Benefits of using a topic to perform the loop

The presence of a buffer topic to implement the loop has several benefits:

* You can retry in case of failure while computing the embeddings or querying the vector database
* Back pressure is handled automatically by the platform
* You can deal with multiple queries at the same time
* You can batch requests to the embedding service
* You can batch requests to the vector database
* You can prevent the vector database and the embedding service from being overloaded

Basically, a buffer topic allows you to build a scalable version of the Flare pattern.

### Using the Flare Controller Agent

The FLARE loop is handled by the [flare-controller](../pipeline-agents/ai-actions/flare-controller.md) agent. The flare controller agent handles steps 5, 6 and 7 of the flow above:

* collects the list of uncertain spans
* adds the uncertain spans to the list of documents to retrieve
* triggers the loop (by writing to the input topic of the flare loop)
* handles the maximum number of iterations

The flare-controller agent uses a field in the message called "flare\_iterations" by default to handle the number of iterations.

### Using the embedding service over a list of documents

To implement the Flare pattern, you need to query the embedding service multiple times. LangStream provides an easy way to perform the same operation over a list of documents with the 'loop-over' capability.

In the example below we use the 'loop-over' capability to query the embedding service for each document in the list of documents to retrieve.

```yaml
  - name: "compute-embeddings"
    type: "compute-ai-embeddings"
    configuration:
      loop-over: "value.documents_to_retrieve"
      model: "${secrets.open-ai.embeddings-model}"
      embeddings-field: "record.embeddings"
      text: "{{ record.text }}"
```

When you use "loop-over", the agent executes for each element in a list instead of operating on the whole message. Use "record.xxx" to refer to the current element in the list.

The snippet above computes the embeddings for each element in the list "documents\_to\_retrieve". The list is expected to be a struct like this:

```json
{
  "documents_to_retrieve": [
      {
        "text": "the text of the first document"
      },
      {
        "text": "the text of the second document"
      }
    ]
}
```

After running the agent the contents of the list are:

```json
{
  "documents_to_retrieve": [
      {
        "text": "the text of the first document",
        "embeddings": [1,2,3,4,5]
       },
       {
        "text": "the text of the second document",
        "embeddings": [6,7,8,9,10]
       }
    ]
}
```

### Querying the vector database over a list of documents

To implement the Flare pattern, you need to query the vector database to look up documents relevant to more than one input query. LangStream provides an easy way to perform the same operation over a list of documents with the 'loop-over' capability.

In the example below we use the 'loop-over' capability to query the database for each document in the list of documents to retrieve.

```yaml
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "JdbcDatasource"
      # execute the agent for all the document in documents_to_retrieve
      # you can refer to each document with "record.xxx"
      loop-over: "value.documents_to_retrieve"
      query: |
              SELECT text,embeddings_vector
              FROM documents
              ORDER BY cosine_similarity(embeddings_vector, CAST(? as FLOAT ARRAY)) DESC LIMIT 5
      fields:
        - "record.embeddings"
      # as we are looping over a list of document, the result of the query
      # is the union of all the results
      output-field: "value.retrieved_documents"
```

When you use "loop-over", the agent executes for each element in a list instead of operating on the whole message. Use "record.xxx" to refer to the current element in the list.

The snippet above computes the embeddings for each element in the list "documents\_to\_retrieve". The list is expected to be a struct like this:

```json
{
  "documents_to_retrieve": [
      {
        "text": "the text of the first document",
        "embeddings": [1,2,3,4,5]
       },
       {
        "text": "the text of the second document",
        "embeddings": [6,7,8,9,10]
       }
    ]
}
```

The agent then adds all the results to a new field named "retrieved\_documents" in the message.

After running the agent the contents of the list are:

```json
{
    "documents_to_retrieve": [
      {
        "text": "the text of the first document",
        "embeddings": [1,2,3,4,5]
       },
       {
        "text": "the text of the second document",
        "embeddings": [6,7,8,9,10]
       }
    ],
  "retrieved_documents": [
      {
        "text": "the text of some document relevant",
        "embeddings_vector": [0.2,7,8,9,5]
       },
       {
        "text": "the text of another document",
        "embeddings_vector": [0.2,3,8,9,2]
       },
       {
        "text": "the text of another document",
        "embeddings_vector": [1.2,9,3,3,3]
       }
    ]
}
```

This behaviour is different from the "compute-ai-embeddings" agent. The "query-vector-db" agent used here adds the results to the message instead of replacing the original list, and the results are all added to the same field.

### Example

```yaml

topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
  - name: "flare-loop-input-topic"
    creation-mode: create-if-not-exists
  - name: "output-topic"
    creation-mode: create-if-not-exists
pipeline:
  # Add the text of the initial task to the list of documents to retrieve
  # and prepare the structure
  - name: "init-structure"
    id: "kickstart-chat"
    type: "document-to-json"
    input: "input-topic"
    configuration:
      text-field: "text"
  - name: "kickstart-document-retrieval"
    type: "compute"
    output: "flare-loop-input-topic"
    configuration:
      fields:
        - name: "value.documents_to_retrieve"
          expression: "fn:listAdd(fn:emptyList(), value.text)"
        - name: "value.related_documents"
          expression: "fn:emptyList()"

  ## Flare loop
  # for each document to retrieve we compute the embeddings vector
  # documents_to_retrieve: [ { text: "the text", embeddings: [1,2,3] }, .... ]
  - name: "convert-docs-to-struct"
    id: "flare-loop"
    type: "compute"
    input: "flare-loop-input-topic"
    configuration:
      fields:
        - name: "value.documents_to_retrieve"
          expression: "fn:listToListOfStructs(value.documents_to_retrieve, 'text')"
        - name: "value.related_documents"
          expression: "fn:emptyList()"
  - name: "compute-embeddings"
    type: "compute-ai-embeddings"
    configuration:
      loop-over: "value.documents_to_retrieve"
      model: "${secrets.open-ai.embeddings-model}"
      embeddings-field: "record.embeddings"
      text: "{{ record.text }}"
      flush-interval: 0
  # for each document we query the vector database
  # the result goes into "value.retrieved_documents"
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "JdbcDatasource"
      # execute the agent for all the document in documents_to_retrieve
      # you can refer to each document with "record.xxx"
      loop-over: "value.documents_to_retrieve"
      query: |
              SELECT text,embeddings_vector
              FROM documents
              ORDER BY cosine_similarity(embeddings_vector, CAST(? as FLOAT ARRAY)) DESC LIMIT 5
      fields:
        - "record.embeddings"
      # as we are looping over a list of document, the result of the query
      # is the union of all the results
      output-field: "value.retrieved_documents"
  - name: "add-documents-to-list"
    type: "compute"
    configuration:
        fields:
          # now we add all the retrieved_documents tp the list
          # of documents to pass to the LLM
          - name: "value.related_documents"
            expression: "fn:addAll(value.related_documents, value.retrieved_documents)"
          # reset previous list (not needed, but clearer)
          - name: "value.retrieved_documents"
            expression: "fn:emptyList()"
          - name: "value.documents_to_retrieve"
            expression: "fn:emptyList()"
  - name: "query-the-LLM"
    type: "ai-text-completions"
    configuration:
      model: "${secrets.open-ai.text-completions-model}"
      completion-field: "value.result"
      logprobs: 5
      logprobs-field: "value.tokens"
      max-tokens: 100
      prompt:
          - |
              There is a list of documents that you must use to perform your task.
              Do not provide information that is not related to the provided documents.
              
              {{# value.related_documents}}
              {{text}}
              {{/ value.related_documents}}
        
              This is the task:
              {{ value.text }}

  - name: "ensure-quality-of-result"
    type: "flare-controller"
    configuration:
        tokens-field: "value.tokens.tokens"
        logprobs-field: "value.tokens.logprobs"
        loop-topic: "flare-loop-input-topic"
        retrieve-documents-field: "value.documents_to_retrieve"
  - name: "cleanup-response"
    type: "compute"
    output: "output-topic"
    configuration:
      fields:
        - name: "value"
          expression: "value.result"     
```

### What’s next?

Do you have a website lying around just waiting to be turned into a useful chatbot ?\
This complete pipeline is available in the [LangStream repo](https://github.com/LangStream/langstream/tree/main/examples/applications/docker-chatbot), and running it on your own is no sweat.
