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

## Quickstart

To create a LangStream control plane, you will need [kubectl](https://kubernetes.io/docs/reference/kubectl/), [helm cli](https://helm.sh/docs/intro/install/), and a running K8s cluster with a recent version.

Connect to your GCP cluster:
```bash
gcloud container clusters get-credentials <langstream-cluster> --region us-east1 --project <project-name>
Fetching cluster endpoint and auth data.
Kubernetes v1.21.0-alpha+eabdbc0a40fe7efda92e10270f27b0a3485fb743
kubeconfig entry generated for langstream-cluster.
```

Connect to your Azure cluster:
```bash
az account set --subscription <subscription-name>
az aks get-credentials --resource-group k8s-resource-group --name dev
Merged "dev" as current context in /Users/mendon.kissling/.kube/config
```

Connect to your EKS cluster:
```bash
aws eks update-kubeconfig --region="us-east-2" --name="langstream-cluster"
Added new context arn:aws:eks:us-east-2:423019603865:cluster/langstream-cluster to /Users/mendon.kissling/.kube/config
```

Add the LangStream chart repo to your Helm installation and update it to the latest version:
```bash
helm repo add langstream https://langstream.ai/charts
helm repo update langstream
```

### External codeStorage component
This component stores the state of LangStream applications in an S3 API-compatible bucket or Azure blob.

Modify the [values.yaml](https://github.com/LangStream/charts/blob/main/charts/langstream/values.yaml) file you'll be deploying with to configure the external codeStorage component.

These values can be found in your storage provider's dashboard.

Azure:
```
codeStorage:
  type: azure
  configuration:
    endpoint: https://<storage-account>.blob.core.windows.net
    container: langstream
    storage-account-name: <storage-account>
    storage-account-key: <storage-account-key>
```

S3:
```
codeStorage:
  type: s3
  configuration:
    access-key: <aws-access-key>
    secret-key: <aws-secret-key>
```

If you're using GKE Cloud Storage, see [Simple migration from Amazon S3 to Cloud Storage](https://cloud.google.com/storage/docs/aws-simple-migration) for using the Cloud Storage API to interact with an S3 bucket.

To configure a local S3-compatible storage service, such as [minio](https://min.io/docs/minio/kubernetes/upstream/index.html), run:
```bash
kubectl apply -f https://raw.githubusercontent.com/LangStream/langstream/main/helm/examples/minio-dev.yaml
```

### Install LangStream
Install the LangStream Helm chart:
```bash
helm install langstream \
    -n langstream \
    --create-namespace \
    --values values.yaml \
    langstream/langstream
```

Result:
```
Release "langstream" does not exist. Installing it now.
NAME: langstream
LAST DEPLOYED: Tue Nov  7 11:38:05 2023
NAMESPACE: langstream
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

In your Kubernetes cluster, you should see four new pods deploy in the `langstream` namespace.
For more configuration options, see the [Helm charts documentation](https://langstream.ai/charts/).

### Deploy Kafka cluster

Install the Strimzi Kafka operator.
```bash
helm repo add strimzi https://strimzi.io/charts/
helm install strimzi-kafka strimzi/strimzi-kafka-operator
```

Install a [persistent Kafka cluster](https://github.com/strimzi/strimzi-kafka-operator/blob/main/examples/kafka/kafka-persistent-single.yaml) to the langstream namespace.

```bash
kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-persistent-single.yaml -n langstream
kafka.kafka.strimzi.io/my-cluster created
```

The Strimzi operator will create and watch a single-ZooKeeper Kafka cluster.

In your LangStream application's instance.yaml file, point the `bootstrap.servers` to your new Kafka bootstrap server's address.
```yaml
instance:
  streamingCluster:
    type: "kafka"
    configuration:
      admin:
        bootstrap.servers: my-cluster-kafka-bootstrap.langstream.svc.cluster.local:9092
```

For production deployments, set the bootstrap server address as a secret value for KAFKA_BOOTSTRAP_SERVERS.
For more, see [Secrets](../building-applications/secrets.md).

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


### Deploy sample application

Run a sample application to test your new environment.
For more on building LangStream applications, see [Set up your development environment](../building-applications/development-environment.md).
```bash
langstream apps deploy test -app sample-app/application -s sample-app/secrets.yaml -i sample-app/instance.yaml
packaging app: /Users/mendon.kissling/Documents/GitHub/LS Application/sample-app/application
app packaged
deploying application: test (1 KB)
application test deployed
```

To monitor deployment from the CLI, use `langstream apps get <app-name>`.

`langstream-app-setup` and `langstream-runtime-deployer` pods will deploy in the `langstream-default` namespace in your Kubernetes cluster.
When these pods reach a Completed state, your application pod(s) will deploy.

For integrating LangStream and your remote cluster into VSCode workflows, [Install the VSCode extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) and use the provided starter applications & agent snippets.
