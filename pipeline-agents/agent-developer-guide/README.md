---
description: Creating custom Python agents in LangStream
---

# Agent Developer Guide

As your journey continues with LangStream, you might want to develop your own agent.&#x20;

Developing your own agent for LangStream is quite simple, using Python best practices. If you already have a Python application, it could be a good candidate as an Agent.

LangStream offers 3 different types of agents. A [source](../custom-agents/python-source.md) agent is the start of a pipeline, a [sink](../custom-agents/python-sink.md) agent writes pipeline results to another service, and a [processor](../custom-agents/python-function.md) agent is a step in the pipeline. The gist of developing an agent is to implement one of its APIs ([Source](../custom-agents/python-source.md), [Sink](../custom-agents/python-sink.md), or [Processor](../custom-agents/python-function.md)). You provide the application’s source (the .py) files when deploying to the Control Plane. All of Python’s constructs and [duck typing](https://towardsdatascience.com/duck-typing-python-7aeac97e11f8) can be used as you build the agent.

It’s typical to run the Control Plane as an internal service within an Organization. An agent’s outgoing access might be limited to the internal network, or might have internet access. This may create incompatibility with LangStream’s pre-built agents, or you may want to include domain knowledge specific to processing within the agent.&#x20;

The Agent Developer Guide is broken into three milestones:\
1\. [Agent Types](agent-types.md) - Understand the three main Python agents you'll use in your applications.\
2\. [Deploying Agents](agent-creation.md) - Create agents to process records. Handle exceptions for each agent type.\
3\. [Configuration and Testing](configuration-and-testing.md) - Configure, test, and package your agents for production.

Get started with [Part 1: Agent Types.](agent-types.md)

###

