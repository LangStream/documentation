---
description: Part 4 of the Agent Developer Guide
---

# Environment variables

{% hint style="info" %}
This is Part 4 of the Agent Developer Guide. Start at the beginning [here.](./)
{% endhint %}

Many Python libraries, especially LangChain, use ENV variables to configure their behavior and these ENV variables often contain secrets like the OPENAI\_API\_KEY.

You can easily map ENV variables to secrets and to global variables using the enviroment configuration entry.

This is an example of passing the OPENAI\_API\_KEY to the agent and also configuring LangSmith integration:

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

You've reached the end of the Agent Developer Guide. Well done!

