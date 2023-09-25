# Using Apache Pulsar

Configuration for a LangStream streaming instance.

### Configuration

In order to connect to a Pulsar broken you must provide the following configuration:
- the Pulsar Servicer URL
- the Pulsar Admin URL
- the credentials to connect to the Pulsar Admin API
- a default tenant
- a default namespace

### Schema Registry

LangStream supports the Pulsar Schema Registry, you don't need to provide additional configuration.


### Examples

This is how it looks like a configuration for a Pulsar instance:

```yaml
    streamingCluster:
    type: "pulsar"
    configuration:
        admin:
            serviceUrl: "pulsar://localhost:6650"
        service:
            serviceUrl: "http://localhost:8080"
        defaultTenant: "public"
        defaultNamespace: "default"
```