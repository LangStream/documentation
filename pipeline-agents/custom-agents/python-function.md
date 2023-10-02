# Python processor

Along with the pre-made agents, you can provide your own processor agent as a Python application.

The Python application needs to follow a specific directory structure for this agent to successfully run. 

Within the “application” directory create a directory named “python”. 

Within that directory place the .py file with the class that will be the entry point.

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

For more on developing custom Python processor agents, see the [Agent Developer Guide.](../agent-developer-guide/)

### Example

Example python class located at ./application/python/example.py:

```python
from langstream import SimpleRecord

# Example Python processor that adds an exclamation mark to the end of the record value
class Exclamation(Processor):
  def process(self, record):
      return [SimpleRecord(record.value() + "!!")]
```

Configure the agent to use the python class:

```yaml
- name: "Process using Python"
  type: "python-function"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    className: example.Exclamation
```

The python application can optionally take in parameters from the application environment. The following is an example python application that is given a “config” object in its `init` method.

```python
from langstream import SimpleRecord
import openai
import json
from openai.embeddings_utils import get_embedding

class Embedding(object):

  def init(self, config):
    print('init', config)
    openai.api_key = config["openaiKey"]

  def process(self, record):
    embedding = get_embedding(record.value(), engine='text-embedding-ada-002')
    result = {"input": str(record.value()), "embedding": embedding}
    new_value = json.dumps(result)
    return [SimpleRecord(value=new_value)]
```

The config object is a map that is built from the agent's pipeline.yaml:

```yaml
- name: "OpenAI Embeddings"
  type: "python-function"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    className: embeddings.Embedding
    openaiKey: "${ secrets.open-ai.access-key }"
```

### Topics

**Input**

* None, the message and configuration will be provided as input to the python function.
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

**Output**

* Structured as a langstream SimpleRecord
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="143.33333333333331">Label</th><th width="159">Type</th><th>Description</th></tr></thead><tbody><tr><td>className</td><td>String (required)</td><td><p>A combination of the file name and the class name.</p><p></p><p>Example: For the file my-python-app.py that has class MyProcessor, the value would be my-python-app.MyProcessor</p></td></tr><tr><td>&#x3C;any></td><td><br></td><td>Additional configuration properties specific to the application.</td></tr></tbody></table>
