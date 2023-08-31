# Error handling

Processor and sink agents can have failure behavior configured in their pipeline.yaml file:

```
errors:
    on-failure: skip|fail|dead-letter
    retries: 1
```

You can configure error behavior at the top of the pipeline file, and then that behavior will apply to all agents in the pipeline.

Source agents do not have configurable error handling.

## Configuration

<table><thead><tr><th width="163.33333333333331">On-failure</th><th width="159">Behavior</th></tr></thead><tbody><tr><td>skip</td><td>Skip the record</td></tr><tr><td>fail</td><td>Fail the processing. The executor pod is restarted. The message and all other messages that were queued or being processed locally will be processed again.</td></tr><tr><td>dead-letter</td><td>The failed message is put into a dead-letter queue topic. The name of the topic is computed from the “input-topic” of the agent (even for implicit topics) as `topicname + “-deadletter”` and the schema is the same.</td></tr></tbody></table>
