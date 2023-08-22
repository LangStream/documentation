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

# Kubernetes

LangStream container images are available on Docker Hub. Current images can be deployed to Kubernetes. The control plane is made up of the following images:

* [datastax/langstream-deployer](https://gallery.ecr.aws/y3i6u2n7/datastax-public/langstream-deployer)
* [datastax/langstream-control-plane](https://gallery.ecr.aws/y3i6u2n7/datastax-public/langstream-control-plane)
* [datastax/langstream-runtime](https://gallery.ecr.aws/y3i6u2n7/datastax-public/langstream-runtime)
* [datastax/langstream-api-gateway](https://gallery.ecr.aws/y3i6u2n7/datastax-public/langstream-api-gateway)
* [datastax/langstream-cli](https://gallery.ecr.aws/y3i6u2n7/datastax-public/langstream-cli)

### Quick Start

To create a LangStream control plane, you will need [kubectl](https://kubernetes.io/docs/reference/kubectl/), [helm cli](https://helm.sh/docs/intro/install/), and a running K8s cluster.

```bash
kubectl apply -f https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/minio-dev.yaml
helm repo add langstream https://datastax.github.io/langstream
helm repo update
helm upgrade \
    -i langstream \
    -n langstream \
    --create-namespace \
    --wait \
    --values https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/simple.yaml \
    langstream/langstream
```

#### Open the control-plane and api-gateway ports (in separate terminals)

Control plane:

```bash
kubectl -n langstream port-forward svc/langstream-control-plane 8090:8090 &
```

API gateway:

```bash
kubectl -n langstream port-forward svc/langstream-api-gateway 8091:8091 &
```

### Your first application

Here are a few ways to get started building LangStream applications:

* [Set up your development environment](building-applications/development-environment.md) and learn how to build the needed manifests
* [Install the VSCode extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) and use the provided starter applications & agent snippets
