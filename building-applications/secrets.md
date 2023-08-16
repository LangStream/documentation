# Secrets

Learn more about the LangStream project [here](../about/what-is-langstream.md).

## Secrets

A place to hold secrets. Each label:value in this file is used as a reference in configuration and pipeline manifests. Their values carry on to a step’s environment where it is applied.

### Manifest

```yaml
secrets:
  - name: astra-token
    id: astra-token
    data:
      token: xxx
      tenant: mytenant
      namespace: default
  - name: open-ai
    id: open-ai
    data:
      access-key: xxx
```

\


<table><thead><tr><th width="119">Root</th><th width="91">Node</th><th width="127">Type</th><th>Description</th></tr></thead><tbody><tr><td><br>secrets</td><td></td><td></td><td>The base node in the yaml, Holds the collection of secrets.</td></tr><tr><td></td><td>name</td><td><br></td><td>The secret name used for display</td></tr><tr><td></td><td>id</td><td><br></td><td>The id of the secret used for referencing its value</td></tr><tr><td></td><td>data</td><td>&#x3C;any key:value><br></td><td><p>Object of applicable values, given the secret. Provide any combination of key:value that is applicable to the given secret.</p><p></p><p>To retrieve the values use the format - secrets.&#x3C;name>.&#x3C;key><br><br>(don't include "data" when referencing secrets)</p></td></tr></tbody></table>
