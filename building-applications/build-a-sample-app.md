# Sample App

This sample application takes minimal configuration to get you started on your LangStream journey.

1. Complete the LangStream installation steps in [Get Started.](../get-started.md)
2. Pass your OpenAI credentials to /tmp/secrets.yaml:

```bash
export AZURE_URL=xx
export OPEN_AI_ACCESS_KEY=xx

echo """
secrets:
  - name: open-ai
    id: open-ai
    data:
      url: $AZURE_URL
      access-key: $OPEN_AI_ACCESS_KEY
""" > /tmp/secrets.yaml
```

3. Create a project folder in examples/applications:

```
mkdir sample-app && cd sample-app
touch configuration.yaml instance.yaml
mkdir application && cd application
touch pipeline.yaml gateways.yaml
```

It should look something like this:

```
|- sample-app
|- application
    |- pipeline.yaml
    |- gateways.yaml
|- instance.yaml
|- configuration.yaml
|- (optional) secrets.yaml
```

4. Populate the yaml files:

Instance.yaml declares the application's processing infrastructure, including where streaming and compute take place.

```yaml
instance:
  streamingCluster:
    type: "kafka"
    configuration:
      admin:
        bootstrap.servers: my-cluster-kafka-bootstrap.kafka:9092
```

Configuration.yaml contains auth information.

```yaml
configuration:
  resources:
    - type: open-ai-configuration
      name: OpenAI Azure configuration
      configuration:
        url: "{{{ secrets.open-ai.url }}}"
        access-key: "{{{ secrets.open-ai.access-key }}}"
        provider: azure
  dependencies: []
```

Gateways.yaml contains API gateways for communicating with your application.

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

Pipeline.yaml contains the chain of agents that makes up your program, and the input and output topics that they communicate with.

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
    configuration:
      model: "gpt-35-turbo" # This needs to be set to the model deployment name, not the base name
      completion-field: "value"
      messages:
        - role: user
          content: "What can you tell me about {{% value}} ?"
```

Save all your files.

5. Deploy your application:

```bash
langstream apps deploy sample-app -app ./application -i ./instance.yaml -s /tmp/secrets.yaml
langstream apps get sample-app
```

Result:

```bash
packaging app: /Users/mendon.kissling/sample-app/./application
app packaged
deploying application: sample-app (0 KB)
application sample-app deployed
ID               STREAMING        COMPUTE          STATUS           EXECUTORS        REPLICAS
sample-app       kafka            kubernetes       DEPLOYING        0/0
```

6. Ensure your app is running - a Kubernetes pod should be deployed with your application, and STATUS will change to DEPLOYED.
7. Send a query to OpenAI about "Barack Obama":

```bash
session="$(uuidgen)"
langstream gateway produce sample-app produce-input -p sessionId="$session" -v "Barack Obama"
langstream gateway consume sample-app consume-output -p sessionId="$session"
```

```result
{"status":"OK","reason":null}
Connected to ws://localhost:8091/v1/consume/default/sample-app/consume-output?&param:sessionId=0DB21293-0E77-4C89-8185-4F8D4C49E7C7&
{"record":{"key":null,"value":"Barack Obama is an American politician and attorney who served as the 44th President of the United States from 2009 to 2017. He was born in Honolulu, Hawaii, in 1961 to a Kenyan father and an American mother. Obama is known for his policies on healthcare reform, economic stimulus, foreign policy, civil rights, and environmental regulation. He is also famous for his inspiring and charismatic speeches and his ability to connect with people from all backgrounds. Before his presidency, Obama served as a community organizer, civil rights attorney, and senator for the state of Illinois. He is also a published author, with several books to his name, including his memoir \"Dreams from My Father\" and \"The Audacity of Hope.\"","headers":{"langstream-client-session-id":"0DB21293-0E77-4C89-8185-4F8D4C49E7C7"}},"offset":"eyJvZmZzZXRzIjp7IjAiOiI0In19"}
```
