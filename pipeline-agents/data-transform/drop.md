# drop

This agent drops a message for further processing. Use in conjunction with the ‘when’ configuration to selectively drop messages.

### Example

Given the input:

```json
{
  "firstName": "value1",
  "lastName": "value2"
}
```

With an agent configuration of:

```yaml
- name: "Cast to a string"
- name: "Drop user data"
  type: "drop"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    when: "value.firstName == value1"
```

There would be no output because the message is dropped.

### Topics

#### Input

* Structured only text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### Output

* Structured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#drop).
