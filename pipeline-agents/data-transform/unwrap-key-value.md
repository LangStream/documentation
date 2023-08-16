# unwrap-key-value

If the input message is a KeyValue, the unwrap-key-value transform function extracts the KeyValue’s key or value and makes it the record value.

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

<table><thead><tr><th width="136.33333333333331">Label</th><th width="149">Type</th><th>Description</th></tr></thead><tbody><tr><td>unwrapKey</td><td>boolean (optional)</td><td><p>By default, the KeyValue’s value is unwrapped. Set this parameter to true to unwrap the key instead.<br></p><p>Default value is “false”</p></td></tr></tbody></table>
