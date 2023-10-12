# text-normaliser

This is an agent that applies specific transformations on text.

### Example

An example that lowercases the provided contents:

```yaml
  - name: "Normalise text"
    type: "text-normaliser"
    configuration:
      make-lowercase: true
      trim-spaces: true
```

With the configuration above and an input of "HI there with a TRAILING space ", the output is `hi there with a trailing space.`

### Topics

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#text-normaliser).