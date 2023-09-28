# hugging-face-configuration

A huggingface resource used for LLM functions.


Note that the following examples sets sensitive data as plain text. This is for education purpose only, it's highly recommended to use [secrets](../../building-applications/secrets.md).



```yaml
configuration:
  resources:
    - type: "hugging-face-configuration"
      name: "Hugging Face AI configuration"
      configuration:
        access-key: "hf-access-key"
```



### API Reference

<table><thead><tr><th width="158.33333333333331">Label</th><th width="139">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-key</td><td><br></td><td><p>Your hugging face token. </p></td></tr><tr><td>inference-url</td><td><br></td><td><p>Hugging face inference url.</p><p></p><p>Default value is <code>https://api-inference.huggingface.co</code></p></td></tr></tbody></table>
