---
description: Part 4 of the Agent Developer Guide
---

# Passing enviroment variables to the agent

{% hint style="info" %}
This is Part 4 of the Agent Developer Guide. Start at the beginning [here.](./)
{% endhint %}

Many Python libraries, especially LangChain, use ENV variables to configure their behavior and these ENV variables often contain secrets like the OPENAI_API_KEY.

You can easily map ENV variables to secrets and to global variables using the enviroment configuration entry.

This is an example about how to pass the OPENAI_API_KEY to the agent and also configure LangSmith integration:


```yaml
    configuration:
      className: example.ChatBotService
      environment:
        - key: "OPENAI_API_KEY"
          value: "${secrets.open-ai.access-key}"
        - key: "LANGCHAIN_TRACING_V2"
          value: "true"
        - key: "LANGCHAIN_ENDPOINT"
          value: "${ secrets.lang-smith.api-url }"
        - key: "LANGCHAIN_API_KEY"
          value: "${ secrets.lang-smith.api-key }"

```

With this syntax you can leverage the secrets management of LangStream to pass secrets to your agent.

If you have multiple agents in the same pipeline, they won't have access to the secrets of each other.


### What's next?

Continue on to Part 3 of the Agent Developer Guide, [Configuration and Testing.](configuration-and-testing.md)
