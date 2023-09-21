# topic

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

The topic is an ordered sequence of messages, each message in LangStream is interpreted as a Record, with the following properties:
- a value
- a key
- a set of properties (also named headers) 

The key and the value can be of any type, but by default LangStream interprets them as strings or JSON encoded structures, see below for the details.

Both the key and the value can be null. In some pipelines, like with data coming from CDC (Capture Data Change) data flows or going to Database Sinks, a non null key with a null value represents a DELETION of a record from a database.

The properties of the message are a set of key-value pairs, usually treated as strings. Some messaging brokers, like Kafka, allow to write binary content to headers. LangStream doesn't perform computations or transormations on the message properties if not directly implemented in agents. In case you are writing custom agents you may have to take this into account.

### **Partitioning**

Most of the messaging brokers support the concept of partitioned topics, in Kafka each topic is always partitioned with one or more partitions.

LangStream handles automatically the partitions.

Partitions are a way to increase the concurrency of the processing of the messages. Especially in Kafka, where only one consumer (agent in LangStream terms) can read from a partition at a time.

In many cases LangStream agents poll data from the topics and then perform perallel processing even with only one partition, using multi threading tecniques, but only one pod can still consume from a partition at a time, so even if you increase the parallelism of an agent and you have only 1 partition then you will see only one pod receiving messages at a time.

When you define a topic you can explicitly set the number of partitions:
```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
    partitions: 4
``` 

In case you want to increase the number of partitions you have to use the tools of the messaging broker you are using.

### **Creation and deletions of topics**

LangStream can create your topics when the application is deployed.
This is the purpose of the **creation-mode** configuration.


```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
    deletion-mode: delete
```  

The valid values are:

- "create-if-not-exists": the topic is created when the application is deployed
- "none": the topic is defined in LangStream but LangStream doesn't try to create it

The default behaviour is "none".

At the same way you can automatically delete your topics in case of deletion of the application, this is what 'deletion-mode' does.

Valid values are:
- "delete": the topic is deleted when the application is deleted
- "none": the topic is defined in LangStream but LangStream doesn't try to delete it

{% hint style="warning" %}
If you configure deletion-mode=delete you may lose some data in case of accidental undeploying of your application in production.

In fact, if you don't delete the topics, you can simply deploy the application again and the processing will continue from the point in which the application was stopped. This happens because most of the state of the LangStream application is held in the topics.

{% endhint %}

You can also customise all the properties provided by the underlying broker:

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

You do it by setting the `options` and the `config` configuration parameters.


The `config` section is applyed while creating a topic, in the case of Kafka, they become additional configuration options for the topic. Please refer to the Kafka documentation about [topic configurations](https://kafka.apache.org/documentation/#topicconfigs).

The `options` is related to additional properties required to fine tune the client that connects to the topic.

Available options are:
- `consumer.xxx`: the option xxx is applied to the [Kafka Consumer configuration](https://kafka.apache.org/documentation/#consumerconfigs)
- `producer.xxx`: the optin xxx is apploied to the [Kafka Producer configuratio](https://kafka.apache.org/documentation/#producerconfigs)
- `replication-factor`: this is the replication-factor for the topic, when it is created


### **Ordering guarantees**

LangStream handles all of the aspects you would have to deal with while building a messaging application, one of the most difficult points is to give strong ordering guarantees.
For instance if you are implementing a chat bot you really want that the questions and the (streaming, chuncked) answers are processed in the natural order as perceived by the end user.
This means that in spite of all the processing that is performed thru the pipeline the platform must guarantee that messages are delivered in the expected order.

This is pretty hard, considering that LangStream automatically deals with:
- temporary failures and retries
- asyncronous processing
- (micro) batching
- scalability

The good thing is that you don't have to care about all of these problems.

But you must be aware that the main way to control the ordering of messages is by means of the **message key**. 
LangStream guarantees that all the messages with the same key are processed in the same order as they have been written to the topic. If one message enters a retry loop, then all the other messages with the same key are put put on hold until the message is done.
If the key is null then LangStream is free to process the messages in any order.


### **Implicit topics**

The LangStream planner may decide to create additional topics to connect the agents.
This is because most of the agents may run together in the same kubernetes pod, but under some conditions this is not possible, for instance:

- two agents in the same pipeline have different resource requirements, so they m,must live in separate pods 
- some agents require to connect directly to a topic
- an agent is marked as not "composable"

### **Schema less topics**

By default LangStream interprets the contents of the messages as Unicode encoded strings (UTF-8) and when an agent tries to access the message as a structure, it tries to parse the string as JSON.

This means that you can write a message in the input topic as a string and read it as a JSON structure in the output topic.

When an agent that expects a structure as input encounters a string that cannot
be parsed as JSON this is handled as a regular processing failure, and you can apply the standard failure management options (like skipping unparsable messages or posting them to the deadletter queue).

### **Schema management**

LangStream can handle automatically the Schema associated to the topic, depending
on the messaging broker you are using.

If you are using Apache Pulsar then the Schema Registry is built-in on the Broker
and you don't have to configure anything more.

If you are using Apache Kafka then you need to configure the URL and the credentials to access a Schema Registry.

This happens in the instance.yaml file in the streamingCluster configuration,
see the [kafka](../../instance-clusters/streaming/kafka.md) cluster documentation for the actual configuration of the Schema Registry client.

LangStream comes with an abstraction of the Schema management systems and allows you to write portable applications.

These are the supported schema types:
- string
- bytes
- avro


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

The same applies in case you write an AVRO record: the schema will be automatically registered in the registry.


### **Dead letter queue topics**

When you mark an agent with **on-failure: deadletter**, this means that in case of error the message that was read by the input topic has to be move to a side topic
in order to not stop the pipeline while keeping the problematic message for further debugging.

In this case the LangStream planner automatically create a topic next to the
input topic of the agent, with the same schema and with a name as `topicname + “-deadletter”`.

You can read more about error handling [here](../../building-applications/error-handling.md).
