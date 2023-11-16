# ollama-configuration

The resource `ollama-configuration` configures access to the Ollama models for embeddings and completions via the Ollama REST API.

Check out the docs at [Ollama.ai](https://github.com/jmorganca/ollama) to learn more about how to start it locally.

`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "ollama-configuration"
      name: "ollama"
      configuration:
        url: "${secrets.ollama.url}"
```

`secrets.yaml`
```yaml
secrets:
  - name: ollama
    id: ollama
    data:
      url: "${OLLAMA_URL:-http://host.docker.internal:11434}"
```

This example uses host.docker.internal at the default Ollama port 11434,. This works well if you are running Ollama
on your local machine with LangStream in Docker.


## Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#ollama-configuration).