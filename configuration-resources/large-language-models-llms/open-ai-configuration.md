# open-ai-configuration

An OpenAI resource is used for AI agents.

## OpenAI

`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "open-ai-configuration"
      name: "OpenAI"
      configuration:
        access-key: "${ secrets.open-ai.access-key }"
```

`secrets.yaml`
```yaml
secrets:
  - id: open-ai
    data:
      access-key: ${OPEN_AI_ACCESS_KEY}
```

## Azure OpenAI

`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "open-ai-configuration"
      name: "OpenAI Azure"
      configuration:
        url: "${ secrets.azure-open-ai.url }"
        access-key: "${ secrets.azure-open-ai.access-key }"
        provider: "azure"
```

`secrets.yaml`
```yaml
secrets:
  - id: azure-open-ai
    data:
      url: "${AZURE_URL:-https://COMPANY.openai.azure.com}"
      access-key: "${AZURE_ACCESS_KEY}"
```

## Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#open-ai-configuration).
