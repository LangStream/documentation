# Pipelines

## About pipelines

A pipeline is a manifest of topics and processing steps.

The example manifest below defines a pipeline with 1 step. It receives messages via "input-topic", processes the messages, and sends processed messages to "output-topic".

```yaml
topics:
  - name: "input-topic"
    creation-mode: create-if-not-exists
  - name: "output-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "ai-chat-completions"
    type: "ai-chat-completions"
    input: "input-topic"
    output: "output-topic"
    errors:
      on-failure: skip
    configuration:
      model: "gpt-3.5-turbo"
      completion-field: "value"
      messages:
        - role: user
          content: "What can you tell me about {{% value}} ?"
```

### Module and Topics Configuration Values

<table><thead><tr><th width="114.33333333333331">Root</th><th width="163">Node</th><th>Description</th><th data-hidden>Type</th></tr></thead><tbody><tr><td>module</td><td></td><td></td><td><br></td></tr><tr><td>id</td><td></td><td>Referenceable value of the pipeline</td><td><br></td></tr><tr><td>name</td><td></td><td>The name of the application</td><td><br></td></tr><tr><td>topics</td><td></td><td>A collection of topics that will be created within the tenant, and used to transport data between steps.</td><td>object[]</td></tr><tr><td><br></td><td>name</td><td>The name of the topic. This value must comply with the given messaging platform’s rules.</td><td>String (required)</td></tr><tr><td><br></td><td>creation-mode</td><td><p>Whether the pipeline should attempt to create the topic if it doesn’t exist. Supported values are:</p><ul><li>“create-if-not-exists”</li><li>“None”</li></ul><p>The default value is “none”</p></td><td>String (optional)</td></tr></tbody></table>

### Pipeline Configuration Values

<table><thead><tr><th width="163.33333333333331">Name</th><th width="171">Type</th><th>Description</th></tr></thead><tbody><tr><td>pipeline<br></td><td>object[]</td><td>The pipeline node holds the collection of processing steps. The order of the steps in the collection decides how the pipeline is arranged.</td></tr><tr><td>Name</td><td>String (required)</td><td></td></tr><tr><td>id</td><td>String (required)</td><td></td></tr><tr><td>type</td><td>String (required)</td><td>The type name of processing to be run. See <a href="../pipeline-agents/ai-actions/">AI Actions</a> for supported types.</td></tr><tr><td>input</td><td><br></td><td>Reference to the topic name</td></tr><tr><td>output</td><td><br></td><td>Reference to the topic name</td></tr><tr><td>configuration</td><td>object</td><td>Given the chosen type, these are the config values used. Refer to the configuration area of each type for more info.</td></tr></tbody></table>
