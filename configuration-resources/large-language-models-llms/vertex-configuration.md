# vertex-configuration

A vertex-configuration resource is used for AI agents.

`configuration.yaml`
```yaml
configuration:
  resources:
    - type: "vertex-configuration"
      name: "Google Vertex AI configuration"
      configuration:
        url: "{{{ secrets.vertex.url }}}"
        region: "{{{ secrets.vertex.region }}}"
        project: "{{{ secrets.vertex.project }}}"
        # Authentication is done either via service account JSON
        serviceAccountJson: "{{{ secrets.vertex.service-account-json }}}"
        # or token
        token: "{{{ secrets.vertex.token }}}"
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


## API Reference

<table><thead><tr><th width="229.33333333333331">Label</th><th width="110">Type</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td><br>String</td><td><p>URL connection for the Vertex API.</p></td></tr><tr><td>serviceAccountJson</td><td><br>String</td><td><p>Specify a custom service account. Refer to the <a href="https://cloud.google.com/iam/docs/keys-create-delete">GCP documentation</a> on how to download it</p></td></tr><tr><td>token</td><td><br>String</td><td><p>Access key for the Vertex API. You can generate a short-life token with <code>gcloud auth print-access-token</code>.</p></td></tr><tr><td>region</td><td>String<br></td><td><p>GCP region for the Vertex API. </p></td></tr><tr><td>project</td><td>String<br></td><td>GCP project name for the Vertex API.</td></tr></tbody></table>
