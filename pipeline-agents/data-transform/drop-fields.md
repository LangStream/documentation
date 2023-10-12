# drop-fields

This agent drops fields of structured data.

### Example

Given the input:

```json
{
 "name": "value1", 
 "password": "value2"
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

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#drop-fields).