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

# Instances

This is a declaration of what infrastructure will support the “streaming” and “compute” of the pipeline. Streaming refers to what messaging platform the topics will be created in. Compute refers to where the agents will run the pipeline steps.

```yaml
instance:
  globals:
    tableName: "vsearch.products"
  streamingCluster:
    type: "kafka"
    configuration:
      admin:
        bootstrap.servers: kafka-gcp-useast4.dev.streaming.datastax.com:9093
        security.protocol: SASL_SSL
        sasl.jaas.config: "org.apache.kafka.common.security.plain.PlainLoginModule required username='${ secrets.astra-token.tenant }' password='token:${ secrets.astra-token.token }';"
        sasl.mechanism: PLAIN
        session.timeout.ms: "45000"
  computeCluster:
    type: "kubernetes"
```

### Globals

Within instance.yaml, use "globals" to define values for parameters across your application.

For example, this instance defines `topicName` as a global parameter with the value "input-topic":
```yaml
instance:
  globals:
    topicName: "input-topic"
    otherTopicName: "${OTHER_TOPIC_NAME:-default-topic-name}"
```

The second global `otherTopicName` uses an alternate declaration method where the value is loaded from a dotenv file containing a `OTHER_TOPIC_NAME="value"` line. The `:-` characters allow you to designate a default value - in this case, `default-topic-name`.

The `topicName` parameter can now be referenced wherever you need it, perhaps in your application's pipeline.yaml file:
```yaml
topics:
  - name: "${globals.topicName}"
    creation-mode: create-if-not-exists
    deletion-mode: delete
  - name: "${globals.otherTopicName}"
    creation-mode: create-if-not-exists
    deletion-mode: delete
```

You can also use these parameters when creating assets, as in `CREATE TABLE IF NOT EXISTS ${globals.vectorKeyspace}.${globals.vectorTable}`.

### Manifest

<table><thead><tr><th width="119">Root</th><th width="167">Node</th><th width="94">Type</th><th>Description</th></tr></thead><tbody><tr><td>instance</td><td><br></td><td><br></td><td>Top-level node</td></tr><tr><td><br></td><td>globals</td><td>object</td><td><p>A set of name:value pairs that should be applied to all clusters.</p><p><br></p><p>Example:</p><p>tableName: "vsearch.products"</p></td></tr><tr><td><br></td><td>streamingCluster</td><td>object</td><td>The settings of the messaging platform use to stream data. See the ref below for more.</td></tr><tr><td><br></td><td>computeCluster</td><td>object</td><td>The settings of the cluster where agents process data. See the ref below for more.</td></tr></tbody></table>

### streamingCluster

<table><thead><tr><th width="167">Label</th><th width="107.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td>type</td><td>string</td><td>The type name of messaging platform to be used. Refer to the instance clusters area for supported types.</td></tr><tr><td>configuration</td><td>object</td><td>Configurations of the streaming platform. Refer to the instance clusters area for supported configuration.</td></tr></tbody></table>

{% hint style="info" %}
**DataStax Astra users**

To use your Astra streaming tenant as the streaming cluster with LangStream, enable the Starlight for Kafka feature. Doing so will provide you with the needed bootstrap and security information to use the kafka type.

Read more about enabling Starlight for Kafka in Astra Streaming in the [documentation](https://docs.datastax.com/en/streaming/astra-streaming/developing/astream-kafka.html) and also in the [learning site](https://docs.datastax.com/en/streaming/streaming-learning/use-cases-architectures/starlight/kafka/index.html). Learn more about the Starlight for Kafka project [here](https://docs.datastax.com/en/streaming/starlight-for-kafka/2.10.1.x/index.html).
{% endhint %}
