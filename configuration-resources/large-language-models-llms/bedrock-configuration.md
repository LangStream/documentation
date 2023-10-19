# open-ai-configuration

The resource `bedrock-configuration` allows you to configure the access to the Amazon Bedrock models for embeddings and completions.

`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "bedrock-configuration"
      name: "Bedrock"
      configuration:
        access-key: "${secrets.bedrock.access-key}"
        secret-key: "${secrets.bedrock.secret-key}"
        region: "${secrets.bedrock.region}"
```

`secrets.yaml`
```yaml
secrets:
  - id: bedrock
    data:
      access-key: "${BEDROCK_ACCESS_KEY}"
      secret-key: "${BEDROCK_SECRET_KEY}"
      region: "${BEDROCK_REGION}"
```


## Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#bedrock-configuration).