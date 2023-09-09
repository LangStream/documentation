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

<table><thead><tr><th width="197.33333333333331">Label</th><th width="140">Type</th><th width="408.66666666666674">Description</th></tr></thead><tbody><tr><td>allowedLanguages</td><td>string[] (required)</td><td><p>A collection of the language codes that are allowed to be further processed. If the code doesn’t pass, the message will be dropped.</p><p></p><p>Refer to the <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">ISO 639-1list</a> for allowed codes.</p></td></tr></tbody></table>
