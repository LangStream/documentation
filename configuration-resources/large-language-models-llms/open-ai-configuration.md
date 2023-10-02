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


## API reference
<table><thead><tr><th width="158.33333333333331">Labele</th><th width="111">Type</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>string</td><td><p><b>Only for Azure OpenAI provider</b>Base url for the OpenAI api. </p><p></p><p>Example: https://COMPANY.openai.azure.com</p></td></tr><tr><td>access-key</td><td>string</td><td><p>Your OpenAI key</p><p></p></td></tr><tr><td>provider</td><td>string</td><td><p>OpenAI provider type. Supported values are:</p><ul><li>“openai” (default)</li><li>“azure”</li></ul></td></tr></tbody></table>
