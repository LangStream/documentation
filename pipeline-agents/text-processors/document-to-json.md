# document-to-json

This agent converts an unstructured blob of text (like a pdf document) into a JSON structured string.

### Example

Example as a step in a pipeline

```yaml
- name: "Convert to structured data"
  type: "document-to-json"
  intput: "input-topic"
  output: "output-topic"
  configuration:
    text-field: text
    copy-properties: true
```

With the configuration above and an input of "Hello there", the output is `{"text": "Hello there"}`.

### Topics

#### **Input**

* Unstructured only text (blob of text) [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#document-to-json).
