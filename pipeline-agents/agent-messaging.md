---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Agent Messaging

### Agent message structure and templating

All of the agents accept 2 message formats - plain text and json formatted text. Plain text is simply an unstructured string like “this is a string”. JSON formatted text is a string with a structure like `{"a": "this is a", "b":"json string"}.`

#### Plain text input

If the input message to an agent is in plain text, then you refer to it as “\{\{% value\}}”. For example, in the ai-chat-completions agent, if you wanted to append the text from the input message to a pre-formatted prompt, you would set the message configuration as:

```
messages:
  - role: user
    content: "What can you tell me about {{% value}} ?"
```

Or in the query agent if you wanted to include the input message as a part of the query you would:

```
query: "SELECT col1, col2 FROM my-table WHERE col3 like ‘?’"
fields:
  - "value"
```

#### JSON text input

As a JSON formatted string, JSON text provides more structure for the agent to work with. You can reference individual values within the text. Refer to the entire JSON string as “\{\{% value\}}” or you can refer to specific values as “\{\{% value.\<label> \}}”.

If the input message had the format:

```json
{
"first-name": "joe",
"last-name": "schmo",
"account-id": 12345,
"a.dot-value": "asdf",
"address": {
  "street": "123 street rd",
  "city": "hollywood",
  "state": "ca"
  }
}
```

Then you would have the following references available in the agent:

| \{\{% value\}}                | {"first-name": "joe","last-name": "schmo","account-id": 12345,"a.dot-value": "asdf"} |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| \{\{% value.first-name\}}     | joe                                                                                  |
| \{\{% value.last-name\}}      | schmo                                                                                |
| \{\{% value.account-id\}}     | 12345                                                                                |
| \{\{% value.aDot-value\}}     | asdf                                                                                 |
| \{\{% value.address.street\}} | 123 street rd                                                                        |
| \{\{% value.address.city\}}   | hollywood                                                                            |
| \{\{% value.address.state\}}  | ca                                                                                   |

The same query from the previous example could be expanded:

```
query: "SELECT col1, col2 FROM my-table WHERE firstName like '?' && lastName like '?'"
fields:
  - "value.first-name"
  - "value.last-name"
```

#### Output

All agents output results as JSON text, regardless if the input was plain text or not.&#x20;

### Implicit input and output topics

Pipeline agents were designed with debugging and flexibility in mind. All agents support monitoring an input topic for new messages and writing the result of its action to an output topic. This can provide useful debugging points to see how a given agent’s configuration was applied to data. It can also introduce processing optimizations for managing topic backpressures and message backlogs.

Some agents don’t need an input or output specified. In those cases, when LangStream makes the pipeline runnable, it will bypass the use of a message topic and “feed” data directly to the next step. This offers better processing time but is a trade off to needing more memory and compute.

As a best practice, during pipeline development it is recommended to use input/output topics between all agent steps. Performance is not a worry and it helps to make processing more “visible”. When development is stable you could optionally remove some of the intermediate topics to aid processing time, but it’s not common to create a pipeline that does significant processing (3-7 steps) and not have some topics in between steps.

{% hint style="warning" %}
As you learn more about each agent’s capabilities, look for the “Input” and “Output” areas to identify if it supports implicit topics.
{% endhint %}

Example of a pipeline using topics between all agent steps:

```yaml
module: "module-1"
id: "pipeline-1"
name: "Read from S3 and chunk text"
topics:
  - name: "s3-output-extract-input"
    creation-mode: create-if-not-exists
  - name: "extract-output-split-input"
    creation-mode: create-if-not-exists
  - name: "split-output"
    creation-mode: create-if-not-exists
pipeline:
  - name: "Read from S3"
    type: "s3-source"
    output: "s3-output-extract-input"
    configuration:
      bucketName: documents
      endpoint: "http://minio.minio-dev.svc.cluster.local:9000"
  - name: "Extract text"
    type: "text-extractor"
    input: "s3-output-extract-input"
    output: "extract-output-split-input"
  - name: "Split into chunks"
    type: "text-splitter"
    input: "extract-output-split-input"
    output: "split-output"
    configuration:
      chunkSize: 1000
```

The same example pipeline not using topics to transport data:

```yaml
module: "module-1"
id: "pipeline-1"
name: "Read from S3 and chunk text"
topics:
  - name: "split-output"
    creation-mode: create-if-not-exists
pipeline:
  - name: "Read from S3"
    type: "s3-source"
    configuration:
      bucketName: documents
      endpoint: "http://minio.minio-dev.svc.cluster.local:9000"
  - name: "Extract text"
    type: "text-extractor"
  - name: "Split into chunks"
    type: "text-splitter"
    output: "split-output"
    configuration:
      chunkSize: 1000
```



Adding input and output topics between agents also changes how many pods are deployed. For example, creating the below pipeline with no topics between agents feeds data directly to the next step, with all processing taking place in 1 pod. This offers better processing time, but is a trade off to needing more memory and compute.

```yaml
topics:
  - name: input-topic
    creation-mode: create-if-not-exists
  - name: output-topic
    creation-mode: create-if-not-exists
pipeline:
  - name: "Convert to structured data"
    type: "document-to-json"
    input: "input-topic"
    configuration:
      text-field: "text"
      copy-properties: true
  - name: "Normalize text"
    type: "text-normaliser"
    configuration:
      makeLowercase: true
  - name: "Split into chunks"
    type: "text-splitter"
    output: "output-topic"
    configuration:
      splitter_type: "RecursiveCharacterTextSplitter"
      chunk_size: 3
      separators: ["\n\n", "\n", " ", ""]
      keep_separator: false
      chunk_overlap: 1
      length_function: "cl100k_base"
```

Creating the same pipeline with topics between agents creates 3 worker pods and splits processing across them:

```yaml
name: Text processing
topics:
  - name: input-topic1
    creation-mode: create-if-not-exists
  - name: input-topic2
    creation-mode: create-if-not-exists
  - name: output-topic1
    creation-mode: create-if-not-exists
  - name: output-topic2
    creation-mode: create-if-not-exists
pipeline:
  - name: "Convert to structured data"
    type: "text-extractor"
    input: "input-topic1"
    output: "output-topic1"
    configuration:
      text-field: "text"
      copy-properties: true
  - name: "Normalize text"
    type: "text-normaliser"
    input: "output-topic1"
    output: "input-topic2"
    configuration:
      makeLowercase: true
  - name: "Split into chunks"
    type: "text-splitter"
    input: "input-topic2"
    output: "output-topic2"
    configuration:
      splitter_type: "RecursiveCharacterTextSplitter"
      chunk_size: 3
      separators: ["\n\n", "\n", " ", ""]
      keep_separator: false
      chunk_overlap: 1
      length_function: "cl100k_base"
```
