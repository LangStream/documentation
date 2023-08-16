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

# Build and install (source)

LangStream uses Maven as its build system. When the below script is run the project source will be tested, compiled, and the container images will be built.

### Requirements

* Docker
* Java 17
* Git

### Clone the project

This will clone the latest code of the project into the "streaming-gen-ai" folder.

```
git clone https://datastax.com/datastax/streaming-gen-ai
```

### Build the project

This will compile source, build the cli, and install images.

```
cd streaming-gen-ai
./docker/build.sh
```

### Deploy a store and the control plane

{% hint style="info" %}
If you are using Minikube load the new images with the following commands:

```bash
minikube image load datastax/sga-cli:latest-dev
minikube image load datastax/sga-deployer:latest-dev
minikube image load datastax/sga-control-plane:latest-dev
minikube image load datastax/sga-runtime:latest-dev
minikube image load datastax/sga-api-gateway:latest-dev
```
{% endhint %}

```bash
kubectl apply -f ./helm/examples/minio-dev.yaml
helm upgrade -i sga helm/sga --values ./helm/examples/local.yaml --wait
```

### Locate the CLI

During the build, the latest CLI has created in the "bin" folder.

```
./bin/sga-cli --version
```
