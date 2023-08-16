# text-normaliser

This is an agent that applies specific transformations on text.

### Example

An example that lowercases the provided contents:

```yaml
- name: "Normalize text"
  type: "text-normaliser"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
      makeLowercase: true
```

### Topics

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="173.33333333333331">Label</th><th width="134">Type</th><th>Description</th></tr></thead><tbody><tr><td>makeLowercase</td><td>Boolean (optional)</td><td><p>Transform the provided text to all lowercase.</p><p></p><p>Defaults to a value of “true”</p></td></tr><tr><td>trimSpaces</td><td>Boolean (optional)</td><td><p>Trim empty spaces from each line of text.</p><p></p><p>Defaults to a value of “true”</p></td></tr></tbody></table>

\
