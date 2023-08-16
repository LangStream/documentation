# merge-key-value

This agent merges the fields of KeyValue records where both the key and value are structured types of the same schema type.

### Example

Given the input:

```json
{
  key: {
    keyField: key
  },
  value: {
    valueField: value
  }
}
```

With an agent configuration of:

```yaml
- name: "Merge key value"
  type: "merge-key-value"
  input: "input-topic" # optional
  output: "output-topic" # optional
```

The output would be:

```json
{
  key: {
    keyField: key
  },
  value: {
    keyField: key,
    valueField: value
  }
}
```

### Topics

#### Input

* Structured only text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### Output

* Structured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

(no configuration options)
