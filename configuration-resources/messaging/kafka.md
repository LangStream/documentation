# Using Apache Kafka

Configuration for a LangStream streaming instance.

### Configuration

In order to connect to Kafka Broker you must provide the addess of the broker with the `bootstrap.servers` property.

Please refer to the Apache Kafka Java client documentation for more details about the configuration properties.


### Authentication

Usually in Apache Kafka you provide Authentication using the JAAS configuration file, in LangStream you can provide the configuration directly in the instance.yaml file.

- security.protocol: the security protocol to use, for example SASL_SSL
- sasl.jaas.config: the JAAS configuration to use for authentication
- sasl.mechanism: PLAIN
- session.timeout.ms: "45000"


### Examples

This is a configuration for a Kafka instance without authentication, on PLAINTEXT connections:

```yaml
instance:
  streamingCluster:
    type: "kafka"
    configuration:
      admin:
        bootstrap.servers: my-cluster-kafka-bootstrap.kafka:9092
```


This is how it looks like when you use SASL_SSL for authentication:

```yaml
instance:
  streamingCluster:
    type: "kafka"
    configuration:
      admin:
        bootstrap.servers: "{{{ secrets.kafka.bootstrap-servers }}}"
        security.protocol: SASL_SSL
        sasl.jaas.config: "org.apache.kafka.common.security.plain.PlainLoginModule required username='{{{ secrets.kafka.username }}}' password='{{{ secrets.kafka.password }}}';"
        sasl.mechanism: PLAIN
        session.timeout.ms: "45000"
```

Please always use secrets to store sensitive information like passwords and usernames.

### Using Apache Kafka in "docker run"

When you are running you application in [Docker](../../installation/docker.md) mode, you can use the default Kafka instance provided by the LangStream docker image and you don't need to provide any configuration.