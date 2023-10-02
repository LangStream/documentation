# re-rank

When you implement the RAG (Retrieval Agumented Generation) pattern you need to query a Vector Database to get documents related to the input text, then you need to re-rank the results to get the most relevant ones.

The results from the Vector Database are a list of documents, and each document is a text with a vector of floats.

Usually when you want to retrieve the top N documents, you filter the results using a query, but you can still get documents that are not relevant to the input text using this method. This is because the typical Vector Database query is based on the cosine similarity between the input vector and the document vectors.

The Re-ranking agent allows you to further filter the documents with additional processing to validate that the document is relevant to the input text and to keep only the most relevant documents.

The room in the prompt is usually limited, so you want to use as few documents as possible while also keeping the most relevant ones.

One of the most commonly used algorithms for re-ranking is Maximal Marginal Relevance (MMR).

You can find some reference material about MMR here:

\[Maximal Marginal Relevance to Re-rank results in Unsupervised KeyPhrase Extraction]\(https://medium.com/tech-that-works/maximal-marginal-relevance-to-rerank-results-in-unsupervised-keyphrase-extraction-22d95015c7c5)

\[The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries]\(https://www.cs.cmu.edu/\~jgc/publication/The\_Use\_MMR\_Diversity\_Based\_LTMIR\_1998.pdf)

The default implementation of MMR in LangStream is based on the CMU paper above. It uses the B25 algorithm to compute the similarity between the input text and the document text. It also uses the cosine similarity between the query vector and the document vector.

The BM25 algorithm needs a couple of parameters, `k1` and `b`, that you can configure in the agent.

You can find more information about BM25 here:

\[BM25]\(https://en.wikipedia.org/wiki/Okapi\_BM25)

### How to use the re-rank agent

Here is a full example of running a vector search and then re-ranking the results:

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
      model: "{{{secrets.open-ai.embeddings-model}}}" # This needs to match the name of the model deployment, not the base model
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
      k1: 1.2
      b: 0.75
```

### **Topics**

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="155.33333333333331">Label</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td>max</td><td>integer</td><td>Maximum number of documents to keep.</td></tr><tr><td>field</td><td>string</td><td>Reference to the field that contains the documents to sort (for instance `value.query_results``)</td></tr><tr><td>output-field</td><td>string</td><td>Reference to the field that will contain the sorted documents (for instance `value.sorted_results``). You can also use same value as the field **parameter** in order to override it</td></tr><tr><td>query-text</td><td>string</td><td>Reference to the field that contains the original query (i.e. the question from the user)</td></tr><tr><td>query-embeddings</td><td>string</td><td>Reference to the field that contains the embeddings vector computed on the query</td></tr><tr><td>text-field</td><td>string</td><td>Reference to the field in each record that contains text of the document (for instance `record.text`)</td></tr><tr><td>embeddings-field</td><td>string</td><td>Reference to the field in each record that contains the embeddings vector computed on the text (for instance `record.embeddings`)</td></tr><tr><td>algoritm</td><td>string</td><td>This can be `MMR` to use the MMR algorithm or `none` to disable the ranking</td></tr><tr><td>lamdba</td><td>number</td><td>This is the `lamda` parameter in the MMR algorithm</td></tr><tr><td>b</td><td>number</td><td>This is the `b` parameter in the B25 algorithm</td></tr><tr><td>k1</td><td>number</td><td>This is the `k1` parameter in the B25 algorithm</td></tr></tbody></table>
