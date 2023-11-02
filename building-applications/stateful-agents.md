# Stateful agents


This documentation page provides information on how to provision disks to agents for performing stateful computations- 
Provisioning disks to agents offers several benefits:

* **Stateful Computations**: Allows agents to retain data between computations, enabling the execution of complex, multi-step tasks.
* **Improved Efficiency**: Reduces the need to repeatedly fetch data from external sources, resulting in faster processing times.
* **Data Persistence**: Ensures that important data is not lost in case of agent restarts or failures.


```yaml
- name: "Stateful processing using Python"
  resources:
    disk:
      enabled: true
      size: 50M
    id: "my-python-processor"
    type: "python-processor"
```

Disks are automatically provided to agent at runtime by LangStream.
The agent must declare the `resources.disk` section to automatically ask for a persistent disk.
The provided disk are isolated from other agents and each agent can request different disk size and type.

The `disk` section provides these parameters:
- `enabled` (boolean): wheter to provide the disk or not.
- `size` (string): size of the disk to provision. e.g. 100K, 100M, 100G.
- `type` (string): type of the disk. 


At runtime LangStream converts the disk specification to the actual storage provisioner configured in the LangStream cluster.
The `type` option is statically mapped to a Kubernetes Storage class. The value `default` means to use the default Storage Class configured in Kubernetes.


Once you requested the disk, it's mounted in the local file system of the agent.
In Python, you can access the directory by calling `AgentContext.get_persistent_state_directory()`.

```python
from langstream import SimpleRecord, Processor, AgentContext

class Exclamation(Processor):
    def init(self, config, context: AgentContext):
        self.context = context

    def process(self, record):
        directory = self.context.get_persistent_state_directory()
        counter_file = os.path.join(directory, "counter.txt")
        ...
```
