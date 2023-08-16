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

### Example

If the configuration set Google Vertex as its AI model:

```yaml
configuration:
  resources:
    - type: "vertex-configuration"
      name: "Google Vertex AI configuration"
      configuration:
        url: "{{ secrets.vertex-ai.url }}"
        # use triple quotes in order to turn off escaping
        serviceAccountJson: "{{{ secrets.vertex-ai.serviceAccountJson }}}"
        token: "{{ secrets.vertex-ai.token }}"
        region: "{{ secrets.vertex-ai.region }}"
        project: "{{ secrets.vertex-ai.project }}"
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
