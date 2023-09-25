# Using Apache Pulsar

Configuration for a LangStream streaming instance.

### Configuration

To connect to a Pulsar broker, provide the following configuration:
- the Pulsar Service URL
- the Pulsar Admin URL
- the credentials to connect to the Pulsar Admin API
- a default tenant
- a default namespace

### Schema Registry

LangStream supports the Pulsar Schema Registry, and you don't need to provide any additional configuration.


### Examples

This is how a configuration for a Pulsar instance looks:

```yaml
    streamingCluster:
    type: "pulsar"
    configuration:
        admin:
            serviceUrl: "http://localhost:8080"
        service:
            serviceUrl: "pulsar://localhost:6650"
        defaultTenant: "public"
        defaultNamespace: "default"
```