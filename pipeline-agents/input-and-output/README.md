---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: false
---

# Input & Output

## Source agents

Source agents are responsible for getting records into the pipeline from external services.

* [Web Crawler](webcrawler-source.md)
* [S3 Source](s3-source.md)
* [Azure Blob Storage Source](../builtin-agents/input-and-output/azure-blob-storage-source.md)
* [Apache Camel source agent](camel-source.md)

## Sink agents

Sink agents are responsible for exporting records from the pipeline to external services.

* [Kafka connect Sink](sink.md)
* [Vector Database Sink](vector-db-sink.md)
