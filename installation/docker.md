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

# Running LangStream on Docker

### Why Docker?

LangStream is designed to be a cloud-native application. This means that it is designed to run on Kubernetes and to be deployed on a cloud environment.
But sometimes you want to get started quickly and you don't need the full power of Kubernetes to see your Generative AI application in action.

This is why the LangStream CLI provides a simple way to run your application locally using Docker.

### Running your application on docker

Using the [LangStream CLI](../installation/langstream-cli.md) you can run your application directly:

```bash
 langstream docker run super-cool-app -app ./application  -s ./secrets.yaml
```

This commands starts a docker container using the same version of the CLI.

The container by defaults runs all the LangStream components, a Kafka Broker and a S3 service (using Minio).

The docker container exposes the Control Plane on the default port (8090) and the API Gateway on the default port (8091),
this way you can run most of the CLI commands against the local container, especially the commands to interact with the gateway.

When you kill the application with Ctrl-C the environment is automatically disposed.
If you need to persist your topics or the S3 environment then you have to build your own instance.yaml file and pass it using the "-i" flag.

### Selecting the services to run

By default the docker container runs all the LangStream components, a Kafka Broker and a S3 service (using Minio).

You can use the following flags to select the services to run:

* --start-broker true|false: starts the Kafka broker
* --start-s3 true|false: starts the S3 service
* --start-webservices true|false: starts the LangStream HTTP components (control plane and API gateway)

For instance if you are using an external Apache Kafka or Pulsar broker you don't need to start Kafka in the container and you can save local resources.

### Running a single agent

By default the "docker run" mode runs all the agents in the application.
If you want to debug or work on a single agent you can use the "--only-agent" flag to specify the agent to run.

The id of the agent is the same id of the "executors" section in the application descriptor that you can see in the "langstram apps get -o yaml" command.
Basically it is not the id of an agent in the pipeline.yaml file but it is the id of a pyshical executor. When you run your application in a Kubernetes cluster
the id would be the id of a Statefulset.

### Execution model

When you run your application in "docker run" mode, the container runs a simplified enviroment that doesn't need Kubernetes, but this comes with a fews simplifications to the execution runtime.

In production mode, on Kubernetes, the LangStream planner builds and execution plan from your pipeline files, and then it submits the execution plan to the Kubernetes cluster in the form of Statefulsets. Each Statefulset is responsible to run a single agent and you can usually configure the number of replicas for each agent in the pipeline file, in the "resources" section.

But in docker mode there is only one Java process that runs all the agents, and for each agent it starts only one execution flow, like having a statefulset with only one replica.
The resources (JVM and CPU) are shared between all the agents, so if you have a lot of agents in your application you may need to increase the resources of the docker container.

The initialisation of the assets is always performed, for all the assets declared in the application, independently from the agents that are running. This is because the assets are shared between all the agents, even if they are declared in some pipeline file.

You cannot select the logs to show, as all the agents share the same output (but you can still run one agent at a time). The "langstream apps logs" command is not available in this mode.


### Tuning the docker container

As the resources are handled by docker and the JVM and the Python processes share the same resources, you may need to increase the resources of the docker container. You can use the following flags to increase the resources:

* --memory: the amount of memory to allocate to the docker container
* --cpus: the number of CPUs to allocate to the docker container
* --docker-args: additional arguments to pass to the docker run command

You can also customizer the docker image that you want to use to run your application. By default the CLI uses the official LangStream docker image, but you can use your own image, maybe you want to test the same application with a different LangStream runtime version.

The following flags are available:

* --langstream-runtime-docker-image: the docker image to use to run the application
* --langstream-runtime-version: the version of the docker image to use to run the applications

If you have built [the CLI locally from the sources](../installation/build-and-install-source.md) the docker image defaults to the local docker image

You can also override the command used to launch the container, the default value is "docker", but you can use the "--docker-command" command to override it.
