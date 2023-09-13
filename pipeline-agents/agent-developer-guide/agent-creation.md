# Agent Creation

{% hint style="info" %}
This is Part 2 of the Agent Developer Guide. Start at the beginning [here.](./)
{% endhint %}

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

### Agent records

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

### Creating agents

#### **Source**

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

Handling Exceptions

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

#### **Sink**

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

Handling Exceptions

Ideally the python app catches and handles exceptions that occur while committing a record to a sink. If an exception goes uncaught in the agent process, the LangStream runtime will follow the failure management strategy declared in pipeline error spec. This gives the developer tools to prevent pod restarts.

#### **Processor**

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

Handling Exceptions

The processor agent has a special return type `List[Tuple[Record, Union[List[Record], Exception]]]` that has provisions for including an Exception rather than the Record(s). If an exception is provided in the return, the LangStream runtime will follow the failure management strategy declared in pipeline error spec. This gives the developer tools to prevent pod restarts.

Single Record Processor

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

### What's next?

Continue on to Part 3 of the Agent Developer Guide, [Configuration and Testing.](configuration-and-testing.md)
