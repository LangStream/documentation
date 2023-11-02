# Using Pravega.io

Configuration for a LangStream streaming instance.

Please note that support for Pravega.io is still experimental and is not recommended for production use.

### Configuration

Connect to a Pravega broker with the following configuration:
- The Controller URI
- The Scope

In Pravega, a scope is like a tenant, which is a namespace for your topics.
In Pravega the topics are called "streams".

### Examples

Configuration for a Pravega.io standalone instance looks like this:

```yaml
    streamingCluster:
    type: "pravega"
    configuration:
        client:
            controller-uri: "tcp://localhost:9090"
            scope: "langstream"        
```

Start the Pravega standalone instance with this command:
    
```bash
docker run -it --rm -p 9090:9090 -e HOST_IP=host.docker.internal -p 12345:12345 pravega/pravega:0.13.0 standalone
```

Start the LangStream docker chatbot example with this command:

```bash
export OPEN_AI_ACCESS_KEY=your-key-here
langstream docker run test \
   -app https://github.com/LangStream/langstream/blob/main/examples/applications/openai-completions \
   -s https://github.com/LangStream/langstream/blob/main/examples/secrets/secrets.yaml \
   -i https://github.com/LangStream/langstream/blob/main/examples/instances/pravega-docker.yaml
```
