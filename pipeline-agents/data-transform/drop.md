# drop

This agent drops a message for further processing. Use in conjunction with the ‘when’ configuration to selectively drop messages.

### Example

Given the input:

```json
{
  firstName: value1,
  lastName: value2
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

<table><thead><tr><th width="153.33333333333331">Label</th><th width="160">Type</th><th>Description</th></tr></thead><tbody><tr><td>when</td><td>string (optional)</td><td><p>By default, the record is dropped. Set this parameter to selectively choose when to drop a message (do not include mustache brackets, the agent will fill the value correctly).<br></p><p>Example:</p><p>when: “value.userId == 5”</p></td></tr></tbody></table>

