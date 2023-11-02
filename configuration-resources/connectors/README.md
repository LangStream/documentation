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

# Connectors

With LangStream you can leverage a wide range of connectors to integrate your application with external systems.

It is possible to use Apache Kafka Connectors and Apache Camel components.


## Apache Kafka Connect

Apache Kafka Connect is a framework to connect Kafka with external systems such as databases, key-value stores, search indexes, and file systems, using so-called Connectors.

You can find the docs at [https://kafka.apache.org/documentation/#connect](https://kafka.apache.org/documentation/#connect)

LangStream currently supports both Kafka Connect Sources and Kafka Connect Sinks.


Check out the [Apache Kafka Connect](./kafka-connect.md) page for more information.


## Apache Camel

Apache Camel is an open source integration framework that empowers you to quickly and easily integrate various systems consuming or producing data.

You can find the docs at [https://camel.apache.org/](https://camel.apache.org/)

LangStream currently supports using Camel components as sources.

Check out the [Apache Camel](./camel.md) page for more information.

## Reference

Check out the reference configurations for [Apache Kafka](./kafka.md) and [Apache Pulsar](./pulsar.md)
