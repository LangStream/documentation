# Python sink

Along with the included pre-made agents, you can provide your own custom sink agent as a Python application.

The Python application needs to follow a specific directory structure for this agent to successfully run.

Within the “application” directory, create a directory named “python”.

Within that directory, place the .py file with the class that will be the entry point.

The directory will look like this:

```
|- Project directory
    |- application
        |- python
            |- application.py
    |- pipeline.yaml
    |- configuration.yaml
|- (optional) secrets.yaml
```

For more on developing custom Python sink agents, see the [Agent Developer Guide.](../agent-developer-guide/)

## Python sink example

```python
from typing import List
from langstream import Sink, Record

class ExampleSink(Sink):

    def start(self):
        # Initialize any necessary resources or connections here
        pass

    def write(self, record: Record):
        # Process the records to the sink
        # Perform your processing logic here
        processed_data = self.process_data(record.value)

        # Print or log the processed data
        print("Processed Data:", processed_data)

        # Implement any necessary logic for storing the processed data

    def process_data(self, data):
        # Placeholder for your data processing logic
        # Modify this function according to your actual processing needs
        processed_data = data.upper()  # Example: Convert text to uppercase
        return processed_data

    def close(self):
        # Clean up any resources or connections here
        pass
```

Configure the agent to use the python class in pipeline.yaml:

```yaml
pipeline:
  - name: "A custom Python sink"
    type: "python-sink"
    input: "input-topic"
    output: "output-topic"
    configuration:
      className: application.ExampleSink
```

### Topics

**Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)
* Templating [?](../agent-messaging.md#json-text-input)

**Output**

* None, it’s a sink.

### **Configuration**

<table><thead><tr><th width="145.33333333333331">Label</th><th width="164">Type</th><th>Description</th></tr></thead><tbody><tr><td>className</td><td>String (required)</td><td><p>A combination of the file name and the class name.</p><p>Example: For the file my-python-app.py that has class MySink, the value would be my-python-app.MySink</p></td></tr><tr><td>&#x3C;any></td><td><br></td><td>Additional configuration properties specific to the application.</td></tr></tbody></table>
