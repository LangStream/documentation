# text-splitter

This agent takes input text and splits it into sections based on a character count.

### Example

Example of splitting the text into sections and outputting each as a message to the output topic.

```yaml
- name: "Split into chunks"
    type: "text-splitter"
    configuration:
      splitter_type: "RecursiveCharacterTextSplitter"
      chunk_size: 400
      separators: ["\n\n", "\n", " ", ""]
      keep_separator: false
      chunk_overlap: 100
      length_function: "cl100k_base"
```

With a chunk\_size of 3 and an input of Hi there, the output is:

```
output: "Hi "
output: "the"
output: "re"
```

### Topics

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#text-splitter).