# Python source

Along with the included pre-made agents, you can provide your own custom source agent as a Python application. The runtime will attempt to execute the provided class function and return its result.

The Python application needs to follow a specific directory structure for this agent to successfully run.&#x20;

Within the “application” directory, create a directory named “python”.&#x20;

Within that directory, place the .py file with the class function that will be the entry point.

The directory will look something like this:

```
|- Project directory
    |- application
        |- python
            |- application.py
    |- pipeline.yaml
    |- configuration.yaml
|- (optional) secrets.yaml
```

For more on developing custom agents with the Python source, see the [Agent Developer Guide.](../agent-developer-guide/)

### Example

Example python source located at ./application/python/example.py:

```python
import time
from typing import List
from urllib.parse import urlparse

import boto3
from langchain.document_loaders import S3DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langstream import Source, SimpleRecord

class S3Record(SimpleRecord):
    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url


class S3LangChain(Source):
    def __init__(self):
        self.loader = None
        self.bucket = None

    def init(self, config):
        bucket_name = config.get("bucketName", "langstream-s3-langchain")
        endpoint_url = config.get("endpoint", "http://minio-endpoint.-not-set:9090")
        aws_access_key_id = config.get("username", "minioadmin")
        aws_secret_access_key = config.get("password", "minioadmin")
        s3 = boto3.resource(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

        self.bucket = s3.Bucket(bucket_name)
        self.loader = S3DirectoryLoader(
            bucket_name,
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def read(self) -> List[S3Record]:
        time.sleep(1)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            add_start_index=False,
        )
        docs = self.loader.load_and_split(text_splitter=text_splitter)
        return [
            S3Record(doc.metadata["source"], value=doc.page_content) for doc in docs
        ]

    def commit(self, records: List[S3Record]):
        objects_to_delete = [
            {"Key": f'{urlparse(record.url).path.lstrip("/")}'} for record in records
        ]
        self.bucket.delete_objects(Delete={"Objects": objects_to_delete})
```

Configure the agent to use the python class in pipeline.yaml:

```yaml
- name: "A custom python source"
  type: "python-source"
  output: "output-topic" # optional
  configuration:
    className: application.S3LangChain
    bucketName: langstream-langchain-source
    endpoint: "https://s3.eu-west-2.amazonaws.com"

```

### Topics

**Input**

* None, it’s a source

**Output**

* Structured as a langstream SimpleRecord
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="145.33333333333331">Label</th><th width="164">Type</th><th>Description</th></tr></thead><tbody><tr><td>className</td><td>String (required)</td><td><p>A combination of the file name and the class name.</p><p></p><p>Example: For the file my-python-app.py that has class MySource, the value would be my-python-app.MySource</p></td></tr><tr><td>&#x3C;any></td><td><br></td><td>Additional configuration properties specific to the application.</td></tr></tbody></table>

\
