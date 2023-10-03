---
description: Build and run Gen AI applications with ease
---

More tests

<figure><img width=100 src=https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png></figure>

# LangStream Documentation

LangStream is a framework for building and running Generative AI (Gen AI) applications. It is designed to make it easy to build and run Gen AI applications that can process data in real-time. You can combine the power of Large Language Models (LLMs) like GPT-4 and vector databases like Astra DB and Pinecone with the agility of stream processing to create powerful Gen AI applications.

Using LangStream you can develop and test your Gen AI applications on your laptop and then deploy to a production environment powered by Kubernetes and Kafka with a single CLI command.

LangStream applications are fundamentally event-driven. This architecture makes it easy to build reactive Gen AI applications that have scalabiity, fault-tolerance, and high availability.

To make it easy to build Gen AI applications, LangStream comes with several pre-built, configuration-driven agents. There are agents for working with AI chat APIs, vector databases, and text processing, to name a few. If the pre-built agents don't meet your needs, you can easily create your own agents using Python. The LangStream runtime comes preloaded with recent versions of popular Gen AI libraries like LangChain and LlamaIndex.


### Features

* Built on top of proven production technologies like [Kubernetes](https://kubernetes.io/) and [Apache Kafka](https://kafka.apache.org/) 
* Pre-built integrations with LLM services like [ChatGPT](https://openai.com/), [Google Vertex AI](https://cloud.google.com/vertex-ai) and [HuggingFace](https://huggingface.co/)
* Pre-built integration with vector embedding services from Open AI, Google, and Hugging Face. Also includes the ability to download and run open-source embedding models from Hugging Face.
* Pre-built integration with vector databases like [Pinecone](https://www.pinecone.io/) and [Astra DB Vector](https://www.datastax.com/products/vector-search)
* Prompt templating that combines event data, semantic search, database queries, and more for generating prompts with rich context
* Unstructured (PDF, Word, HTML, etc) and structured data processing
* Run Kafka Connect sinks and sources for real-time integration with external systems
* Prometheus metrics and Kubernetes logs for observability
* [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) for developing and debugging applications

### Use Cases
* Q&A chatbots over private data using Retrieval-Augmented Generation (RAG)
* Vector embedding pipelines for managing the lifecycle of vector embeddings
* Automatic text summarization pipelines
* Personalized recommendation pipelines


Get started [here!](get-started.md)
