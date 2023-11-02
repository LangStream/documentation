# Using Apache Kafka Connect connectors

Configuration for LangStream Sources and Sinks using Kafka Connect.

### Deplying the connector into your LangStream application

LangStream doesn't bundle all the Kafka Connect connectors, but you can easily deploy them into your application.

Declare the **dependency** to the connector in your configuration.yaml file and LangStream will download it and deploy it into your application.

```yaml
configuration:
  dependencies:
    - name: "Kafka Connect Sink for Apache Cassandra from DataStax"
      url: "https://github.com/datastax/kafka-sink/releases/download/1.5.0/kafka-connect-cassandra-sink-1.5.0.jar"
      sha512sum: "242bf60363d36bd426232451cac836a24ae8d510857372a128f601503ad77aa9eabf14c4f484ca0830b6a68d9e8664e3820739ad8dd3deee2c58e49a94a20a3c"
      type: "java-library"
```

The jar file is downloaded by the LangStream CLI when you are deploying the application and it is copied to the java/lib directory.
You are not required to use this mechanism - you can manually copy the jar files if you prefer - but if you use the dependency mechanism, the LangStream CLI will check the sha512sum of the files to make sure that they are not corrupted.

We recommend adding a .gitignore file into your application so you don't commit the jar file into your git repository.


### Kafka Connect Sinks

Once you have your connector deployed into your application, you can use it in your pipeline.

This is an example of configuring a Sink connector that writes to Apache Cassandra:

```yaml
name: "Write to Cassandra"
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "Write to Cassandra"
    type: "sink"
    input: "input-topic"
    resources:
      size: 2
    configuration:
      connector.class: com.datastax.oss.kafka.sink.CassandraSinkConnector
      name: cassandra-sink
      key.converter: org.apache.kafka.connect.storage.StringConverter
      value.converter: org.apache.kafka.connect.storage.StringConverter
      # Connector specific configuration
      cloud.secureConnectBundle: "${ secrets.cassandra.secure-connect-bundle }"
      auth.username: "${ secrets.cassandra.username }"
      auth.password: "${ secrets.cassandra.password }"
      topic.input-topic.vsearch.products.mapping: "id=value.id,description=value.description,name=value.name"
```

Provide the configuration for the connector in the "configuration" section of the yaml file.
You must provide `connector.class`, `name`, `key.converter` and `value.converter`, as you would for any other Kafka Connect connector.
Check the reference documentation of the connector you are using for more details about its configuration properties.

### Kafka Connect Sources

Kafka Connect source connectors work the same way as sinks, but you have to provide an additional system topic that Kafka Connect uses to store the state of the source connector.
In this example the system topic is named "offset-topic".

To make the Kafka Connect runtime happy you have to set the `cleanup.policy` config value to "compact" for the offset-topic.
And you have to configure it in the configuration of the agent with the offset.storage.topic property.

This is not a special requirement of LangStream, please checkout the Kafka Connect documentation for more details.

```yaml
    id: "pipeline-1"
    topics:
        - name: "output-topic"
          creation-mode: create-if-not-exists
        - name: "offset-topic"
          creation-mode: create-if-not-exists
          partitions: 1
          options:
              replication-factor: 1
          config:
              cleanup.policy: compact
    pipeline:
        - name: "source1"
        id: "step1"
        type: "source"
        output: "output-topic"
        configuration:
            connector.class: myconnector.ClassName
            num-messages: 5
            offset.storage.topic: "offset-topic"
```