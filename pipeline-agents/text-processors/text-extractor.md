# text-extractor

This agent extracts document contents from a structured string of text.

### Example

An example text-extractor agent step:

```yaml
- name: "Extract text"
  type: "text-extractor"
  input: "input-topic" # optional
  output: "output-topic" # optional
```

### **Topics**

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#text-extractor).