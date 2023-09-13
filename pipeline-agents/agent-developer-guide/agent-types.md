---
description: Part 1 of the Agent Developer Guide
---

# Agent Types

### Source

A source agent is responsible for bringing data into the application’s pipeline.&#x20;

A source agent is the first step of a pipeline and replaces the use of an input topic. A source can be anything. The agent is responsible for retrieving data from a service and uses the LangStream API to create a `Record` that encapsulates that data. LangStream will produce a message on the specified topic for other agents to consume.

### Sink

A sink agent is responsible for writing data to a service outside the application pipeline.&#x20;

The agent is responsible for accepting a list of `Record`s as input and writing the value to the given service. A sink agent may be the last step in a pipeline or may capture data and continue to the next steps in the pipeline.

### Processor

Processor agents are typically placed throughout an application’s pipeline.&#x20;

A processor agent might manipulate data as it flows through the pipeline, or could add in context to help downstream agents make decisions. A processor agent is responsible for accepting a list of `Record`s as input, doing some processing as necessary, and returning a `Record` (or many `Record`s) as a result.

### What's next?

Continue on to Part 2 of the Agent Developer Guide, [Agent Creation.](agent-creation.md)
