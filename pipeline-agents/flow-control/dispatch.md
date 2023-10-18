# dispatch

This agent enables you to dispatch records to different topics, based on conditions defined in the configuration.

### Example

Example of reading from a container, extracting the document text, splitting the text into chunks, and outputting each chunk as a message to the output topic.

```yaml
  - name: "Detect language"
    type: "language-detector"
    input: "input-topic"     
    configuration:
      property: "language"

  - name: "Dispatch"
    type: "dispatch"
    output: default-topic
    configuration:
      routes:
        - when: properties.language == "en"
          destination: topic-english
        - when: properties.language == "fr"
          destination: topic-french
        - when: properties.language == "none"
          action: drop
```

This example detects the language of the input record and then decides to send english and french records to different topics. 
You could then implement another pipeline to perform different computation based on the language.

In case the language is not recognized, the message will be dropped.
In case the language is recognized but the it's neither english or french, it will continue the pipeline - in this case it will be written in the `default-topic`



### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#dispatch).