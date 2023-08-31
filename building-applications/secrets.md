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

### Credentials

Where do you find credentials for these items? Here's a little help:

| Secret       | Location                                                                                                                  | Example Value                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| astra-token  | [Astra Streaming](https://astra.datastax.com/)                                                                            | token: eyXxx...                                                      |
|              | [AS tenant](https://astra.datastax.com/)                                                                                  | tenant: mytenant                                                     |
|              | [AS namespace](https://astra.datastax.com/)                                                                               | namespace: default                                                   |
| open-ai      | [OpenAI Access Key](https://platform.openai.com/)                                                                         | access-key: xxx                                                      |
|              | [OpenAI Azure URL](https://azure.microsoft.com/en-us/products/ai-services/openai-service)                                 | url: https://company-openai-dev.openai.azure.com/                    |
| vertex-ai    | [Google Service Account](https://developers.google.com/identity/protocols/oauth2#serviceaccount)                          | url: https://us-central1-aiplatform.googleapis.com                   |
|              | [Vertex API token](https://cloud.google.com/vertex-ai/docs/workbench/reference/authentication)                            | token: xxx                                                           |
|              | A JSON file downloaded from the Google console containing auth info.                                                      | serviceAccountJson: xxx                                              |
|              |                                                                                                                           | region: us-central1                                                  |
|              |                                                                                                                           | project: myproject                                                   |
| hugging-face | [hugging-face](https://huggingface.co/docs/hub/security-tokens)                                                           | access-key:                                                          |
| astra        | [Astra clientID](https://astra.datastax.com/)                                                                             | username: fnsNZtMgvgBHurHJjfSbgQwifnsNZtMgvgBHurHJjfSbgQwi           |
|              | [Astra token](https://astra.datastax.com/)                                                                                | password: AstraCSxxxx                                                |
|              | Base64-encoded secure connect bundle downloaded from Astra                                                                | secureBundle: $(base64 ./secure-connect-my-database.zip > ./b64.txt) |
| s3           | [Minio console](https://min.io/docs/minio/kubernetes/upstream/)                                                           | bucketName: "langstream-code-storage"                                |
|              |                                                                                                                           | endpoint: "http://minio.minio-dev.svc.cluster.local:9000"            |
|              |                                                                                                                           | username: "minioadmin"                                               |
|              |                                                                                                                           | password: "minioadmin"                                               |
| google       | [Google Service Account](https://developers.google.com/identity/protocols/oauth2#serviceaccount)                          | client-id: xxxx                                                      |
| github       | [Github](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app) | client-id: xxxx                                                      |
| pinecone     | [Pinecone console](https://app.pinecone.io/)                                                                              | service: "pinecone"                                                  |
|              |                                                                                                                           | api-key: ""                                                          |
|              |                                                                                                                           | project-name: "b4ea705"                                              |
|              |                                                                                                                           | environment: "asia-southeast1-gcp-free"                              |
|              |                                                                                                                           | index-name: "my-pinecone-index"                                      |

Please note that the example values provided are taken from the current content and may not accurately reflect the actual values that should be used for each secret.

<table><thead><tr><th width="119">Root</th><th width="91">Node</th><th width="127">Type</th><th>Description</th></tr></thead><tbody><tr><td><br>secrets</td><td></td><td></td><td>The base node in the yaml, Holds the collection of secrets.</td></tr><tr><td></td><td>name</td><td><br></td><td>The secret name used for display</td></tr><tr><td></td><td>id</td><td><br></td><td>The id of the secret used for referencing its value</td></tr><tr><td></td><td>data</td><td>&#x3C;any key:value><br></td><td><p>Object of applicable values, given the secret. Provide any combination of key:value that is applicable to the given secret.</p><p></p><p>To retrieve the values use the format - secrets.&#x3C;name>.&#x3C;key><br><br>(don't include "data" when referencing secrets)</p></td></tr></tbody></table>
