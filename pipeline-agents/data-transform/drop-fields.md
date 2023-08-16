# drop-fields

This agent drops fields of structured data.

### Example

Given the input:

```json
{
 name: value1, 
 password: value2
}
```

With an agent configuration of:

```yaml
- name: "Drop password"
  type: "drop-fields"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    fields: ["password"]
```

The output would be:

```json
{
  "name": "value1"
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

<table><thead><tr><th width="113.33333333333331">Label</th><th width="181">Type</th><th>Description</th></tr></thead><tbody><tr><td>fields</td><td>string (required)</td><td>A comma-separated list of fields to drop.</td></tr><tr><td>part</td><td>string (optional)</td><td><p>When used with KeyValue data, defines if the transform function is done on the key or on the value. If null or absent the transform function applies to both the key and the value.</p><p></p><p>Supported values are “key” or “value”.</p></td></tr></tbody></table>
