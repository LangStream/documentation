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
* Python 3.11+ and PIP

### Clone the project

This will clone the latest code of the [project](https://github.com/LangStream/langstream) into the "langstream" folder.

```
git clone https://github.com/LangStream/langstream
```

### Build the project

This will compile source, build the cli, and install images.

```
cd langstream
pip install -r requirements.txt
./docker/build.sh
```

### Deploy the LangStream runtime

{% hint style="info" %}
If you are using Minikube load the new images with the following command:

```bash
dev/deploy-minikube.sh
```
{% endhint %}

You also need to install MinIO for local testing:

```bash
kubectl apply -f ./helm/examples/minio-dev.yaml
```

Then you can install the LangStream runtime:

```bash
helm install -i langstream langstream/langstream --values helm/examples/local.yaml --wait
```

You can find a script that does everything for you and also starts a Kafka broker:

```bash
dev/start-local.sh
```


### Locate the CLI

During the build, the latest CLI has created in the "bin" folder.

```
./bin/langstream --version
```

Please note that this CLI uses the conf/cli.yaml file and it does not behave the same way as the CLI installed with brew, that uses the $HOME/.langstream/config file with a different format.