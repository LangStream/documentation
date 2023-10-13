# RAG pattern

The Retrieval Augmented Generation (RAG) pattern is a powerful way to extend the knowledge base of a language model. It is used to:

* Provide more accurate, up-to-date, and context-aware responses
* Extend the knowledge base of the LLM
* Improve the quality of the generated text

LangStream makes it easy to build applications using the RAG pattern. It currently has native support for [DataStax Astra DB](https://www.datastax.com/products/vector-search), [Pinecone](https://www.pinecone.io/), [Milvus/Zilliz](https://milvus.io/) and [Apache Cassandra](https://cassandra.apache.org).

Please refer to the [Data Storage section](../configuration-resources/data-storage/) for more information on how to configure your vector database.

### Vector search example

Once you have your [vector database](../building-applications/vector-databases.md) populated with text and vector embeddings, you can use the [query-vector-db agent](../pipeline-agents/text-processors/query-vector-db.md) to perform a similarity search.

The flow of a vector search application with the RAG pattern is as follows:

* Start from a query text
* Compute the [embeddings](../pipeline-agents/ai-actions/compute-ai-embeddings.md) of the query text
* [Query](../pipeline-agents/text-processors/query-vector-db.md) the vector database to get the most similar documents
* [Re-rank](broken-reference) the results to get the most relevant documents
* Build a prompt with the query text and the most relevant documents
* [Query the LLM](../pipeline-agents/ai-actions/ai-chat-completions.md) with the prompt to get the final response
* Finally, return the response to the user

```yaml
pipeline:
  - name: "convert-to-structure"
    type: "document-to-json"
    input: "questions-topic"
    configuration:
      text-field: "question"
  - name: "compute-embeddings"
    type: "compute-ai-embeddings"
    configuration:
      model: "${secrets.open-ai.embeddings-model}" # This needs to match the name of the model deployment, not the base model
      embeddings-field: "value.question_embeddings"
      text: "{{% value.question }}"
      flush-interval: 0
  - name: "lookup-related-documents"
    type: "query-vector-db"
    configuration:
      datasource: "JdbcDatasource"
      query: "SELECT text,embeddings_vector FROM documents ORDER BY cosine_similarity(embeddings_vector, CAST(? as FLOAT ARRAY)) DESC LIMIT 20"
      fields:
        - "value.question_embeddings"
      output-field: "value.related_documents"
  - name: "re-rank documents with MMR"
    type: "re-rank"
    configuration:
      max: 5 # keep only the top 5 documents, because we have an hard limit on the prompt size
      field: "value.related_documents"
      query-text: "value.question"
      query-embeddings: "value.question_embeddings"
      output-field: "value.related_documents"
      text-field: "record.text"
      embeddings-field: "record.embeddings_vector"
      algorithm: "MMR"
      lambda: 0.5
      k1: 1.52
      b: 0.75
  - name: "ai-chat-completions"
    type: "ai-chat-completions"

    configuration:
      model: "${secrets.open-ai.chat-completions-model}" # This needs to be set to the model deployment name, not the base name
      # on the log-topic we add a field with the answer
      completion-field: "value.answer"
      # we are also logging the prompt we sent to the LLM
      log-field: "value.prompt"
      # here we configure the streaming behavior
      # as soon as the LLM answers with a chunk we send it to the answers-topic
      stream-to-topic: "answers-topic"
      # on the streaming answer we send the answer as whole message
      # the 'value' syntax is used to refer to the whole value of the message
      stream-response-completion-field: "value"
      # we want to stream the answer as soon as we have 20 chunks
      # in order to reduce latency for the first message the agent sends the first message
      # with 1 chunk, then with 2 chunks....up to the min-chunks-per-message value
      # eventually we want to send bigger messages to reduce the overhead of each message on the topic
      min-chunks-per-message: 20
      messages:
        - role: system
          content: |
              An user is going to perform a questions, The documents below may help you in answering to their questions.
              Please try to leverage them in your answer as much as possible.
              Take into consideration that the user is always asking questions about the LangStream project.
              If you provide code or YAML snippets, please explicitly state that they are examples.
              Do not provide information that is not related to the LangStream project.
            
              Documents:
              {{%# value.related_documents}}
              {{% text}}
              {{%/ value.related_documents}}
        - role: user
          content: "{{% value.question}}"          
```

### What’s next?

Do you have a website lying around just waiting to be turned into a useful chatbot ?\
This complete pipeline is available in the [LangStream repo](https://github.com/LangStream/langstream/tree/main/examples/applications/docker-chatbot), and running it on your own is no sweat.
