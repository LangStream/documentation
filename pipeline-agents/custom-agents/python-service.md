# Python service

A Python agent is a Python application that is run as a service and it is supposed to expose it using HTTP.&#x20;

The Python application needs to follow a specific directory structure for this agent to successfully run.&#x20;

Within the “application” directory, create a directory named “python”.&#x20;

Within that directory, place the .py file with the class that will be the entry point.

The directory will look something like this:

```
|- Project directory
    |- application
        |- python
            |- application.py
    |- pipeline.yaml
    |- configuration.yaml
|- (optional) secrets.yaml
```

For more on developing custom Python source agents, see the [Agent Developer Guide.](../agent-developer-guide/)

### Example

Example python esrvice located at ./application/python/example.py:

```python

from langstream import Service

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes
import uvicorn

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/chain",
    )

class ChatBotService(Service):

    def main(self):
      uvicorn.run(app, host="0.0.0.0", port=8000)
```

Configure the agent to use the python class in pipeline.yaml:

```yaml
module: default
name: "Basic LangServe application"
pipeline:
  - name: "Start LangServe"
    id: langserve-service
    type: "python-service"
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

It is important that the service listens on port 8000, that is a special port that is mapped to the LangStream service.
The LangStream operator will make sure that the service is reachable from the LangStream Gateway API Service.

Then you can expose your service using a gateway of type "service".

```yaml
gateways:
  - id: chatbot
    type: service
    service-options:
      agent-id: langserve-service
```

### Topics

**Input**

* None

**Output**

* None
