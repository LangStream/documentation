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

LangStream leverages the [Apache Kafka Connect](https://kafka.apache.org/documentation/#connect) and [Apache Camel](https://camel.apache.org/) frameworks to integrate your application with external systems.



## Apache Kafka Connect

Apache Kafka Connect is a framework to connect Kafka with external systems such as databases, key-value stores, search indexes, and file systems.

You can find the docs at [https://kafka.apache.org/documentation/#connect](https://kafka.apache.org/documentation/#connect)

LangStream currently supports both Kafka Connect Sources and Kafka Connect Sinks.


Check out the [Apache Kafka Connect](./kafka-connect.md) page for more information.


## Apache Camel

Apache Camel is an open source integration framework that empowers you to quickly and easily integrate various systems consuming or producing data.

You can find the docs at [https://camel.apache.org/](https://camel.apache.org/)

LangStream currently supports using Camel components as sources.

Check out the [Apache Camel](./camel.md) page for more information.
