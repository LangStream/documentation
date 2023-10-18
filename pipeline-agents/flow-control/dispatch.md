# dispatch

This agent enables you to dispatch records to different topics, based on conditions defined in the configuration.

### Example

This is an example about how to use the `dispatch` agent to dispatch records to different topics based on the language of the text.

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

This example detects the language of the input record and then dispatches english and french records to different topics. 
You could then implement another pipeline to perform different computations based on the language.

If the language is not recognized, the message is dropped.
If the language is recognized but it's neither english or french, the message will be written to the `default-topic`


### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#dispatch).