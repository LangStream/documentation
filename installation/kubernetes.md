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

LangStream container images are available on the [Github packages registry](https://github.com/orgs/LangStream/packages?repo\_name=langstream). A LangStream cluster is made up of the following images:

* [datastax/langstream-deployer](https://github.com/LangStream/langstream/pkgs/container/langstream-deployer)
* [datastax/langstream-control-plane](https://github.com/LangStream/langstream/pkgs/container/langstream-control-plane)
* [datastax/langstream-runtime](https://github.com/LangStream/langstream/pkgs/container/langstream-runtime)
* [datastax/langstream-api-gateway](https://github.com/LangStream/langstream/pkgs/container/langstream-api-gateway)
* [datastax/langstream-cli](https://github.com/LangStream/langstream/pkgs/container/langstream-cli)

### Quick Start

To create a LangStream control plane, you will need [kubectl](https://kubernetes.io/docs/reference/kubectl/), [helm cli](https://helm.sh/docs/intro/install/), and a running K8s cluster.

```bash
kubectl apply -f https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/minio-dev.yaml
helm repo add langstream https://langstream.ai/charts
helm repo update
helm upgrade \
    -i langstream \
    -n langstream \
    --create-namespace \
    --values https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/simple.yaml \
    langstream/langstream
```

#### Open the control-plane and api-gateway ports

Control plane:

```bash
kubectl -n langstream port-forward svc/langstream-control-plane 8090:8090 &
```

API gateway:

```bash
kubectl -n langstream port-forward svc/langstream-api-gateway 8091:8091 &
```

### Alternate port forwarding

You can instead open the control plane and API gateway ports in your Helm chart.

This example uses traefik for ingress.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: control-plane
  annotations:
    kubernetes.io/ingress.class: "traefik"
spec:
  rules:
    - host: langstream.yourdomain.local  # Replace with your actual domain or host
      http:
        paths:
            backend:
              service:
                name: langstream-control-plane
                port:
                  number: 8090

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-gateway
  annotations:
    kubernetes.io/ingress.class: "traefik"
spec:
  rules:
    - host: ws.langstream.yourdomain.local  # Replace with your actual domain or host
      http:
        paths:
            backend:
              service:
                name:  langstream-api-gateway
                port:
                  number: 8091

```

### Your first application

Here are a few ways to get started building LangStream applications:

* [Set up your development environment](building-applications/development-environment.md) and learn how to build the needed manifests
* [Install the VSCode extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) and use the provided starter applications & agent snippets
