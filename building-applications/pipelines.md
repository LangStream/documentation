# Pipelines

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

## Pipeline configuration

<table><thead><tr><th width="163">Property</th><th>Description</th><th>Type</th></tr></thead><tbody><tr><td>module</td><td>String</td><td>The module reference for this pipeline. If not specified, a default module will be used.</td></tr><tr><td>id</td><td>String</td><td>Unique id of the pipeline. If not specified, it will be computed automatically.</td></tr><tr><td>name</td><td>String</td><td>The name of the pipeline.</td></tr><tr><td>topics</td><td>object[]</td><td>A collection of topics that will be bound to the application lifecycle, and used to transport data between steps. See [Topics](../configuration-resources/messaging/topics.md) for more details</td></tr><tr><td>assets</td><td>object[]</td><td>A collection of topics that will be bound to the application lifecycle. See [Assets](assets.md) for more details</td></tr><tr><td>resources</td><td>object</td><td>Resources configuration for the pipeline agents.</td></tr><tr><td>pipeline</td><td>object[] (Required)</td><td>Pipeline agents configuration.</td></tr></tbody></table>

### Pipeline agents configuration

Inside the `pipeline` property, you must specify a list of agents.

Each agent can be configured with the following properties.

<table><thead><tr><th width="163.33333333333331">Name</th><th width="171">Type</th><th>Description</th></tr></thead><tbody><tr><td>name</td><td>String (required)</td><td></td></tr><tr><td>id</td><td>String (required)</td><td></td></tr><tr><td>type</td><td>String (required)</td><td>The type name of processing to be run. See <a href="../pipeline-agents/ai-actions/">AI Actions</a> for supported types.</td></tr><tr><td>input</td><td><br></td><td>Reference to the topic name</td></tr><tr><td>output</td><td><br></td><td>Reference to the topic name</td></tr><tr><td>configuration</td><td>object</td><td>Given the chosen type, these are the config values used. Refer to the configuration area of each type for more info.</td></tr></tbody></table>

### Agent resources



When deploying a pipeline, some agents might require additional CPU or memory to run properly. Depending on the traffic load and the agent architecture, you might need to scale the pipeline vertically or horizontally, or both.

The `resources` property allows you to specify the `size` (scale vertically) and the `parallelism` (scale horizontally) for the pipeline.

```yaml
topics:
  ...

resources:
  parallelism: 3
  size: 2
  
pipeline:
  ...
```

Setting `parallelism` to 3 will deploy the pipeline with 3 different replicas. Each replica will use the configured `size` for CPU and memory.

The `size` parameter describes both CPU and memory. The value is a multiplier factor that is computed at runtime, starting from a base cpu/memory value. For example, if the default value for the memory - for a single replica - is 512 MB, specifying `size: 2` will make the pipeline to use 1024MB per-replica.

The requested resources are implemented by using [Kubernetes limits](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/). Be aware that if an agent tries to use more memory than the requested, the pipeline will fail with `OOMKilled` error.

### Multiple manifests in one application

When you place multiple yaml manifests in the same "application" folder, LangStream will create a single application with multiple modules. Each module is a pipeline of agent steps.

```
|- project-folder
    |- application
        |- pipeline.yaml
        |- second-pipeline.yaml
        |- gateways.yaml
        |- configuration.yaml
```

In this structure, both pipeline.yaml and second-pipeline.yaml will be created as a single application, with a separate module for each pipeline.

See the [webcrawler pipeline agent ](broken-reference)and its [source code](https://github.com/LangStream/langstream/tree/main/examples/applications/webcrawler-source) for an example.
