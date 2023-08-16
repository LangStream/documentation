# vertex-configuration

A Google vertex configuration.

```yaml
configuration:
  resources:
    - type: "vertex-configuration"
      name: "Google Vertex AI configuration"
      configuration:
        url: "{{ secrets.vertex-ai.url }}"
        # use triple quotes in order to turn off escaping
        serviceAccountJson: "{{{ secrets.vertex-ai.serviceAccountJson }}}"
        token: "{{ secrets.vertex-ai.token }}"
        region: "{{ secrets.vertex-ai.region }}"
        project: "{{ secrets.vertex-ai.project }}"
```

### **Configuration values**

<table><thead><tr><th width="229.33333333333331">Label</th><th width="110">Type</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td><br>String</td><td><p>Connection to Vertex API. Typically this is a reference to a secret.</p><p></p><p>Example: “{{ secrets.vertex-ai.url }}”</p></td></tr><tr><td>serviceAccountJson</td><td><br>String</td><td><p>Specify a custom service account. If you don't specify a service account, Vertex AI Pipelines runs your pipeline using the default Compute Engine service account.</p><p><br>Example: "{{{ secrets.vertex-ai.serviceAccountJson }}}"</p></td></tr><tr><td>token</td><td><br>String</td><td><p>Access key for the Vertex API. Typically this is a reference to a secret.</p><p><br>"{{ secrets.vertex-ai.token }}"</p></td></tr><tr><td>region</td><td>String<br></td><td><p>Region for the Vertex API. Typically this is a reference to a secret:</p><p><br>"{{ secrets.vertex-ai.region }}"<br><br>The region will look like this: </p><p>"us-central-1"</p></td></tr><tr><td>project</td><td>String<br></td><td>Project name for the Vertex API. Typically this is a reference to a secret:<br>"{{ secrets.vertex-ai.project }}"</td></tr></tbody></table>
