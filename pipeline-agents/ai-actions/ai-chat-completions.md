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

> The `ai-chat-completions` for OpenAI uses the /v1/chat/completions endpoint. Refer to the [OpenAI documentation](https://platform.openai.com/docs/models/model-endpoint-compatibility) to know which models are compatible.

Setup the OpenAI LLM [configuration](../../configuration-resources/large-language-models-llms/open-ai-configuration.md).
Add the `ai-chat-completions` agent:

```yaml
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    output: "history-topic"
    configuration:
      model: "gpt-3.5-turbo"
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
          content: "You are a helpful assistant. Below you can find a question from the user. Please try to help them the best way you can.\n\n{{ value.question }}"
```

## Using Ollama chat models

> Refer to the [ollama documentation](https://ollama.ai/library) to find a list of models.

Setup the Ollama [configuration](../../configuration-resources/large-language-models-llms/ollama-configuration.md).
Add the `ai-chat-completions` agent:

```yaml
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    configuration:
      model: "llama2"
      max-tokens: 100
      completion-field: "value.chatresult"
      log-field: "value.request"
      messages:
        - role: user
          content: "This is my question.Please answer briefly:\n\n{{ value.question }}"
```

## Using Amazon Bedrock AI21 Jurassic-2 models

> Refer to the [Amazon documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html#model-parameters-jurassic2) for other parameters and options.

Set up the Amazon Bedrock LLM [configuration](../../configuration-resources/large-language-models-llms/uration.md).
Add the `ai-chat-completions` agent:

```yaml
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    configuration:
      model: "ai21.j2-mid-v1"
      completion-field: "value.answer"
      options:
        request-parameters:
          # here you can add all the supported parameters
          temperature: 0.5
          maxTokens: 300
        # expression to retrieve the completion from the response JSON. It varies depending on the model 
        response-completions-expression: "completions[0].data.text"
      messages:
        - content: "{{ value.question }}"
```



## Using Amazon Bedrock Anthropic Claude models

> Refer to the [Amazon documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html#model-parameters-claude) to learn other parameters and options.

Setup the Amazon Bedrock LLM [configuration](../../configuration-resources/large-language-models-llms/bedrock-configuration.md).
Add the `ai-chat-completions` agent:

```yaml
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    configuration:
      model: "anthropic.claude-v2"
      completion-field: "value.answer"
      options:
        request-parameters:
          # here you can add all the supported parameters
          temperature: 0.5
          max_tokens_to_sample: 300
          top_p: 0.9
          top_k: 250
        # expression to retrieve the completion from the response JSON. It varies depending on the model 
        response-completions-expression: "completion"
      messages:
        - content: "{{ value.question }}"
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

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#ai-chat-completions).
