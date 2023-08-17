# text-splitter

This agent takes input text and splits it into sections based on a character count.

### Example

Example of splitting the text into sections and outputting each as a message to the output topic.

```yaml
- name: "Split into chunks"
  type: "text-splitter"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    chunkSize: 1500
```

### Topics

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="140.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>chunk-size</td><td>Integer (optional)</td><td><p>The number of characters to break a document’s contents into.</p><p></p><p>Default to a value of 1000 characters.</p></td></tr></tbody></table>

\
