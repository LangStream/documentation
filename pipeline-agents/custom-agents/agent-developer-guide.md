---
description: Creating custom Python agents in LangStream
---

# Agent Developer Guide

As your journey continues with LangStream, you might want to develop your own agent.&#x20;

Developing your own agent for LangStream is quite simple, using Python best practices. If you already have a Python application, it could be a good candidate as an Agent.

LangStream offers 3 different types of agents. A [source](python-source.md) agent is the start of a pipeline, a [sink](python-sink.md) agent writes pipeline results to another service, and a [processor](python-function.md) agent is a step in the pipeline. The gist of developing an agent is to implement one of its APIs ([Source](python-source.md), [Sink](python-sink.md), or [Processor](python-function.md)). You provide the application’s source (the .py) files when deploying to the Control Plane. All of Python’s constructs and [duck typing](https://towardsdatascience.com/duck-typing-python-7aeac97e11f8) can be used as you build the agent.

It’s typical to run the Control Plane as an internal service within an Organization. An agent’s outgoing access might be limited to the internal network, or might have internet access. This may create incompatibility with LangStream’s pre-built agents, or you may want to include domain knowledge specific to processing within the agent.&#x20;

#### Agent types

[**Source**](python-source.md)

A source agent is responsible for bringing data into the application’s pipeline.&#x20;

A source agent is the first step of a pipeline and replaces the use of an input topic. A source can be anything. The agent is responsible for retrieving data from a service and uses the LangStream API to create a `Record` that encapsulates that data. LangStream will produce a message on the specified topic for other agents to consume.

[**Sink**](python-sink.md)

A sink agent is responsible for writing data to a service outside the application pipeline.&#x20;

The agent is responsible for accepting a list of `Record`s as input and writing the value to the given service. A sink agent may be the last step in a pipeline or may capture data and continue to the next steps in the pipeline.

[**Processor**](python-function.md)

Processor agents are typically placed throughout an application’s pipeline.&#x20;

A processor agent might manipulate data as it flows through the pipeline, or could add in context to help downstream agents make decisions. A processor agent is responsible for accepting a list of `Record`s as input, doing some processing as necessary, and returning a `Record` (or many `Record`s) as a result.

#### Deploying the agent

Once you have built, tested, and packaged the agent you will need to include it as a part of the LangStream application deployment. Within the “application” directory create a directory named “python”. Within that directory place all the files included in packaging.

```
|- application
    |- python
        |- main.py
```

To include the agent as a step in the pipeline, set the className to match the entry coordinates in the “python” folder. For example, if the entry to a source agent was “main.py” and the class was “MySourceAgent”, then the pipeline step would be:

```
- name: "Process using custom source"
  type: "python-source"
  output: "output-topic"
  configuration:
    className: main.MySourceAgent
```

#### Agent records

When developing a custom agent, your contract with the LangStream runtime will be implementing the correct function(s) as well as working with the `Record` type. This is how LangStream moves data between agents and message topics.&#x20;

Below is the definition of the Record interface.

```
from abc import abstractmethod
from typing import Any, List, Tuple

class Record(ABC):
    """The Record interface"""

    @abstractmethod
    def key(self):
        """Get the record key."""
        pass

    @abstractmethod
    def value(self):
        """Get the record value."""
        pass

    @abstractmethod
    def origin(self) -> str:
        """Get the origin of the record."""
        pass

    @abstractmethod
    def timestamp(self) -> int:
        """Get the timestamp of the record."""
        pass

    @abstractmethod
    def headers(self) -> List[Tuple[str, Any]]:
        """Get the record headers."""
        pass
```

The LangStream Python package also offers an implementation of the `Record` class, called a `SimpleRecord`. Its constructor makes creating a new Record easier to implement. All of the above properties & functions are available in `SimpleRecord` .

```
from typing import Any, List, Tuple

class SimpleRecord(Record):
    def __init__(self, value, key=None, origin: str = None, timestamp: int = None, headers: List[Tuple[str, Any]] = None):
        self._value = value
        self._key = key
        self._origin = origin
        self._timestamp = timestamp
        self._headers = headers or []

...
```

#### Creating agents

**Source**

If you are creating a source agent, all that is required is the “read” function. This function doesn’t have any input but returns a collection of `Record`s that will be passed to the next step in the pipeline. The LangStream runtime will call this function in a loop. Depending on the source type, care needs to be taken to not overwhelm the service being called.

```
from langstream import Source, Record
from typing import Any, Dict

class MySourceAgent(Source):
  def init(self, config: Dict[str, Any]):
    # On start, consume config values
    pass

  def read(self) -> List[Record]:
    # The Source agent generates records and returns them as a list of records
    
    time.sleep(1)
    results = []
  
    # Implement a read from service
    # results.append(Record(value=XXXXX))
   
    return results

  def close(self):
    # Clean up before exiting
    pass
```

An alternate way of creating a source is to import `SimpleRecord` from the LangStream Python package and implement a `read` function. The LangStream runtime will “sense” that you have created a source type agent.

```
from langstream import SimpleRecord

class MySourceAgent(object):
  def read(self) -> List[SimpleRecord]:
    # The Source agent generates records and returns them as a list
  
    results = []
  
    # Implement a read from service
    # results.append(SimpleRecord(value=XXXXX))
   
    return results
```

**Handling exceptions**

It is left to the developer to handle errors in a source agent. The LangStream runtime is not expecting any errors from the agent process. If an unhandled exception occurs within a source agent, it will bubble up through the container, to the pod, where the Kubernetes scheduler will restart the pod. At a minimum, you can print to console and let Kubernetes direct the error message somewhere. This will prevent the pod restart.

```
  def read(self) -> List[Record]:
    try:
      # do some work
      return results
    except Exception as e:
      logging.error(f"Read error: {e}")
    
    return [] # gracefully return nothing because an exception occurred
```

**Sink**

If you are creating a sink agent then you’ll need to implement the “write” function as well as the “set\_commit\_callback” function. The write function takes in a collection of `Record`s that were provided by the previous step in the pipeline. It is called whenever data is available for processing. The set\_commit\_callback commit function provides acknowledgment to LangStream that records have been successfully consumed and can be removed.

```
from langstream import Sink, Record, CommitCallback
from typing import Any, Dict, List

class MySinkAgent(Sink):
  def init(self, config: Dict[str, Any]):
    # On start, consume config values
    pass

  def write(self, records: List[Record]):
    # Receives records from the framework and typically writes them to an external service
  
    for record in records:
      # use record.headers() for reference
      # write record.value() to a service
      self.commit_callback.commit(record)

  def set_commit_callback(self, commit_callback: CommitCallback):
    self.commit_callback = commit_callback

  def close(self):
    # Clean up before exiting
    pass
```

**Handling exceptions**

Ideally the python app catches and handles exceptions that occur while committing a record to a sink. If an exception goes uncaught in the agent process, the LangStream runtime will follow the failure management strategy declared in pipeline error spec. This gives the developer tools to prevent pod restarts.

**Processor**

Finally, if you are creating a processor agent, you will implement the “process” function. This function takes in a collection of `Record`s that were provided by the previous step in the pipeline. It is called whenever data is available for processing.

```
from langstream import Processor, Record
from typing import Any, Dict, List, Tuple, Union

class MyProcessorAgent(Processor):
  def init(self, config: Dict[str, Any]):
    # On start, consume config values
    pass

  def process(self, records: List[Record]) -> List[Tuple[Record, Union[List[Record], Exception]]]:
    results = []
  
    for record in records:
      try:
        # do some work
        # results.append((record, [Record(), Record(), ...]))
      except Exception as e:
        results.append((record, e))

    return results

  def close(self):
    # Clean up before exiting
    pass
```

The return of a processor agent is meant to be generic, so that the developer can optimize for batching. A simple processing rule might return one Record for each record provided. But in more advanced cases, the processing might result in multiple records returned from a single Record provided.

If you had 2 input records “record1” and “record2” and the processing resulted in 2 to 3 new records for each provided, then the result would be:

```
[
    (record1, [outputRecord1, outputRecord2]),
    (record2, [outputRecord3, outputRecord4, outputRecord5])
]
```

If an exception occurred while processing the second record provided, the result would include the caught `Exception`:

```
[
    (record1, [outputRecord1, outputRecord2]),
    (record2, Exception)
]
```

Both of these returned collections would let the LangStream runtime gracefully handle issues and continue processing the next step(s).

**Handling exceptions**

The processor agent has a special return type `List[Tuple[Record, Union[List[Record], Exception]]]` that has provisions for including an Exception rather than the Record(s). If an exception is provided in the return, the LangStream runtime will follow the failure management strategy declared in pipeline error spec. This gives the developer tools to prevent pod restarts.

**Single record processor**

The LangStream Python package offers an implementation of the full `Processor` interface, called `SingleRecordProcessor`. This class is a simplified way to create a processor where 1 `Record` will be received and N number of `Record`s will be returned. Exception handling will be done by agent processing.

```
from langstream import Record, SimpleRecord, SingleRecordProcessor
from typing import List

class MyAgent(SingleRecordProcessor):
  def process_record(self, record: Record) -> List[Record]:
    results = []
  
    try:
      # do some work
      # results.append( SimpleRecord(value="some value") )
    except Exception as e:
      results.append((record, e))

    return results
```

{% hint style="info" %}
Start with the `SingleRecordProcessor` and move into a full `Processor` as needed. Most use cases should fit `SingleRecordProcessor.`Only the most advanced batching and asynchronous processing need a full `Processor`.
{% endhint %}

#### Configuration

Normally it’s a best practice to not hardcode credentials, settings, and other dynamic information an application may need. The LangStream runtime offers a way to provide configuration values at runtime to the agent. The values are declared in the pipeline.yaml manifest where the agent step is created, and are made available during the startup of the agent process as a Dictionary.

Given the labels declared in init:

```
from typing import Dict, Any

def init(self, config: Dict[str, Any]):
  self.value1 = config.get("value1", "default value")
  self.value2 = config.get("value2", "default value")
```

The values would be passed to the agent in pipeline.yaml:

```
pipeline:
  - name: "Load S3 documents and chunk them with LangChain"
    type: "python-source|python-sink|python-processor"
    output: "output-topic"
    input: "input-topic"
    configuration:
      className: example.MyAgent
      value1: "some-config-value" # as string
      value2: "{{ secrets.my-app.some-secret-value}}" # as a secret ref
```

#### Testing and packaging the agent

During development, it’s best to follow the [12 factors](https://12factor.net/) as closely as possible - specifically parity between environments. You should be developing an agent locally using the same (or near similar) environment it will run within on LangStream. Our approach to reach environment parity is to use Docker as a test and packaging environment.

Python is a cross-platform runtime. Given a list of dependent packages (requirements.txt), the installation of an app should be augmented/fail based on what operating system is being used. While most installers offer the option of declaratively providing what platform the install should provision for, if you’ve ever attempted this you know there are quite a few caveats that come with that promise. To achieve a reproducible, iterable result, it’s best to package and test in an environment matching production.

**Packaging**

When you are creating a LangStream agent, you aren’t creating a proper Python package. It’s more akin to creating a cloud function (think Lambda). Given the [folder structure of a LangStream application](https://docs.langstream.ai/building-applications/development-environment), inside the “application” folder, your agent source code will go inside a “python” folder. It’s encouraged to develop the agent in that folder. Given that some agents are one simple .py file, there’s no need to create a separate development environment.

To build an application in Python means to use an installer that downloads the needed dependencies. The installer takes into account the platform (operating system), how the package is distributed, and the desired version. It then finds the matching download or fails with no match. If you are developing in the “python” folder, and your agent has dependent libraries, they will be placed in a folder specific to your Python environment (\~/.cache/pip, \~/Library/Caches/pip, or \<user>\appdata\local\pip\cache). The LangStream runtime creates a `PYTHONPATH` environment variable that looks for agent src in both the “python” and the “python/lib” folders.

When you are ready to package the agent for deployment to LangStream, use the following Docker commands to ensure the downloaded dependencies are compatible with the LangStream runtime environment (not your development environment). \
The command assumes you are running it from the “application” folder and your dependencies are declared in "python/requirements.txt"

```
docker run --rm \
    -v $(pwd)/python:/app-code-download \
    --entrypoint "" \
    ghcr.io/langstream/langstream-runtime:0.0.11 \
    /bin/bash -c 'pip3 install --target /app-code-download/python/lib --upgrade --prefer-binary -r requirements.txt'
```

{% hint style="info" %}
Note the version of LangStream was provided as the image’s tag. This should match the version of LangStream you are developing for.
{% endhint %}

**Unit testing**

Similar to packaging, the below Docker command is a starting suggestion of how to run your unit tests against the same environment the agent will run in LangStream.

Using unittest:

```
docker run --rm \
    -v $(pwd)/python:/app-code-download \
    --entrypoint "" \
    ghcr.io/langstream/langstream-runtime:0.0.11 \
    /bin/bash -c 'python3 -m unittest discover -s test'
```

Using tox:

```
docker run --rm \
    -v ${app_path}:/app-code-download \
    --entrypoint "" \
    ghcr.io/langstream/langstream-runtime:0.0.11 \
    /bin/bash -c 'tox'
```

#### Multiple Python apps in one LangStream application

If your LangStream application consists of more than one custom agent, it is recommended that you separate them into 2 different applications. They can share input or output topics or be put inline with one another indirectly by topic. Separating by application gives you two clear “python” folders to house your artifact. This will aid in dependency collisions and other effects of two apps trying to share the same folder.
