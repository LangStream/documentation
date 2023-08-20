# Python source

Along with the included pre-made agents, you can provide your own custom source agent as a Python application. The runtime will attempt to execute the provided class function and return its result.

The Python application needs to follow a specific directory structure for this agent to successfully run.&#x20;

Within the “application” directory, create a directory named “python”.&#x20;

Within that directory, place the .py file with the class function that will be the entry point.

### Example

Example python class located at ./application/python/example.py:

```python
import tempfile
import time
from typing import List


import boto3
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


from langstream_runtime.api import Source, Record
from langstream_runtime.simplerecord import SimpleRecord


class ExampleSource(Source):
   # initialize the application
    def init(self, config):
        # example input args
        # bucket_name = config.get('bucketName', 'langstream-s3-langchain')
        # endpoint_url = config.get('endpoint', 'http://minio-endpoint.-not-set:9090')


    # read from the source (like S3 or database)
    def read(self) -> List[Record]:
        time.sleep(1)
        text_splitter = RecursiveCharacterTextSplitter(
            # Set a really small chunk size, just to show.
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            add_start_index=False,
        )
        docs = self.loader.load_and_split(text_splitter=text_splitter)
        return [ S3Record(doc.metadata['s3_object_key'], value=doc.page_content) for doc in docs ]


    # finalize the read
    def commit(self, records: List[S3Record]):
        objects_to_delete = [{'Key': f'{record.name}'} for record in records]
        self.bucket.delete_objects(Delete={'Objects': objects_to_delete})
```

Configure the agent to use the python class in configuration.yaml:

```yaml
- name: "A custom python source"
  type: "python-source"
  output: "output-topic" # optional
  configuration:
    className: example.ExampleSource
    bucketName: langstream-langchain-source
    endpoint: "https://s3.eu-west-2.amazonaws.com"

```

### Topics

**Input**

* None, it’s a source

**Output**

* Structured as a langstream\_runtime.api.Record
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="145.33333333333331">Label</th><th width="164">Type</th><th>Description</th></tr></thead><tbody><tr><td>className</td><td>String (required)</td><td><p>A combination of the file name and the class name.</p><p></p><p>Example: For the file my-python-func.py that has class MyFunction, the value would be my-python-func.MyFunction</p></td></tr><tr><td>&#x3C;any></td><td><br></td><td>Additional configuration properties specific to the application.</td></tr></tbody></table>

\
