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

This will clone the latest code of the [project](https://github.com/LangStream/langstream) into the "langstream" folder.

```
git clone https://github.com/LangStream/langstream
```

### Build the project

This will compile source, build the cli, and install images.

```
cd langstream
./docker/build.sh
```

### Deploy a store and the control plane

{% hint style="info" %}
If you are using Minikube load the new images with the following commands:

```bash
minikube image load --overwrite langstream/langstream-deployer:latest-dev
minikube image load --overwrite langstream/langstream-control-plane:latest-dev
minikube image load --overwrite langstream/langstream-runtime:latest-dev
minikube image load --overwrite langstream/langstream-api-gateway:latest-dev
minikube image load --overwrite langstream/langstream-cli:latest-dev
```
{% endhint %}

```bash
kubectl apply -f ./helm/examples/minio-dev.yaml
helm upgrade -i langstream langstream/langstream --values helm/examples/local.yaml --wait
```

### Locate the CLI

During the build, the latest CLI has created in the "bin" folder.

```
./bin/langstream --version
```
