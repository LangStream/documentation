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

This agent currently only accepts JSON-formatted inputs.

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

### Using Open AI

Set up the OpenAI LLM [configuration](../../configuration-resources/large-language-models-llms/open-ai-configuration.md).
Add the `compute-ai-embeddings` agent:


```yaml
- name: "compute-embeddings"
  type: "compute-ai-embeddings"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    model: "text-embedding-ada-002"
    embeddings-field: "value.embeddings"
    text: "{{ value }}"
```

### Using Google Vertex AI

Set up the Vertex LLM [configuration](../../configuration-resources/large-language-models-llms/vertex-configuration.md).
Add the `compute-ai-embeddings` agent:


```yaml
- name: "compute-embeddings"
  type: "compute-ai-embeddings"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    model: "textembedding-gecko"
    embeddings-field: "value.embeddings"
    text: "{{ value }}"
```

### Using Ollama

> Refer to the [ollama documentation](https://ollama.ai/library) to find a list of models.

Setup the Ollama [configuration](../../configuration-resources/large-language-models-llms/ollama-configuration.md).

Add the `compute-ai-embeddings` agent:


```yaml
- name: "compute-embeddings"
  type: "compute-ai-embeddings"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    model: "llama2"
    embeddings-field: "value.embeddings"
    text: "{{ value }}"
```

{% hint style="info" %}
Ollama models may compute embeddings but currently they are not as good as the ones provided by OpenAI or Huggingface. In the future Ollama will models specifics for embeddings.
{% endhint %}

### Using Amazon Bedrock

Set up the Amazon Bedrock LLM [configuration](../../configuration-resources/large-language-models-llms/bedrock-configuration.md).
Add the `compute-ai-embeddings` agent:

```yaml
- name: "compute-embeddings"
  type: "compute-ai-embeddings"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    model: "amazon.titan-embed-text-v1"
    embeddings-field: "value.embeddings"
    text: "{{ value }}"
```

### Using Huggingface

Set up the Huggingface resource [configuration](../../configuration-resources/large-language-models-llms/hugging-face-configuration.md).
Add the `compute-ai-embeddings` agent:

```yaml
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

Set `HUGGING_FACE_PROVIDER=api` and provide your Huggingface key and embeddings model to use the HF inference API:
```yaml
export HUGGING_FACE_PROVIDER=api
export HUGGING_FACE_ACCESS_KEY=your_access_key
export HUGGING_FACE_EMBEDDINGS_MODEL=multilingual-e5-small
```

To compute text embeddings with a local model instead of calling the Huggingface API, set `HUGGING_FACE_PROVIDER=local` and set your embeddings model.
```yaml
HUGGING_FACE_PROVIDER=local
HUGGING_FACE_EMBEDDINGS_MODEL=multilingual-e5-small
HUGGING_FACE_EMBEDDINGS_MODEL_URL=djl://ai.djl.huggingface.pytorch/intfloat/multilingual-e5-small
```
The above example will use the multilingual-e5-small Huggingface model locally via the [Deep Java Library](https://github.com/deepjavalibrary/djl/blob/master/extensions/tokenizers/README.md#use-djl-huggingface-model-converter-experimental).

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

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#compute-ai-embeddings).
