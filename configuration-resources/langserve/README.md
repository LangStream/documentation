---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: false
---

# Integation with LangServe applications

[LangServe](https://github.com/langchain-ai/langserve) is a popular runtime to execute LangChain applications.

LangStream natively integrates with LangServe and allows you to invoke services exposed by LangServe applications.

Use the built-in `langserve-invoke` agent to implement this integration.

This example invokes a LangServe application that exposes a service at `http://localhost:8000/chain/stream`.

```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
  - name: "output-topic"
    creation-mode: create-if-not-exists
  - name: "streaming-answers-topic"
    creation-mode: create-if-not-exists
pipeline:
  - type: "langserve-invoke"
    input: input-topic
    output: output-topic
    id: step1
    configuration:
      output-field: value.answer
      stream-to-topic: streaming-answers-topic
      stream-response-field: value
      min-chunks-per-message: 10
      debug: false
      method: POST
      allow-redirects: true
      handle-cookies: false
      url: "http://host.docker.internal:8000/chain/stream"
      fields:
        - name: topic
          expression: "value"
```


When you run the LangStream application in docker the URL is `http://host.docker.internal:8000/chain/stream` due to how docker desktop works.


To allow your LangStream application to be accessible from a UI, you have to configure a gateway:
```yaml
gateways:
  - id: chat
    type: chat
    chat-options:
      answers-topic: streaming-answers-topic
      questions-topic: input-topic
      headers:
        - value-from-parameters: session-id
```

## Starting the LangServe application locally

This is the sample code of the LangServe application:

```python
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/chain",
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
```

Start the LangServe application with the following command:

```bash
export OPENAI_API_KEY=...
pip install fastapi langserve langchain openai sse_starlette uvicorn
python example.py
```

## Starting the LangStream application locally

To run the LangStream application on docker locally:

```bash
langstream docker run -app /path/to/applicationn 
```

The LangStream UI will be running at [http://localhost:8092/](http://localhost:8092/) 