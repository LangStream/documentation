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

This example uses host.docker.internal, that works well in case you are runnning Ollama
on your local machine and run LangStream in docker.


## Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#ollama-configuration).