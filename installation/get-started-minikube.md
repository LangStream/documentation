# Minikube

To create a LangStream cluster locally, it's recommended to use [minikube](https://minikube.sigs.k8s.io/docs/start/) - setting 4 CPUs is highly recommended.
`mini-langstream` comes in help for installing and managing your local cluster.


## Install mini-langstream

mini-langstream requires the following commands to be already installed:
- Docker
- Minikube
- Helm
- Kubectl
- LangStream CLI


{% hint style="info" %}
If you install mini-langstream using Brew, all the dependencies are automatically installed.
{% endhint %}

MacOS:

```bash
brew install LangStream/langstream/mini-langstream
```

Unix:

```bash
curl -Ls "https://raw.githubusercontent.com/LangStream/langstream/main/mini-langstream/get-mini-langstream.sh" | bash
```

## Start the cluster

mini-langstream will do all the setup for you, in particular:
- start `minikube` in a dedicated context
- deploy LangStream components using `helm`
- run a stateful Kafka broker as docker container
- run a stateful s3-compatible storage (MinIO) as docker container
- forward the control plane and API Gateways ports locally
- create a dedicated LangStream CLI profile to interact with the cluster
- wrap all the common k8s tools to inspect the cluster (`mini-langstream kubectl`, `mini-langstream helm`, `mini-langstream k9s`)

1. Start or ensure the cluster is running:

```bash
mini-langstream start
```

2. Try to use the CLI:

```bash
mini-langstream cli apps list
```
3. Deploy an application:

```bash
export OPENAI_API_KEY=<your-openai-api-key>
mini-langstream cli apps deploy my-app -app https://github.com/LangStream/langstream/tree/main/examples/applications/openai-completions -s https://github.com/LangStream/langstream/blob/main/examples/secrets/secrets.yaml
```

To delete all the storage and stop the cluster:

```bash
mini-langstream delete
```


## Your first application

Here are a few ways to get started building LangStream applications:

* [Build a sample application](../building-applications/build-a-sample-app.md) to quickly create an OpenAI query with LangStream.
* [Set up your development environment](../building-applications/development-environment.md) and learn how to build the needed manifests
* [Install the VSCode extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) and use the provided starter applications & agent snippets
