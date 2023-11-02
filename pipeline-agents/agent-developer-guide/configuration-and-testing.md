---
description: Part 3 of the Agent Developer Guide
---
# Configuration and Testing

{% hint style="info" %}
This is Part 3 of the Agent Developer Guide. Start at the beginning [here.](./)
{% endhint %}

### Configuring the agent

Normally it’s a best practice to not hardcode credentials, settings, and other dynamic information an application may need. The LangStream runtime offers a way to provide configuration values at runtime to the agent. The values are declared in the pipeline.yaml manifest where the agent step is created, and are made available during the startup of the agent process as a Dictionary.

Given the labels declared in init:

```python
from typing import Dict, Any

def init(self, config: Dict[str, Any]):
  self.value1 = config.get("value1", "default value")
  self.value2 = config.get("value2", "default value")
```

The values would be passed to the agent in pipeline.yaml:

```yaml
pipeline:
  - name: "Load S3 documents and chunk them with LangChain"
    type: "python-source|python-sink|python-processor"
    output: "output-topic"
    input: "input-topic"
    configuration:
      className: example.MyAgent
      value1: "some-config-value" # as string
      value2: "${ secrets.my-app.some-secret-value}" # as a secret ref
```

### Testing and packaging the agent

During development, it’s best to follow the [12 factors](https://12factor.net/) as closely as possible - specifically parity between environments. You should be developing an agent locally using the same (or near similar) environment it will run within on LangStream. Our approach to reach environment parity is to use Docker as a test and packaging environment.

Python is a cross-platform runtime. Given a list of dependent packages (requirements.txt), the installation of an app should be augmented/fail based on what operating system is being used. While most installers offer the option of declaratively providing what platform the install should provision for, if you’ve ever attempted this you know there are quite a few caveats that come with that promise. To achieve a reproducible, iterable result, it’s best to package and test in an environment matching production.

#### **Packaging**

When you are creating a LangStream agent, you aren’t creating a proper Python package. It’s more akin to creating a cloud function (think Lambda). Given the [folder structure of a LangStream application](https://docs.langstream.ai/building-applications/development-environment), inside the “application” folder, your agent source code will go inside a “python” folder. It’s encouraged to develop the agent in that folder. Given that some agents are one simple .py file, there’s no need to create a separate development environment.

To build an application in Python means to use an installer that downloads the needed dependencies. The installer takes into account the platform (operating system), how the package is distributed, and the desired version. It then finds the matching download or fails with no match. If you are developing in the “python” folder, and your agent has dependent libraries, they will be placed in a folder specific to your Python environment (\~/.cache/pip, \~/Library/Caches/pip, or \<user>\appdata\local\pip\cache). The LangStream runtime creates a `PYTHONPATH` environment variable that looks for agent src in both the “python” and the “python/lib” folders.

When you are ready to package the agent for deployment to LangStream, use the following Docker commands to ensure the downloaded dependencies are compatible with the LangStream runtime environment (not your development environment). \
The command assumes you are running it from the “application” folder and your dependencies are declared in "python/requirements.txt"

```bash

langstream python load-pip-requirements -app /path/to/application

```

{% hint style="info" %}
The command above will create a “python/lib” folder with the dependencies installed. This folder is added to the PYTHONPATH environment variable when the agent is run on LangStream. It uses the same docker image as the runtime, with the same version of Python and of the core libraries that will run in production.
This is very important, especiacially if you are using Mac or Windows to develop your agent.
{% endhint %}

#### **Unit testing**

Similar to packaging, the below Docker command is a starting suggestion of how to run your unit tests against the same environment the agent will run in LangStream.

Using unittest:

```bash
langstream python run-tests -app /path/to/application 
```

Using tox:

```bash
langstream python run-tests -app /path/to/application -c tox
```

### Multiple Python apps with dependency conflicts

If your LangStream application consists of more than one custom agent and you have dependencies conflicts, it is recommended that you separate them into 2 different applications. They can share input or output topics or be put inline with one another indirectly by topic. Separating by application gives you two clear “python” folders to house your artifact. This will aid in dependency collisions and other effects of two apps trying to share the same folder.


### What's next?

Continue on to Part 4 of the Agent Developer Guide, [Environment variables.](enviroment.md)
