# Topics

LangStream uses a messaging broker, like Apache Kafka or Apache Pulsar, to communicate between agents. A topic is a named stream of messages that agents can read from or write to.

### **Creating a topic**

You define the topics used by the application in the pipeline YAML files.

```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
    deletion-mode: none
  - name: "output-topic"
    creation-mode: create-if-not-exists
    deletion-mode: none
```

You can define the same topic in different pipeline files, but the definition must be exactly the same.

### **Structure of a message**

The topic is an ordered sequence of messages. Each message in LangStream is interpreted as a Record, with the following properties:

* a value
* a key
* a set of properties (also called headers)

The key and the value can be of any type, but by default LangStream interprets them as strings or JSON encoded structures, see below for the details.

Both the key and the value can be null. In some pipelines, like with data coming from CDC (Change Data Capture) data flows or going to database sinks, a non-null key with a null value represents a DELETION of a record from a database.

The properties of the message are a set of key-value pairs, usually treated as strings. Some messaging brokers, like Kafka, allow binary content to be written to headers. LangStream doesn't perform computations or transformations on the message properties if this is not directly implemented in agents. If you are writing custom agents you may have to take this into account.

### **Partitioning**

Most of the messaging brokers support the concept of partitioned topics, in Kafka each topic is always partitioned with one or more partitions.

LangStream handles partitions automatically.

Partitions are a way to increase message processing concurrency. This is especially important in Kafka, where only one consumer (an "agent" in LangStream terms) can read from a partition at a time.

In many cases, LangStream agents poll data from the topics and then perform parallel processing even with only one partition using multi-threading techniques, but only one pod can still consume from a partition at a time, so even if you increase the parallelism of an agent and you have only 1 partition, you will see only one pod receiving messages at a time.

When you define a topic you can explicitly set the number of partitions:

```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
    partitions: 4
```

If you want to increase the number of partitions after setting them, you have to use your messaging broker's tools.

### **Creation and deletions of topics**

LangStream can create your topics when the application is deployed. This is the purpose of the **creation-mode** configuration.

```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
    deletion-mode: delete
```

The valid values are:

* "create-if-not-exists": the topic is created when the application is deployed
* "none": the topic is defined in LangStream but LangStream doesn't try to create it

The default behaviour is "none".

\`deletion-mode' controls automatic deleting of your topics in case of deletion of the application.

Valid values are:

* "delete": the topic is deleted when the application is deleted
* "none": the topic is defined in LangStream but LangStream doesn't try to delete it

{% hint style="warning" %}
If you configure deletion-mode=delete you may lose some data in case of accidental undeploying of your application in production.

In fact, if you don't delete the topics, you can simply deploy the application again and the processing will continue from the point in which the application was stopped. This happens because most of the state of the LangStream application is held in the topics.
{% endhint %}

You can also customise all the properties provided by the underlying broker by setting values in the `options` and `config` configuration parameters.

```yaml
    topics:
      - name: "offset-topic"
        creation-mode: create-if-not-exists
        partitions: 1
        options:
            consumer.max.poll.records: 10
            producer.retries: 2
            replication-factor: 1
        config:
            cleanup.policy: compact
```

The `config` section is applyed while creating a topic. InKafka's case, the parameters become additional configuration options for the topic. Please refer to the Kafka documentation about [topic configurations](https://kafka.apache.org/documentation/#topicconfigs).

The `options` configuration is related to additional properties required to fine tune the client that connects to the topic.

Available options are:

* `consumer.xxx`: the option xxx is applied to the [Kafka Consumer configuration](https://kafka.apache.org/documentation/#consumerconfigs)
* `producer.xxx`: the option xxx is applied to the [Kafka Producer configuration](https://kafka.apache.org/documentation/#producerconfigs)
* `replication-factor`: this is the replication-factor for the topic, when it is created. For more on Kafka's replication factor, see the [Kafka documentation](https://docs.confluent.io/kafka/design/replication.html).

### **Ordering guarantees**

One of the most challenging parts of building a messaging application is providing strong ordering guarantees. LangStream guarantees that all the messages with the same key are processed in the same order as they have been written to the topic. For example, if you're implementing a chat bot, you want the questions and the (streaming, chunked) answers to be processed in their natural order from the end user's perspective. This means that in spite of all the processing performed throughout the pipeline, the platform must guarantee that messages are delivered in the expected order.

This is pretty challenging, considering that LangStream automatically deals with:

* temporary failures and retries
* asynchronous processing
* (micro) batching
* scalability

Fortunately, you don't have to solve all of these problems.

But you must be aware that the main way to control the ordering of messages is by means of the **message key**. LangStream guarantees that all the messages with the same key are processed in the same order as they have been written to the topic. If one message enters a retry loop, then all the other messages with the same key are put put on hold until the message is done. If the key is null then LangStream is free to process the messages in any order.

### **Implicit topics**

The LangStream planner may decide to create additional topics to connect the agents. This is because most of the agents may run together in the same Kubernetes pod, but under some conditions this is not possible, for example:

* two agents in the same pipeline have different resource requirements, so they must live in separate pods
* some agents require a direct connection to a topic
* an agent is marked as not "composable"

### **Schema less topics**

By default LangStream interprets the contents of the messages as Unicode encoded strings (UTF-8) and when an agent tries to access the message as a structure, it tries to parse the string as JSON.

This means that you can write a message in the input topic as a string, and read it as a JSON structure in the output topic.

When an agent that expects a structure as input encounters a string that cannot be parsed as JSON, this is handled as a regular processing failure, and you can apply the standard failure management options (like skipping unparsable messages or posting them to the deadletter queue).

### **Schema management**

LangStream can automatically handle the schema associated to the topic, depending on the messaging broker you are using.

If you are using Apache Pulsar, then the Schema Registry is built-in on the Broker and you don't have to configure anything.

If you are using Apache Kafka, you need to configure the URL and the credentials to access a Schema Registry.

These values are set in the instance.yaml file in the streamingCluster configuration, see the [kafka](broken-reference) cluster documentation for the actual configuration of the Schema Registry client.

LangStream comes with an abstraction of the Schema management system that allows you to write portable applications.

The supported schema types are:

* string
* bytes
* avro

```yaml
topics:
  - name: "schemaless-topic"
    creation-mode: create-if-not-exists
