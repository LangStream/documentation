# hugging-face-configuration

A huggingface resource used for LLM functions.


`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "hugging-face-configuration"
      name: "Hugging Face AI configuration"
      configuration:
        access-key: "${ secrets.hugging-face.access-key }"
```

`secrets.yaml`
```yaml
secrets:
  - id: hugging-face
    data:
      access-key: "${HF_ACCESS_KEY}"
```
## Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#hugging-face-configuration).
