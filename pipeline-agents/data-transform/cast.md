# cast

The casting agent transforms the input message data into a target-compatible schema.

### Example

Given the input:

```json
{
 "field1": "value1", 
 "field2": "value2"
}
```

With an agent configuration of:

```yaml
- name: "Cast to a string"
  type: "cast"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    schema-type: "string"
```

The output would be:

```json
{
  "field1": "value1", 
  "field2": "value2"
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

<table><thead><tr><th width="153.33333333333331">Label</th><th width="160">Type</th><th>Description</th></tr></thead><tbody><tr><td>schema-type</td><td>string (required)</td><td>The target schema type. Only "STRING" is available.</td></tr><tr><td>part</td><td>string (optional)</td><td><p>When used with KeyValue data, defines if the processing is done on the key or on the value. If null or absent the transform function applies to both the key and the value.</p><p></p><p>Supported values are “key” or “value”.</p></td></tr></tbody></table>
