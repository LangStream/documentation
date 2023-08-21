# Get Started

To create a LangStream control plane, you will need [kubectl](https://kubernetes.io/docs/reference/kubectl/), [helm cli](https://helm.sh/docs/intro/install/), and a running K8s cluster (a default 4 CPU [minikube](https://minikube.sigs.k8s.io/docs/start/) is fine).

### Installation

1. Start a minikube:

```bash
minikube start
```

2. Install MinIO for local testing:

```
kubectl apply -f https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/minio-dev.yaml
```

3. Deploy Langstream from the Helm repository:

```bash
helm repo add langstream https://langstream.github.io/charts
helm repo update
helm upgrade \
    -i langstream \
    -n langstream \
    --create-namespace \
    --wait \
    --values https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/simple.yaml \
    langstream/langstream
```

&#x20; 4\. Open the control-plane and api-gateway ports (in separate terminals):

Control plane:

```bash
kubectl -n langstream port-forward svc/langstream-control-plane 8090:8090 &
```

API gateway:

```bash
kubectl -n langstream port-forward svc/langstream-api-gateway 8091:8091 &
```

### Environment setup

1. Port forward minio in a separate terminal:

```
kubectl port-forward pod/minio 9000 9090 -n minio-dev  
```

2. Install Kafka:

```
kubectl create namespace kafka 
kubectl create -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka 
kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-persistent-single.yaml -n kafka
```

3. Install the LangStream CLI with brew. Other options are available [here](installation/langstream-cli.md).

```bash
brew tap LangStream/langstream
brew install langstream
```

With LangStream installed and your environment set up, you're ready to build an application.

### Your first application

Here are a few ways to get started building LangStream applications:

* [Set up your development environment](building-applications/development-environment.md) and learn how to build the needed manifests
* [Install the VSCode extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) and use the provided starter applications & agent snippets
