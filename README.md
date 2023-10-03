---
description: Build and run Gen AI applications with ease
---

More tests
<i class="fab fa-github"></i>

<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 496 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg>

<a href="https://github.com/FortAwesome/Font-Awesome">
  <svg>
    <use xlink:href="fa-brands.svg#github"></use>
  </svg>
</a>



<p>I will display &#xf09b;</p>

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
