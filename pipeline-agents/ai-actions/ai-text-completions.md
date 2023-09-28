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

# ai-text-completions

Given the AI model specified in an application's configuration resources, this agent will use its completion API to submit message prompts and return the result. This agent will discover its type (i.e. OpenAI, Hugging Face, VertexAI) and use the corresponding library to generate the embedding. It is up to the developer to match the correct mode name with the configured AI model.

## Using OpenAI text models

The `ai-text-completions` for OpenAI uses the /v1/completions endpoint. Refer to the [OpenAI documentation](https://platform.openai.com/docs/models/model-endpoint-compatibility) to know which models are compatible.

```yaml
pipeline:
  - name: "ai-text-completions"
    type: "ai-text-completions"
    configuration:
      model: "gpt-3.5-turbo-instruct"
      prompt:
        - "{{% value.question }}"
```

## Using VertexAI text models

Refer to the [VertexAI documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text) to know which models are compatible.
```yaml
pipeline:
  - name: "ai-text-completions"
    type: "ai-text-completions"
    configuration:
      model: "text-bison"
      max-tokens: 100
      prompt:
        - "{{% value.question }}"
```

{% hint style="info" %}
VertexAI text completions accepts only one `prompt` value.
{% endhint %}


## Using HuggingFace models

{% hint style="info" %}
`ai-chat-completions` and `ai-text-completions` are equivalent for Hugging Face models.
{% endhint %}

Refer to the [HugginFace documentation](https://huggingface.co/docs/api-inference/quicktour) to know more about HuggingFace inference API.

```yaml
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    configuration:
      model: "gpt2"
      prompt:
        - "You are a helpful assistant. Below you can find a question from the user. Please try to help them the best way you can.\n\n{{% value.question}}"
```


### Prompt limitations

Most public LLMs have character limits on message content. It is up to the application developer to ensure the combination of preset prompt text and an input message stays under that limit.

### Costs incurred

Some public LLMs offer a free tier and then automatically begin charging per prompt (or by prompt chunk). It is up to the application developer to be aware of these possible charges and manage them appropriately.

### Topics

#### Input

* Structured and unstructured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

#### Output

* Structured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

<table><thead><tr><th width="182.33333333333331">Label</th><th width="162">Type</th><th>Description</th></tr></thead><tbody><tr><td>model</td><td>string (required)</td><td><p>Given the AI model set in the configuration resources, this is the corresponding model name to use.<br></p><p>Example using the OpenAI model: “gpt-3.5-turbo-instruct”</p></td></tr><tr><td>completion-field</td><td>string (required)</td><td><p>The name of an additional field that will be added to the output message data containing the LLM completion.<br></p><p>Provide in the form: “value.&#x3C;field-name>” (do not include mustache brackets, this not a templated value).</p></td></tr><tr><td>log-field</td><td>string (optional)</td><td>This is the final prompt that was submitted to the model.</td></tr><tr><td>stream-to-topic</td><td>string (optional)</td><td></td></tr><tr><td>stream-response-completion-field</td><td>string (optional)</td><td></td></tr><tr><td>prompt</td><td>string[]</td><td><p>A collection of LLM prompt messages</p><p></p><p>Example collection:</p><ul><li>- “Translate from English to Italian: {{% value }}”</li></ul></td></tr></tbody></table>

