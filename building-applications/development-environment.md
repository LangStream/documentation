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

Filename: instance-local.yaml\


Environment: staging

Filename: instance-staging.yaml



Environment: production

Filename: instance-production.yaml

#### Secrets.yaml

This is a holder for secrets used within pipeline steps, configuration dependencies, and instance declarations. It is an optional value. Secrets are held separately to create a separation of information. It’s not a good practice to hard code tokens in pipeline manifests. Instead, include a pointer to a secret that is managed in different ways. [Learn more about secrets.](secrets.md)

{% hint style="info" %}
All the yaml files are processed through a [mustache template engine](https://mustache.github.io/). Therefore, you can reference values interchangeably between files. Refer to [mustache documentation](https://mustache.github.io/mustache.5.html) or [this example site](https://www.tsmean.com/articles/mustache/the-ultimate-mustache-tutorial/) to learn more about templating.
{% endhint %}
