# trigger-event

This agent enables you to write a new record (an "event") to a different topic, based on a condition.
It can also optionally drop the record from the main flow of the pipeline.

This agent is different from the [dispatch agent](dispatch.md) as the record that is sent to the new topic is a new record, not the same record that was received.

### Example

This is an example about how to use the `trigger-event` agent to write a new record to a different topic when a condition is met.

```yaml
  - name: "Split some text"  
    type: "text-splitter"
    input: input-topic-splitter
    configuration:
       ....

  - name: "Trigger event on last chunk"
    type: "trigger-event"
    output: output-topic-chunks
    configuration:
      destination: drop-stale-chunks-topic
      continue-processing: true
      when: fn:toInt(properties.text_num_chunks) == (fn:toInt(properties.chunk_id) + 1)
      fields:
          - name: "value.filename"
            expression: "key.filename"
```

In this example the `text-splitter` agent splits a text in to a set of chunks.
When the last chunk is processed, the `trigger-event` agent will write a new record to the `drop-stale-chunks-topic` topic.
The new record will have a filename field into the value part.

## Defining the contents of the output record

The `trigger-event` agent allows you to configure a set of fields that will be written to the output record.
As usual you can write to the key part, the value part and the properties of the record.
Use the [expression language](../../building-applications/expression-language.md) to define the fields and write the expression.


### Aborting the processing downstream

The `trigger-event` agent can also abort the processing of the record downstream by setting the `continue-processing` property to `false`.
This is useful in the cases in which you have some system events that you want to write to a different topic, but you don't want to continue processing the record downstream.

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#trigger-event).