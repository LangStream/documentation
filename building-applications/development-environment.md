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

# Development Environment

A LangStream application is composed of multiple yaml manifests. Each manifest complements the others to create a data processing environment. You will typically use the [LangStream CLI](../installation/langstream-cli.md) to interact with the Kubernetes control plane.&#x20;

Your development environment should follow a specific folder structure:

* At the root there should be instance.yaml and optionally a secrets.yaml.
* The root should also contain a directory for the application files. We typically name this “application”.
* The “application” directory should contain a pipeline.yaml and optionally a configuration.yaml.

The hierarchy should look like this:

```
|
|- application
    |- pipeline.yaml
    |- (optional) configuration.yaml
|- instance.yaml
|- (optional) secrets.yaml
```

{% hint style="info" %}
Want to get started a little quicker? Check out the [LangStream VSCode Extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) for pre-made applications and agent code snippets.
{% endhint %}

#### Application directory

This is referred to as the “application directory” because the main pipeline and its configuration are declared within.

* pipeline.yaml: this is the declaration of topics and pipeline steps. It is required. [Learn more about building pipelines.](../pipeline-agents/agent-messaging.md)
* configuration.yaml: this is the declaration of additional services a step in the pipeline depends on. It is optional. [Learn more about configurations.](configuration.md)

#### Instance.yaml

The instance is a declaration of the application’s processing infrastructure. This includes where “streaming” is processed and where “compute” takes place. This is a required value. [Learn more about instances.](instances.md)

Typically the values for an instance are specific to the environment running the application. As you promote the application off of your desktop to higher environments, other instance files may be needed. In this case, it is recommended to add a suffix to the file name, representing the environment it is configured for. A few examples:

Environment: local

Filename: instance-local.yaml


Environment: staging

Filename: instance-staging.yaml


Environment: production

Filename: instance-production.yaml

#### Secrets.yaml

This is a holder for secrets used within pipeline steps, configuration dependencies, and instance declarations. It is an optional value. Secrets are held separately to create a separation of information. It’s not a good practice to hard code tokens in pipeline manifests. Instead, include a pointer to a secret that is managed in different ways. [Learn more about secrets.](secrets.md)


#### Template variables in YAML files

{% hint style="info" %}
All the yaml files are processed through a [mustache template engine](https://mustache.github.io/). Therefore, you can reference values interchangeably between files. Refer to [mustache documentation](https://mustache.github.io/mustache.5.html) or [this example site](https://www.tsmean.com/articles/mustache/the-ultimate-mustache-tutorial/) to learn more about templating.
{% endhint %}


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
        bootstrap.servers: "{{{ secrets.kafka.bootstrap-servers }}}"
        security.protocol: SASL_SSL
        sasl.jaas.config: "org.apache.kafka.common.security.plain.PlainLoginModule required username='{{{ secrets.kafka.username }}}' password='{{{ secrets.kafka.password }}}';"
        sasl.mechanism: PLAIN
        session.timeout.ms: "45000"
```

And in the pipeline and in the configuration manifests you can refer both to secrets and to instance values:

This is a pipeline.yaml file:

```yaml
name: "Write to AstraDB"
topics:
  - name: "{{{globals.topic-name}}}"
    creation-mode: create-if-not-exists
assets:
  - name: "documents-table"
    asset-type: "cassandra-table"
    creation-mode: create-if-not-exists
    config:
      table-name: "{{{globals.table-name}}}"
      keyspace: "documents"
      datasource: "AstraDatasource"
      .......
pipeline:
  - name: "Write to Vector database"
    type: "vector-db-sink"
    input: "chunks-topic"
    configuration:
      datasource: "AstraDatasource"
      table-name: "{{{globals.table-name}}}"
      ....
```


This is a configuration.yaml file:

```yaml
configuration:
  resources:
  - type: "open-ai-configuration"
    name: "OpenAI Azure configuration"
    configuration:
      url: "{{{ secrets.open-ai.url }}}"
      access-key: "{{{ secrets.open-ai.access-key }}}"
      provider: "{{{ secrets.open-ai.provider }}}"
  - type: "datasource"
    name: "AstraDatasource"
    configuration:
      service: "astra"
      clientId: "{{{ secrets.astra.clientId }}}"
      secret: "{{{ secrets.astra.secret }}}"
      secureBundle: "{{{ secrets.astra.secureBundle }}}"
      database: "{{{ secrets.astra.database }}}"
      token: "{{{ secrets.astra.token }}}"
      environment: "{{{ secrets.astra.environment }}}"
```

{% hint style="warning" %}
In the Mustache language the syntax with double curly brances implies that the value is escaped. If you want to use the value as is, without escaping it, you need to use triple curly braces.
{% endhint %}

 For example, in the secrets.yaml file you can see the following syntax:

```yaml
access-key: "{{{ secrets.open-ai.access-key }}}"
```

The value of the access-key is not escaped. If you want to escape the value you can use the following syntax:

```yaml
access-key: "{{ secrets.open-ai.access-key }}"
```
but this may lead to unexpected results. So the suggestion is to always use the triple curly braces syntax.

#### Nesting mustache template syntax

Some agents, like the **ai-chat-completions** agent, require a configuration that is a Mustache template.
In this case you can must add a percent character after the duoble (or triple) curly braces. For example:

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
              {{%# value.related_documents}}
              {{{% text}}}
              {{%/ value.related_documents}}
        - role: user
          content: "{{{% value.question}}}"
```

If you don't add the percent character the Mustache syntax is processed by the preprocesing step that applies the secrets and global variables.


#### Using ENV variables in secrets and instance files

As you can see in the example in the secrets.yaml and in the instance.yaml files you can use environment variables to define the values of the secrets and instance values. This is useful when you want to run the same application in different environments without using different secrets and instance files. For example, you can define the following environment variables:

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

