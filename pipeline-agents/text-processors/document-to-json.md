# document-to-json

This agent converts an unstructured blob of text (like a pdf document) into a JSON structured string.

### Example

Example as a step in a pipeline

```yaml
- name: "Convert to structured data"
  type: "document-to-json"
  output: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    text-field: text
    copy-properties: true
```

### Topics

#### **Input**

* Unstructured only text (blob of text) [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="171.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>text-field</td><td>String (required)</td><td>The name of an additional field that will be added to the output message data containing the structured data.</td></tr><tr><td>copy-properties</td><td>Boolean (optional)</td><td><p>Include the input message headers in the output message.<br></p><p>Default is a value of “true”</p></td></tr></tbody></table>

\
