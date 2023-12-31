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

#### Template variables in YAML files


In the pipeline definion you can reference values from the instance and secrets files. For example, if you have a secret.yaml file with the following content:

```yaml
secrets:
  - id: open-ai
    data:
      access-key: "${OPEN_AI_ACCESS_KEY:-}"
      url: "${OPEN_AI_URL:-}"
      provider: "${OPEN_AI_PROVIDER:-openai}"
      embeddings-model: "${OPEN_AI_EMBEDDINGS_MODEL:-text-embedding-ada-002}"
      chat-completions-model: "${OPEN_AI_CHAT_COMPLETIONS_MODEL:-gpt-3.5-turbo}"
  - id: kafka
    data:
      username: "${KAFKA_USERNAME:-}"
      password: "${KAFKA_PASSWORD:-}"
      tenant: "${KAFKA_TENANT:-}"
      bootstrap-servers: "${KAFKA_BOOTSTRAP_SERVERS:-}"
```

You can reference the values in the instance.yaml file like this:

```yaml
instance:
  globals:
     table-name: "my-table"
     topic-name: "topic-1-staging"
  streamingCluster:
    type: "kafka"
    configuration:
      admin:
        bootstrap.servers: "${ secrets.kafka.bootstrap-servers }"
        security.protocol: SASL_SSL
        sasl.jaas.config: "org.apache.kafka.common.security.plain.PlainLoginModule required username='${ secrets.kafka.username }' password='${ secrets.kafka.password }';"
        sasl.mechanism: PLAIN
        session.timeout.ms: "45000"
```

And in the pipeline and in the configuration manifests you can refer both to secrets and to instance values:

This is a pipeline.yaml file:

```yaml
name: "Write to AstraDB"
topics:
  - name: "${globals.topic-name}"
    creation-mode: create-if-not-exists
assets:
  - name: "documents-table"
    asset-type: "cassandra-table"
    creation-mode: create-if-not-exists
    config:
      table-name: "${globals.table-name}"
      keyspace: "documents"
      datasource: "AstraDatasource"
      .......
pipeline:
  - name: "Write to Vector database"
    type: "vector-db-sink"
    input: "chunks-topic"
    configuration:
      datasource: "AstraDatasource"
      table-name: "${globals.table-name}"
      ....
```


This is a configuration.yaml file:

```yaml
configuration:
  resources:
  - type: "open-ai-configuration"
    name: "OpenAI Azure configuration"
    configuration:
      url: "${ secrets.open-ai.url }"
      access-key: "${ secrets.open-ai.access-key }"
      provider: "${ secrets.open-ai.provider }"
  - type: "datasource"
    name: "AstraDatasource"
    configuration:
      service: "astra"
      clientId: "${ secrets.astra.clientId }"
      secret: "${ secrets.astra.secret }"
      secureBundle: "${ secrets.astra.secureBundle }"
      database: "${ secrets.astra.database }"
      token: "${ secrets.astra.token }"
      environment: "${ secrets.astra.environment }"
```


 For example, in the secrets.yaml file you can see the following syntax:

```yaml
access-key: "${ secrets.open-ai.access-key }"

#### Mustache templates in YAML files

Some agents, like the **ai-chat-completions** agent, require a configuration that is a Mustache template.
For example:

```yaml
pipeline:
    ....
  - name: "ai-chat-completions"
    type: "ai-chat-completions"

    configuration:
      .....
      messages:
        - role: system
          content: |
              An user is going to perform a questions, he documents below may help you in answering to their questions.
              Please try to leverage them in your answer as much as possible.
              Take into consideration that the user is always asking questions about the LangStream project.
              If you provide code or YAML snippets, please explicitly state that they are examples.
              Do not provide information that is not related to the LangStream project.
            
              Documents:
              {{# value.related_documents}}
              {{{ text}}}
              {{/ value.related_documents}}
        - role: user
          content: "{{ value.question}}"
```


#### Using ENV variables in secrets and instance files

As you can see in the examples in the secrets.yaml and the instance.yaml files, you can use environment variables to define the values of the secrets and instance values. This is useful when you want to run the same application in different environments without using different secrets and instance files. For example, you can define the following environment variables:

```bash
export OPEN_AI_ACCESS_KEY="my-access-key"
export OPEN_AI_PROVIDER="openai"
```

In this case the secrets file is dynamically populated with the values of the environment variables. You can also use the same technique to define the values of the instance file. For example:

```yaml
secrets:
  - id: open-ai
    data:
      access-key: "my-access-key"
      url: ""
      provider: "openai"
      embeddings-model: "text-embedding-ada-002"
      chat-completions-model: "gpt-3.5-turbo"
```

The syntax for referencing environment variables is like in the Linux bash shell. For example, if you want to reference the value of the OPEN_AI_EMBEDDINGS_MODEL environment variable you can use the following syntax:

```yaml
embeddings-model: "${OPEN_AI_EMBEDDINGS_MODEL:-text-embedding-ada-002}"
```

Then you run the "langstream docker run", or "langstream apps deploy" commands the value for the OPEN_AI_EMBEDDINGS_MODEL environment variable is replaced with the current value for the ENV variable OPEN_AI_EMBEDDINGS_MODEL, otherwise it is replaced with the default value "text-embedding-ada-002".

