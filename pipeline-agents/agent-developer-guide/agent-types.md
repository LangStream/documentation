---
description: Part 1 of the Agent Developer Guide
---

# Agent Types

LangStream offers 3 different types of agents. A [source](../custom-agents/python-source.md) agent is the start of a pipeline, a [sink](../custom-agents/python-sink.md) agent writes pipeline results to another service, and a [processor](../custom-agents/python-function.md) agent is a step in the pipeline. The gist of developing an agent is to implement one of its APIs ([Source](../custom-agents/python-source.md), [Sink](../custom-agents/python-sink.md), or [Processor](../custom-agents/python-function.md)). You provide the application’s source (the .py) files when deploying to the Control Plane. All of Python’s constructs and [duck typing](https://towardsdatascience.com/duck-typing-python-7aeac97e11f8) can be used as you build the agent.

It’s typical to run the Control Plane as an internal service within an Organization. An agent’s outgoing access might be limited to the internal network, or might have internet access. This may create incompatibility with LangStream’s pre-built agents, or you may want to include domain knowledge specific to processing within the agent.&#x20;

### Source

A source agent is responsible for bringing data into the application’s pipeline.&#x20;

A source agent is the first step of a pipeline and replaces the use of an input topic. A source can be anything. The agent is responsible for retrieving data from a service and uses the LangStream API to create a `Record` that encapsulates that data. LangStream will produce a message on the specified topic for other agents to consume.

### Sink

A sink agent is responsible for writing data to a service outside the application pipeline.&#x20;

The agent is responsible for accepting a list of `Record`s as input and writing the value to the given service. A sink agent may be the last step in a pipeline or may capture data and continue to the next steps in the pipeline.

### Processor

Processor agents are typically placed throughout an application’s pipeline.&#x20;

A processor agent might manipulate data as it flows through the pipeline, or could add in context to help downstream agents make decisions. A processor agent is responsible for accepting a list of `Record`s as input, doing some processing as necessary, and returning a `Record` (or many `Record`s) as a result.

### Service

Service agents are generic applications that usually do not process streaming data in the scope of a pipeline.&#x20;

Tipically a Service exposes an API service that can be consumed by external applications. For instance you can build your ChatBot UI using a service&#x20;

### What's next?

Continue on to Part 2 of the Agent Developer Guide, [Agent Creation.](broken-reference)
