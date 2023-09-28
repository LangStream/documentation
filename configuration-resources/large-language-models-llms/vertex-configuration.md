# vertex-configuration

A vertex-configuration resource is used for AI agents.

Note that the following examples sets sensitive data as plain text. This is for education purpose only, it's highly recommended to use [secrets](../../building-applications/secrets.md).


```yaml
configuration:
  resources:
    - type: "vertex-configuration"
      name: "Google Vertex AI configuration"
      configuration:
        url: "https://us-central1-aiplatform.googleapis.com"
        region: "us-central1"
        project: "my-gcp-project"
        # Authentication is done either via service account JSON
        serviceAccountJson: "{\"type\":..........}"
        # or token
        token: "{{ secrets.vertex-ai.token }}"
```

For authenticating it's suggested to use the service account JSON since tokens are normally generated with a short TTL.

## API Reference

<table><thead><tr><th width="229.33333333333331">Label</th><th width="110">Type</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td><br>String</td><td><p>Connection to Vertex API. Typically this is a reference to a secret.</p><p></p><p>Example: “{{ secrets.vertex-ai.url }}”</p></td></tr><tr><td>serviceAccountJson</td><td><br>String</td><td><p>Specify a custom service account. If you don't specify a service account, Vertex AI Pipelines runs your pipeline using the default Compute Engine service account.</p><p><br>Example: "{{{ secrets.vertex-ai.serviceAccountJson }}}"</p></td></tr><tr><td>token</td><td><br>String</td><td><p>Access key for the Vertex API. Typically this is a reference to a secret.</p><p><br>"{{ secrets.vertex-ai.token }}"</p></td></tr><tr><td>region</td><td>String<br></td><td><p>Region for the Vertex API. Typically this is a reference to a secret:</p><p><br>"{{ secrets.vertex-ai.region }}"<br><br>The region will look like this: </p><p>"us-central-1"</p></td></tr><tr><td>project</td><td>String<br></td><td>Project name for the Vertex API. Typically this is a reference to a secret:<br>"{{ secrets.vertex-ai.project }}"</td></tr></tbody></table>
