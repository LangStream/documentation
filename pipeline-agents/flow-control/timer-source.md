# timer-source

This source agent periodically emits a new record (an "event") and passes it to the pipeline.

### Example

This is an example using the `timer-source` agent to emit a new record every 60 seconds.

```yaml
  pipeline:
    - name: "Timer"
      type: "timer-source"    
      configuration:
        period-seconds: 60
        fields:
            - name: "key.id"
              expression: "fn:uuid()"
            - name: "value.string_payload"
              expression: "'constant-string-payload'"
            - name: "value.int_payload"
              expression: "42"
            - name: "properties.foo"
              expression: "'some property'"
```

In this example the `timer-source` agent emits one record every 60 seconds.

## Defining the contents of the output record

The agent allows you to configure a set of fields that will be written to the output record.
As usual you can write to the key part, the value part and the properties of the record.
Use the [expression language](../../building-applications/expression-language.md) to define the fields and write the expression.

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#timer-source).