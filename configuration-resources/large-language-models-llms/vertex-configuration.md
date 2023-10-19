# vertex-configuration

A vertex-configuration resource is used for AI agents.

`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "vertex-configuration"
      name: "Google Vertex AI configuration"
      configuration:
        url: "${ secrets.vertex.url }"
        region: "${ secrets.vertex.region }"
        project: "${ secrets.vertex.project }"
        # Authentication is done either via service account JSON
        serviceAccountJson: "${ secrets.vertex.service-account-json }"
        # or token
        token: "${ secrets.vertex.token }"
```

`secrets.yaml`
```yaml
secrets:
  - id: vertex
    data:
      url: "${VERTEX_URL:-https://us-central1-aiplatform.googleapis.com}"
      region: "${VERTEX_REGION:-us-central1}"
      project: "${VERTEX_PROJECT:-my-gcp-project}"
      service-account-json: "<file:service-account-json.json>"
      token: "${VERTEX_TOKEN:-xxx}"
```

For authenticating it's suggested to use the service account JSON since tokens are normally generated with a short TTL.


## Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/resources.md#vertex-configuration).