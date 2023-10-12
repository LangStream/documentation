# language-detector

This is an agent that will detect the language of a message’s data and limit further processing based on language codes.

### Example

```yaml
- name: "Detect language"
  type: "language-detector"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    allowedLanguages: ["it"]
    property: "language"
```

### Topics

#### Input

* Structured and unstructured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### Output

* Structured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#language-detector).