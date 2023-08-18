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

* datastax/sga-deployer:latest-dev
* datastax/sga-control-plane:latest-dev
* datastax/sga-runtime:latest-dev
* datastax/sga-api-gateway:latest-dev

### Quick Start

To create a LangStream control plane, you will need [kubectl](https://kubernetes.io/docs/reference/kubectl/), [helm cli](https://helm.sh/docs/intro/install/), and a running K8s cluster.

```bash
helm repo add langstream https://datastax.github.io/langstream
kubectl apply -f https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/minio-dev.yaml
helm upgrade -i sga helm/sga --values https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/simple.yaml --wait
```

#### Open the control-plane and api-gateway ports

```bash
# Control plane
kubectl port-forward svc/control-plane 8090:8090 &
# Api gateway
kubectl port-forward svc/api-gateway 8091:8091 &
```
