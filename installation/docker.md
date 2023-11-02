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

Using the [LangStream CLI](../installation/langstream-cli.md), you can run your application directly:

```bash
langstream docker run super-cool-app -app ./application  -s ./secrets.yaml
```

This command starts a docker container using the same version of the CLI.

The container by default runs all the LangStream components, a Kafka Broker, and an S3 service (using [Minio](https://min.io/docs/minio/kubernetes/upstream/index.html)).

The docker container exposes the Control Plane on the default port (`8090`) and the API Gateway on the default port (`8091`),
so you can run most of the CLI commands against the local container, especially the commands to interact with the API Gateway. See this [section](#connect-to-the-docker-application) to learn more.

Note that one of the two port is not available, the command will fail. Parallel executions of local run is not supported. 

When you kill the application with Ctrl-C, the environment is automatically disposed of.
If you need to persist your topics or the S3 environment, then you have to build your own instance.yaml file and pass it using the "-i" flag.

```bash
langstream docker run super-cool-app -app ./application \
-i ./instance.yaml \
-s ./secrets.yaml
```

### Selecting the services to run

By default the docker container runs all the LangStream components, a Kafka Broker, and an S3 service (using Minio).

You can use the following flags to select the services to run:

* `--start-broker`: starts the Kafka broker (default is `true`)
* `--start-s3`: starts the S3 service (default is `true`)
* `--start-webservices`: starts the LangStream HTTP components (control plane and API gateway) (default is `true`)
* `--start-database`: starts an embedded vector JDBC compliant database (HerdDB) (default is `true`)
* `--start-ui`: starts and open a UI application that helps you to test the application (default is `true`)

For example, if you are using an external Apache Kafka or Pulsar broke, you don't need to start Kafka in the container and you can save local resources by not running the service.

### Running a single agent

By default the "docker run" mode runs all the agents in the application pipeline.
If you want to debug or work on a single agent you can use the `--only-agent` flag to specify the agent to run.

The id of the agent is the same id of the "executors" section in the application descriptor. You can see this id with the "langstream apps get -o yaml" command.
This id is not the id of an agent in the pipeline.yaml file, but it is the id of the physical executor. When you run your application in a Kubernetes cluster
the id would be the id of a Statefulset.

### Execution model

When you run your application in "docker run" mode, the container runs a simplified environment that doesn't need Kubernetes, but this comes with a few simplifications to the execution runtime.

In production mode on Kubernetes, the LangStream planner builds an execution plan from your pipeline files, and then it submits the execution plan to the Kubernetes cluster in the form of Statefulsets. Each Statefulset is responsible for running a single executor (one or many agents). You can configure the number of replicas for each agent in the `resources` section of the pipeline.yaml file. In docker mode, the resources configuration is ignored.

In docker mode there is only one Java process that runs all the agents, and for each agent it starts only one execution flow, like having a Statefulset with only one replica.
The resources (memory and CPU) are shared between all the agents, so if you have a lot of agents in your application you may need to increase the resources of the docker container (see [Tuning the docker container](#tuning-the-docker-container) below).

The initialisation of the assets is always performed independently from the agents that are running, for all the assets declared in the application. The deletion of the assets is not performed in this mode.

You cannot select which logs to display, as all the agents share the same output (but you can still run one agent at a time). The `langstream apps logs` command is not available in this mode.


### Tuning the docker container

As the resources are handled by docker and the JVM and the Python processes share the same resources, you may need to increase the resources of the docker container. You can use the following flags to increase the resources:

* `--memory`: the amount of memory to allocate to the docker container
* `--cpus`: the number of CPUs to allocate to the docker container
* `--docker-args`: additional arguments to pass to the docker run command

You can also customize the docker image that you want to use to run your application. By default the CLI uses the official LangStream docker image, but you can use your own image, maybe to test the same application with a different LangStream runtime version.

The following flags are available:

* `--langstream-runtime-docker-image`: the docker image to use to run the application
* `--langstream-runtime-version`: the version of the docker image to use to run the applications

If you have built [the CLI locally from the sources](../installation/build-and-install-source.md) the docker image defaults to the local docker image

You can also override the command used to launch the container, the default value is `docker`, but you can pass the `--docker-command` flag to use a different binary path.


### Connect to the docker application using the CLI
The docker container exposes the API gateway on port `8091` and the control plane on port `8090` of your local machine. 
To connect to the docker container it's highly suggested to use a special profile named `local-docker-run`.
This profile ensures you will always connect to the right endpoints.

For example, starting the chat gateway:
```bash
langstream -p local-docker-run gateway chat test chat
```

or for getting the application description:
```bash
langstream -p local-docker-run apps get test -o yaml
```

### Connect to the docker application using a Web interface

By default the CLI starts a web interface that you can use to test your application. The web interface is available at [http://localhost:8092/](http://localhost:8092/).
This interface displays:

* the application logs
* a chatbot-like interface to interact with the gateways
* a diagram of the application pipelines
* the JSON description of the application, both the logical and the physical description (execution plan)
