# Error Handling

Processor and sink agents can have failure behavior configured in their pipeline.yaml file:

```
errors:
    on-failure: skip|fail|dead-letter
    retries: 1
```

The default behavior is "on-failure: fail" with 0 retries.

\
You can configure error behavior at the top of the pipeline file, and then that behavior will apply to all agents in the pipeline. Both agents in this pipeline will skip errors:

````yaml
```
errors:
    on-failure: "skip"
pipeline:
  - name: "convert-to-structure"
    type: "document-to-json"
    input: "questions-topic"
    configuration:
      text-field: "question"
  - name: "compute-embeddings"
    type: "compute-ai-embeddings"
    configuration:
      model: "text-embedding-ada-002"
      embeddings-field: "value.question_embeddings"
      text: "{{% value.question }}"
```
````

Source agents do not have configurable error handling.

## Configuration

<table><thead><tr><th width="163.33333333333331">On-failure</th><th width="159">Behavior</th></tr></thead><tbody><tr><td>skip</td><td>Skip the record</td></tr><tr><td>fail</td><td>Fail the processing. The executor pod is restarted. The message and all other messages that were queued or being processed locally will be processed again.</td></tr><tr><td>dead-letter</td><td>The failed message is put into a dead-letter queue topic. The name of the topic is computed from the “input-topic” of the agent (even for implicit topics) as `topicname + “-deadletter”` and the schema is the same.</td></tr></tbody></table>
