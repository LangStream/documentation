---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: false
---

# Messaging Brokers

LangStream supports both [Apache Kafka](https://kafka.apache.org) and [Apache Pulsar](https://pulsar.apache.org) as message brokers to store and exchange data between agents.

There is also experimental support for [Pravega.io](https://pravega.io).

A LangStream application chooses the message broker at deployment time, and the choice is made in the instance.yaml file.

You can find [here](../../building-applications/topics.md) how to configure the topics in your application.

## Choosing a message broker

The message broker is chosen in the instance.yaml file, using the "broker" section:

```yaml
streamingCluster:
    type: kafka
    configuration:
        admin:
          bootstrapServers: "kafka.default.svc.cluster.local:9092"

```

The LangStream runtime is pluggable and supports multiple message brokers. The current version supports Apache Kafka and Apache Pulsar but you can add your own implementation.
If you're using a different message broker, you have to provide the implementation of the "streamingCluster" interface, feel free to open a GitHub issue or reach out to the
community on Slack if you need help.


## Reference

Check out the reference configurations for [Apache Kafka](./kafka.md) and [Apache Pulsar](./pulsar.md)
