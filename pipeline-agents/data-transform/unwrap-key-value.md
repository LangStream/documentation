# unwrap-key-value

If the input message is a KeyValue, the unwrap-key-value transform function extracts the KeyValue’s key or value and makes it the record value.

### Example

Given the input:

```json
{
  "key": {
    "keyField": "key"
  },
  "value": {
    "valueField": "value"
  }

```

With an agent configuration of:

```yaml
- name: "Unwrap key value"
  type: "unwrap-key-value"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    unwrapKey: false
```

The output would be:

```json
{
  "valueField": "value"
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

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#unwrap-key-value).