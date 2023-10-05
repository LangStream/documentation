# Get Started

You can get started with LangStream in 5 minutes or less. This guide will walk you through the steps to get LangStream running on your local machine.

This guide uses Docker to run all the components of LangStream locally. If you want to learn how to deploy a full LangStream cluster locally using minikube, see [here.](installation/get-started-minikube.md)

### Installation

1. Install the LangStream CLI:

```
brew install LangStream/langstream/langstream
```

If you are on Linux or Windows please refer to the [installation guide](installation/langstream-cli.md).

2. Run the sample application

Let's run a simple LangStream Application that implements a ChatBot using OpenAI's API.

You need to get an OpenAI API key from [here](https://beta.openai.com/).

```
export OPENAI_API_KEY=<your-openai-api-key>
langstream docker run test -app https://github.com/LangStream/langstream/tree/main/examples/applications/openai-completions -s https://github.com/LangStream/langstream/blob/main/examples/secrets/secrets.yaml
```

The first time you run the application, it will take a few minutes to download the Docker images.

3. Chat with the bot

Once the application is running, chat with the bot using the LangStream CLI:

```
langstream gateway chat test -cg consume-output -pg produce-input -p sessionId=$(uuidgen)
```

> **NOTE**
> If you see an 'application not found' error, LangStream is still not ready to accept the connections. Wait a few seconds and try again.

With LangStream installed and your environment set up, you're ready to build an application.

### Your first application

Here are a few ways to get started building LangStream applications:

* [Build a sample application](building-applications/build-a-sample-app.md) to quickly create an OpenAI query with LangStream.
* [Set up your development environment](building-applications/development-environment.md) and learn how to build the needed manifests
* [Install the VSCode extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) and use the provided starter applications & agent snippets