- name: "string-topic"
    creation-mode: create-if-not-exists
    schema:
       type: string
  - name: "bytes-topic"
    creation-mode: create-if-not-exists
    schema:
       type: bytes
  - name: "avro-topic"
    creation-mode: create-if-not-exists
    schema:
        type: avro
        schema: |
            {
                "type" : "record",
                "name" : "Pojo",
                "namespace" : "mynamespace",
                "fields" : [ {
                "name" : "name",
                "type" : "string"
                } ]
            }
```

In case you are consuming from a topic with AVRO schema but you don't know the schema you can omit the schema definition, like this:

```yaml
topics:
  - name: "avro-topic-auto"
    creation-mode: create-if-not-exists
    schema:
        type: avro
```

The runtime gets the schema from the registry while consuming.

The same applies if you write an AVRO record: the schema will be automatically registered in the registry.

### **Dead letter queue topics**

When you mark an agent with **on-failure: deadletter**, this means that in case of error the message that was read by the input topic has to be moved to a side topic to not stop the pipeline while keeping the problematic message for further debugging.

In this case, the LangStream planner automatically creates a topic next to the input topic of the agent, with the same schema and with a name as `topicname + “-deadletter”`.

You can read more about error handling [here](error-handling.md).

### Stream-to-topic parameter

Some agents allow you to configure the "stream-to-topic" parameter in the pipeline as below:

```yaml
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    output: "history-topic"
    configuration:
      model: "${secrets.open-ai.chat-completions-model}"
      # on the log-topic we add a field with the answer
      completion-field: "value.answer"
      # we are also logging the prompt we sent to the LLM
      log-field: "value.prompt"
      # here we configure the streaming behavior
      # as soon as the LLM answers with a chunk we send it to the answers-topic
      stream-to-topic: "output-topic"
      # on the streaming answer we send the answer as whole message
      # the 'value' syntax is used to refer to the whole value of the message
      stream-response-completion-field: "value"
      # we want to stream the answer as soon as we have 10 chunks
      # in order to reduce latency for the first message the agent sends the first message
      # with 1 chunk, then with 2 chunks....up to the min-chunks-per-message value
      # eventually we want to send bigger messages to reduce the overhead of each message on the topic
      min-chunks-per-message: 10
      messages:
        - role: user
          content: "You are a helpful assistant. Below you can find a question from the user. Please try to help them the best way you can.\n\n{{ value.question}}"
```

In this case the agent writes any tokens coming from the LLM to the topic defined in "stream-to-topic".

In fact, LLMs internally work "one token at a time", and the native streaming capabilities of LangStream leverage this behavior for more "real-time" LLM interactions with lower latency.

There are two main configuration properties:

* stream-to-topic: the name of the topic to stream to
* stream-response-completion-field: the field to set in the records sent to the stream-to-topic topic

Usually the value for "stream-response-completion-field" is "value". This means that the token from the LLM replaces the entire content of the "value" part of the message and you can serve it with a [gateway](./api-gateways/README.md) directly. Use "value" to write the result without a structured schema, or use "value.<field>" to write the result in a specific field.

The regular output of the agent is not changed by using "stream-to-topic". The message is still sent to the downstream agent (or output topic) when the whole sequence of tokens is received.

The agent groups tokens to limit the number of writes to the broker by creating sequences of up to "min-chunks-per-message". The first token is sent as soon as possible, then 2 chunks, then 4 chunks, and continues doubling until reaching the limit defined in "min-chunks-per-message".

Messages sent on the "stream-to-topic" are marked with special properties:

* stream-id: this is a string, that is the id of the whole answer
* stream-index: this is a number (as string) of the index of the token in the sequence
* stream-last-message: this is a boolean (as string, "true" or "false") that if "true" then the message is the last of the answer