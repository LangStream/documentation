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

# ai-chat-completions

Given the AI model specified in an application's configuration resources, this agent will use its completion API to submit message prompts and return the result. This agent will discover its type (i.e. OpenAI, Hugging Face, VertexAI) and use the corresponding library to generate the embedding. It is up to the developer to match the correct mode name with the configured AI model.


## Using OpenAI chat models

The `ai-chat-completions` for OpenAI uses the /v1/chat/completions endpoint. Refer to the [OpenAI documentation](https://platform.openai.com/docs/models/model-endpoint-compatibility) to know which models are compatible.

```yaml
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    output: "history-topic"
    configuration:
      model: "${secrets.open-ai.chat-completions-model}" # This needs to be set to the model deployment name, not the base name
      # on the log-topic we add a field with the answer
      completion-field: "value.answer"
      # we are also logging the prompt we sent to the LLM
      log-field: "value.prompt"
      # here we configure the streaming behavior
      # as soon as the LLM answers with a chunk we send it to the answers-topic
      stream-to-topic: "output-topic"
      # on the streaming answer we send the answer as whole message
      # the 'value' syntax is used to refer to the whole value of the message
      stream-response-completion-field: "value"
      # we want to stream the answer as soon as we have 10 chunks
      # in order to reduce latency for the first message the agent sends the first message
      # with 1 chunk, then with 2 chunks....up to the min-chunks-per-message value
      # eventually we want to send bigger messages to reduce the overhead of each message on the topic
      min-chunks-per-message: 10
      messages:
        - role: user
          content: "You are a helpful assistant. Below you can find a question from the user. Please try to help them the best way you can.\n\n{{ value.question}}"
```

## Using VertexAI chat models

Refer to the [VertexAI documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-chat) to know which models are compatible.

```yaml
  - name: "ai-text-completions"
    type: "ai-text-completions"
    output: "answers"
    configuration:
      model: "${secrets.vertex-ai.text-completions-model}"
      # on the log-topic we add a field with the answer
      completion-field: "value.answer"
      # we are also logging the prompt we sent to the LLM
      log-field: "value.prompt"
      max-tokens: 20
      prompt:
        - "{{ value.question}}"
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

<table><thead><tr><th width="182.33333333333331">Label</th><th width="162">Type</th><th>Description</th></tr></thead><tbody><tr><td>model</td><td>string (required)</td><td><p>Given the AI model set in the configuration resources, this is the corresponding model name to use.<br></p><p>Example using the OpenAI model: “gpt-3.5-turbo”</p></td></tr><tr><td>completion-field</td><td>string (required)</td><td><p>The name of an additional field that will be added to the output message data containing the LLM completion.<br></p><p>Provide in the form: “value.&#x3C;field-name>” (do not include mustache brackets, this not a templated value).</p></td></tr><tr><td>log-field</td><td>string (optional)</td><td>This is the final prompt that was submitted to the model.</td></tr><tr><td>stream-to-topic</td><td>string (optional)</td><td></td></tr><tr><td>stream-response-completion-field</td><td>string (optional)</td><td></td></tr><tr><td>messages</td><td>object[]</td><td><p>A collection of LLM prompt messages, see the reference table.</p><p></p><p>Example collection:</p><ul><li>role: user<br>message: “answer the question: {{% value }}”</li><li>role: system<br>message: “You are a friendly customer service agent”</li></ul></td></tr></tbody></table>

#### messages

<table><thead><tr><th width="124.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>role</td><td>string (required)</td><td>Values are limited to what the chosen LLM model supports. Typical values are “user” or “system”.</td></tr><tr><td>content</td><td>string (required)</td><td><p>A templated value that will be sent to the LLM. Refer to message structure and templating for templating options.<br><br></p><p>Example of combining preset prompt and entire input value:</p><p>“You are a friendly customer service agent and like answering questions like: {{% value }}”</p><p><br></p><p>Example of combining preset prompt and specific input value:</p><p>“You are a friendly customer service agent speaking with {{% value.first-name}}. Help them with the question: {{% value.user-question }}”</p></td></tr></tbody></table>
