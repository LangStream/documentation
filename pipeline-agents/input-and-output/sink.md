# sink

The sink agent will attempt to write the input message data to the specified connector. LangStream does not pre-load any sink connectors. However it is compatible with Kafka connect. You can specify a Kafka sink connector (jar) as an application dependency and then use this agent to implement the connector.

### Prerequisites

You will need the (public) URL of the sink connector’s jar. Here are resources to discover different Kafka connectors:

* [Confluent maven repository](https://packages.confluent.io/maven/io/confluent/) (find public URL of connector jar)
* [Apache Cassandra sink for Kafka](https://github.com/datastax/kafka-sink/releases) (example individual connector release)

Once you have the jar, you’ll need its sha512 hash. Here are resources to calculate this:

* [SHA512 File Hash online](https://emn178.github.io/online-tools/sha512\_file\_hash.html) (simple online tool)
* [sha512sum compute](https://linux.die.net/man/1/sha512sum) (for linux, mac, & wsl)
* [Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash) (for powershell)

Finally, you will need the connector’s configuration properties. If you are using an individually distributed jar, the properties should be available in the project’s documentation. [Confluent connector hub](https://www.confluent.io/hub) offers a searchable database of connectors, which link to the documentation.

### Example

This is an example using the Apache Cassandra sink for Kafka. Include the URL, sha512, and type as an application dependency in configuration.yaml

```yaml
configuration:
  dependencies:
    - name: "Kafka Connect Sink for Apache Cassandra from DataStax"
      url: "https://github.com/datastax/kafka-sink/releases/download/1.5.0/kafka-connect-cassandra-sink-1.5.0.jar"
      sha512sum: "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
      type: "java-library"
```

Then the agent would implement the sink connector with appropriate values

```yaml
- name: "Write to Cassandra"
  type: "sink"
  input: "input-topic" # optional
  configuration:
    name: cassandra-sink
    "connector.class": com.datastax.oss.kafka.sink.CassandraSinkConnector
    "key.converter": org.apache.kafka.connect.storage.StringConverter
    "value.converter": org.apache.kafka.connect.storage.StringConverter
    "cloud.secureConnectBundle": "{{ secrets.cassandra.secure-connect-bundle }}"
    "auth.username": "{{ secrets.cassandra.username }}"
    "auth.password": "{{ secrets.cassandra.password }}"
    "topic.input-topic.vsearch.products.mapping": "id=value.id,description=value.description,name=value.name"
```

### Topics

**Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

**Output**

* None, it’s a sink.

### Configuration

<table><thead><tr><th width="108.33333333333331">Label</th><th width="114">Type</th><th>Description</th></tr></thead><tbody><tr><td>name</td><td>string (required)</td><td>The sink type name</td></tr><tr><td>&#x3C;any></td><td><br></td><td>Additional configuration properties specific to the sink type.</td></tr></tbody></table>
