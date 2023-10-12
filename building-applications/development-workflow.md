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

# Development Workflow

### Selecting an enviroment



### Step 1. Running your application on docker

Using the [LangStream CLI](../installation/langstream-cli.md) you can run your application directly:

```bash
 langstream docker run super-cool-app -app ./application  -s ./secrets.yaml
```

In this case the instance.yaml file is optional, if you don't provide it, the CLI will use a default configuration.
The CLI starts a docker container, using the official LangStream docker images, of the same version of the CLI.

The container by default runs all the LangStream components, a Kafka Broker, an S3 service (MinIO) and an embedded vector database (HerdDB).
This is ideal for testing your application locally.

The docker container exposes the Control Plane on the default port (`8090`) and the API Gateway on the default port (`8091`),
so you can run most of the CLI commands against the local container, especially the commands to interact with the API Gateway.

When you kill the application with Ctrl-C, the environment is automatically disposed of.
If you need to persist your topics or the S3 environment, then you have to build your own instance.yaml file and pass it using the "-i" flag.

Please refer to the [LangStream Docker](../installation/docker.md) documentation for more details about the `docker run` command.


### Step 2. Deploy your application on a LangStream cluster

The CLI allows you to deploy and manage applications from your local environment.
You can also use the VSCode extension to create and manage applications on a local or remote cluster.

This approach works well if you need to use a cloud enviroment or a SaaS service or if you need to leverage some advanced features like scaling or resource management.

Using the [LangStream CLI](../installation/langstream-cli.md), a typical workflow is:

1.  Configure the CLI to connect to the remote cluster and set the tenant.
    If you are using a local minikube cluster, then this is not necessary, you can use the default configuration.
    If you are using a remote cluster, you have to configure the credentials, the tenant name, and the control plane address.
   
2.  When ready, deploy your application:

    ```bash
    langstream apps deploy super-cool-app -app ./application -i ./instance.yaml  -s ./secrets.yaml
    ```
3.  Watch the progress of the deployment by watching the logs:

    ```bash
    langstream apps logs "super-cool-app"
    ```
