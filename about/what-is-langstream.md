---
description: LangStream is an open source project driving AI adoption
---

# What is LangStream?

The LangStream project combines the intelligence of large language models with the agility of streaming processing, to create powerful processing applications.

An application in LangStream can watch a message topic and process data through multiple steps to output some useful generative AI results. Say you have a goal of creating a chatbot that can stay up-to-date with some dataset that is constantly changing. As someone interacts with the bot, they are provided with educated meaningful answers that help them navigate some workflow.

To build this kind of bot that is resilient and production ready. you are going to need quite a few “moving parts”. It will take a combination of multiple systems to complete the solution. Every component will need quite a bit of monitoring to ensure health and quick mitigation.

LangStream can significantly reduce the overhead involved in developing a generative AI project like a chatbot by abstracting away the complexities. A developer can create an application that declares a pipeline of steps that vectorize data as it changes. They can also create an application that takes in a user’s question, compares it with the vectorized data, builds a contextualized prompt, and submits it for completion to an LLM. The result can be passed back to the user for further feedback.

### Building LangStream applications

Each pipeline step is converted into an agent. An agent takes an input message, processes its data, and outputs the result as a new message. Processing could be as simple as setting data to all lowercase, or it could be an instruction to drop a labeled value. Or processing could be something more impactful like generative AI processing using an LLM to convert message data into an embedding, or submitting a prompt to an LLM and receiving a completion.

LangStream knows that there are combinations of agents that will process faster when combined. It discovers these opportunities internally while deploying the application. The output, of course, still matches the intended processing.

Every pipeline has a starting point and an end. In the context of streaming data, this is usually referred to as a source and a sink. Sources could be a database, another message topic, or an application that knows how to produce message data for the starting point topic. A pipeline could have one source or many sources. The boundaries of pipeline sources are left to the developer.

Once a pipeline has successfully processed data, something needs to be done with it. This is where a sink is used. Like sources, sinks take all kinds of different shapes. Typically the sink is going to store the processed data in a database. A pipeline could have one sink attached or many. It’s up to the application developer to choose.

Because LangStream uses message broker topics for transport, the given broker has built-in options for connecting topics to sources and sinks. The challenge is, pipelines can get complex. Adding in an additional dependency on a specific connector can make the project a little too much to manage.

LangStream abstracts certain sources and sinks to help a pipeline developer get to something meaningful, faster. During the design of the pipeline, the developer simply declares the “compute type” as “Kubernetes”. LangStream will do all the work of a connector but with the added context of the overall application design.
