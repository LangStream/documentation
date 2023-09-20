# Sample App

This sample application takes minimal configuration to get you started on your LangStream journey.

1. Complete the LangStream installation steps in [Get Started.](../get-started.md)
2. Pass your OpenAI credentials as an [ENV variable](../building-applications/yaml-templates.md):

```bash
export OPEN_AI_ACCESS_KEY=xxxxx
```

3. Create a project folder in examples/applications:

```
mkdir sample-app && cd sample-app
touch secrets.yaml
mkdir application && cd application
touch chatbot.yaml gateways.yaml configuration.yaml
```

It should look something like this:

```
|- sample-app
|- application
    |- chatbot.yaml
    |- gateways.yaml
    |- configuration.yaml
|- secrets.yaml
```

4. Populate the yaml files:

**configuration.yaml** contains information about external services (in this case the OpenAI API).

```yaml
configuration:
  resources:
    - type: open-ai-configuration
      name: OpenAI Azure configuration
      configuration:       
        access-key: "{{{ secrets.open-ai.access-key }}}"
        provider: openai
```

**secrets.yaml** contains the definition of secrets used by your application.

```yaml
secrets:
  - id: open-ai
    data:
      access-key: "${OPEN_AI_ACCESS_KEY:-}"
```

**gateways.yaml** contains API gateways for communicating with your application.

```yaml
gateways:
  - id: produce-input
    type: produce
    topic: input-topic
    parameters:
      - sessionId
    produceOptions:
      headers:
        - key: langstream-client-session-id
          valueFromParameters: sessionId

  - id: consume-output
    type: consume
    topic: output-topic
    parameters:
      - sessionId
    consumeOptions:
      filters:
        headers:
          - key: langstream-client-session-id
            valueFromParameters: sessionId
```

**chatbot.yaml** contains the chain of agents that makes up your program, and the input and output topics that they communicate with.

```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
  - name: "output-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    input: "input-topic"
    output: "output-topic"
    errors:
      on-failure: skip
    configuration:
      model: "gpt-3.5-turbo"
      completion-field: "value"
      messages:
        - role: user
          content: "What can you tell me about {{% value}} ?"
```

Save all your files.

5. Deploy your application:

```bash
langstream docker run sample-app -app ./application  -s ./secrets.yaml
```

Now you should see the docker container starting and then running the application.

6. Ensure your app is running - a docker container should be running:

You can now open a new terminal an inspect the status of the application:

```bash
docker ps
```
Result:

```bash
CONTAINER ID   IMAGE                                                 COMMAND                  CREATED         STATUS        PORTS                                                                                                                                  NAMES
421bb7e082bb   ghcr.io/langstream/langstream-runtime-tester:0.0.21   "/app/entrypoint.sh"     2 minutes ago   Up 2 minutes   0.0.0.0:8090-8091->8090-8091/tcp

```

And youn can use the CLI to inspect the status of the application

```bash
langstream apps get sample-app
```

Result:

```bash
ID          STREAMING   COMPUTE     STATUS      EXECUTORS   REPLICAS  
sample-app  kafka       kubernetes  DEPLOYED    1/1         1/1   
```

For the LangStream CLI the application appears to be running on "kubernetes", even if you are using the docker mode, this is because
the docker container emulates partially the Kubernetes environment.

```bash
langstream apps get sample-app -o yaml
```

Result:

```yaml
---
application-id: "sample-app"
application:
  resources:
    OpenAI Azure configuration:
      id: null
      name: "OpenAI Azure configuration"
      type: "open-ai-configuration"
      configuration:
        access-key: "{{{ secrets.open-ai.access-key }}}"
        provider: "openai"
  modules:
  - id: "default"
    pipelines:
    - id: "chatbot"
      module: "default"
      name: null
      resources:
        parallelism: 1
        size: 1
      errors:
        retries: 0
        on-failure: "fail"
      agents:
      - id: "chatbot-ai-chat-completions-1"
        name: "ai-chat-completions"
        type: "ai-chat-completions"
        input:
          connectionType: "TOPIC"
          definition: "input-topic"
          enableDeadletterQueue: false
        output:
          connectionType: "TOPIC"
          definition: "output-topic"
          enableDeadletterQueue: false
        configuration:
          completion-field: "value"
          messages:
          - content: "What can you tell me about {{% value}} ?"
            role: "user"
          model: "gpt-35-turbo"
        resources:
          parallelism: 1
          size: 1
        errors:
          retries: 0
          on-failure: "fail"
    topics:
    - name: "output-topic"
      config: null
      options: null
      keySchema: null
      valueSchema: null
      partitions: 0
      implicit: false
      creation-mode: "create-if-not-exists"
      deletion-mode: "none"
    - name: "input-topic"
      config: null
      options: null
      keySchema: null
      valueSchema: null
      partitions: 0
      implicit: false
      creation-mode: "create-if-not-exists"
      deletion-mode: "none"
  gateways:
    gateways:
    - id: "produce-input"
      type: "produce"
      topic: "input-topic"
      authentication: null
      parameters:
      - "sessionId"
      produceOptions:
        headers:
        - key: "langstream-client-session-id"
          value: null
          valueFromParameters: "sessionId"
          valueFromAuthentication: null
      consumeOptions: null
      chat-options: null
      events-topic: null
    - id: "consume-output"
      type: "consume"
      topic: "output-topic"
      authentication: null
      parameters:
      - "sessionId"
      produceOptions: null
      consumeOptions:
        filters:
          headers:
          - key: "langstream-client-session-id"
            value: null
            valueFromParameters: "sessionId"
            valueFromAuthentication: null
      chat-options: null
      events-topic: null
  instance:
    streamingCluster:
      type: "kafka"
      configuration:
        admin:
          bootstrap.servers: "localhost:9092"
    computeCluster:
      type: "kubernetes"
      configuration: {}
    globals: null
status:
  status:
    status: "DEPLOYED"
    reason: null
  executors:
  - id: "chatbot-ai-chat-completions-1"
    status:
      status: "DEPLOYED"
      reason: null
    replicas:
    - id: "docker"
      status: "RUNNING"
      agents:
      - agent-id: "topic-source"
        agent-type: "topic-source"
        component-type: "SOURCE"
        info:
          topic: "input-topic"
      - agent-id: "chatbot-ai-chat-completions-1"
        agent-type: "ai-chat-completions"
        component-type: "PROCESSOR"
      - agent-id: "topic-sink"
        agent-type: "topic-sink"
        component-type: "SINK"
        info:
          topic: "output-topic"

```


7. Send a query to OpenAI about "Italian pizza":

```bash
langstream gateway chat sample-app -cg consume-output -pg produce-input -p sessionId=$(uuidgen)
```

At the prompt ask about "Italian pizza" and see the results


