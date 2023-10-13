---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# compute-ai-embeddings

This agent uses the configured AI model’s embedding feature to transform a string of text into a vector embedding. At present, it is assumed that only one AI mode will be set in configuration.yaml. This agent will discover its type (ie OpenAI, Hugging Face, Vertex) and use the corresponding library to generate the embedding. It is up to the developer to match the correct embedding model with the configured AI model.

### JSON and String inputs

This agent currently only accepts JSON-formatted inputs.&#x20;

Either ensure the input is JSON, or put the [document-to-json](../text-processors/document-to-json.md) agent before the compute-ai-embeddings agent in your pipeline:

```yaml
pipeline:
  - name: "convert-to-json"
    type: "document-to-json"
    input: "input-topic"
    configuration:
      text-field: "question"
  - name: "compute-embeddings"
    id: "step1"
    type: "compute-ai-embeddings"
    input: "input-topic"
    output: "output-topic"
    configuration:
      model: "${secrets.open-ai.embeddings-model}" # This needs to match the name of the model deployment, not the base model
      embeddings-field: "value.embeddings"
      text: "{{ value.name }} {{ value.description }}"
      batch-size: 10
      # this is in milliseconds. It is important to take this value into consideration when using this agent in the chat response pipeline
      # in fact this value impacts the latency of the response
      # for latency sensitive applications, consider to set batch-size to 1 or flush-interval to 0
      flush-interval: 500
```

### Example

If the configuration set Google Vertex as its AI model:

```yaml
configuration:
  resources:
    - type: "vertex-configuration"
      name: "Google Vertex AI configuration"
      configuration:
        url: "${ secrets.vertex-ai.url }"
        # use triple quotes in order to turn off escaping
        serviceAccountJson: "${ secrets.vertex-ai.serviceAccountJson }"
        token: "${ secrets.vertex-ai.token }"
        region: "${ secrets.vertex-ai.region }"
        project: "${ secrets.vertex-ai.project }"
```

Then the agent should be:

```yaml
- name: "compute-embeddings"
  id: "step1"
  type: "compute-ai-embeddings"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    model: "textembedding-gecko"
    embeddings-field: "value.embeddings"
    text: "{{% value }}"
```

### Automatically computing the embeddings over a list of inputs

It is possible to perform the same computation over a list of inputs - for example, a list of questions.
You can take the [Flare pattern](../../building-applications/flare-pattern.md) as an example.

In the example below we use the 'loop-over' capability to compute the embeddings for each document in the list of documents to retrieve.

```yaml
  - name: "compute-embeddings"
    type: "compute-ai-embeddings"
    configuration:
      loop-over: "value.documents_to_retrieve"
      model: "${secrets.open-ai.embeddings-model}"
      embeddings-field: "record.embeddings"
      text: "{{ record.text }}"
```   

When you use "loop-over", the agent executes for each element in a list instead of operating on the whole message.
Use "record.xxx" to refer to the current element in the list.

The snippet above computes the embeddings for each element in the list "documents_to_retrieve". The list is expected to be a struct like this:

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

### Topics

#### Input

* Structured and unstructured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

#### Output

* Structured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

<table><thead><tr><th width="187.33333333333331">Label</th><th width="161">Type</th><th>Description</th></tr></thead><tbody><tr><td>model</td><td>string (required)</td><td><p>Given the AI model set in the configuration, this is the corresponding embedding type to use.<br></p><p>Example using the OpenAI model: “text-embedding-ada-002”</p></td></tr><tr><td>embeddings-field</td><td>string (required)</td><td><p>The name of an additional field that will be added to output message data containing generated embedding.<br></p><p>Provide in the form: “value.&#x3C;field-name>” (do not include mustache brackets, this not a templated value)</p></td></tr><tr><td>text</td><td>string (required)</td><td>The text to use.</td></tr></tbody></table>
