# Secrets

Learn more about the LangStream project [here](../about/what-is-langstream.md).

## Secrets

A place to hold secrets. Each label:value in this file is used as a reference in configuration and pipeline manifests. Their values carry on to a step’s environment where it is applied.\
\
Secret values can be modified directly in secrets.yaml, or you can [pass secrets as environment variables.](secrets.md#pass-secrets-as-environmental-variables)

### Manifest

An example secrets.yaml manifest contains the credentials necessary to connect to Astra and OpenAI.

For finding these credentials, see [Credentials.](secrets.md#credentials)

```yaml
secrets:
  - id: astra
    data:
      clientId: ${ASTRA_CLIENT_ID:-}
      secret: ${ASTRA_SECRET:-}
      token: ${ASTRA_TOKEN:-}
      database: ${ASTRA_DATABASE:-}
      secureBundle: ${ASTRA_SECURE_BUNDLE:-}
      environment: ${ASTRA_ENVIRONMENT:-PROD}
  - id: open-ai
    data:
      access-key: "${OPEN_AI_ACCESS_KEY:-}"
      url: "${OPEN_AI_URL:-}"
      provider: "${OPEN_AI_PROVIDER:-azure}"
      embeddings-model: "${OPEN_AI_EMBEDDINGS_MODEL:-text-embedding-ada-002}"
      chat-completions-model: "${OPEN_AI_CHAT_COMPLETIONS_MODEL:-gpt-35-turbo}"
```

### Pass secrets as environment variables

Secret values can be modified directly in secrets.yaml, or you can pass your secrets as environment variables. The secrets.yaml resolves these environment variables.&#x20;

```
export ASTRA_CLIENT_ID=...
export ASTRA_SECRET=...
export ASTRA_DATABASE=...
export ASTRA_TOKEN=...
```

When you go to production, you should create a dedicated secrets.yaml file for each environment.

### Credentials

Where do you find credentials for these items? Here's a little help:

<table><thead><tr><th width="249.33333333333331">Secret</th><th>Location</th><th>Notes and Example Value</th></tr></thead><tbody><tr><td><strong>kafka</strong></td><td></td><td></td></tr><tr><td>username</td><td>ssl.properties</td><td>KAFKA_USERNAME=langstream-tenant</td></tr><tr><td>password</td><td>ssl.properties</td><td>KAFKA_PASSWORD=token:eyXxx... </td></tr><tr><td>tenant</td><td>ssl.properties</td><td>KAFKA_USERNAME=langstream-tenant</td></tr><tr><td>bootstrap.servers</td><td>ssl.properties</td><td>KAFKA_BOOTSTRAP_SERVERS=kafka-gcp-useast1.streaming.datastax.com:9093</td></tr><tr><td><strong>open-ai</strong></td><td></td><td></td></tr><tr><td>access-key</td><td><a href="https://platform.openai.com/">OpenAI Access Key</a></td><td>access-key: xxx</td></tr><tr><td>url</td><td><a href="https://azure.microsoft.com/en-us/products/ai-services/openai-service">OpenAI Azure URL</a></td><td>url: https://company-openai-dev.openai.azure.com/</td></tr><tr><td>provider</td><td><a href="https://azure.microsoft.com/en-us/products/ai-services/openai-service">OpenAI Azure</a></td><td>provider:openai</td></tr><tr><td>embeddings-model</td><td><a href="https://azure.microsoft.com/en-us/products/ai-services/openai-service">OpenAI Azure</a></td><td>OPEN_AI_EMBEDDINGS_MODEL=text-embedding-ada-002 export </td></tr><tr><td>chat-completions-model</td><td><a href="https://azure.microsoft.com/en-us/products/ai-services/openai-service">OpenAI Azure</a></td><td>OPEN_AI_CHAT_COMPLETIONS_MODEL=gpt-35-turbo</td></tr><tr><td><strong>vertex-ai</strong></td><td></td><td></td></tr><tr><td>url</td><td><a href="https://developers.google.com/identity/protocols/oauth2#serviceaccount">Google Service Account</a></td><td>url: https://us-central1-aiplatform.googleapis.com</td></tr><tr><td>token</td><td><a href="https://cloud.google.com/vertex-ai/docs/workbench/reference/authentication">Vertex API token</a></td><td>token: xxx</td></tr><tr><td>serviceAccountJSON</td><td>A JSON file downloaded from the Google console containing auth info.</td><td>serviceAccountJson: xxx</td></tr><tr><td>region</td><td><a href="https://developers.google.com/identity/protocols/oauth2#serviceaccount">Google Service Account</a></td><td>region: us-central1</td></tr><tr><td>project</td><td><a href="https://developers.google.com/identity/protocols/oauth2#serviceaccount">Google Service Account</a></td><td>project: myproject</td></tr><tr><td><strong>hugging-face</strong></td><td></td><td></td></tr><tr><td>access-key</td><td><a href="https://huggingface.co/docs/hub/security-tokens">hugging-face</a></td><td>access-key:</td></tr><tr><td><strong>astra</strong></td><td></td><td></td></tr><tr><td>clientID</td><td><a href="https://astra.datastax.com/">Astra clientID</a></td><td>username: fnsNZtMgvgBHurHJjfSbgQwifnsNZtMgvgBHurHJjfSbgQwi<br><br>ClientID is generated with token</td></tr><tr><td>secret</td><td><a href="https://astra.datastax.com">Astra secret</a></td><td>Secret is generated with token</td></tr><tr><td>token</td><td><a href="https://astra.datastax.com/">Astra token</a></td><td>password: AstraCSxxxx</td></tr><tr><td>database</td><td><a href="https://astra.datastax.com">Astra database</a></td><td>The name of your Astra database</td></tr><tr><td>secureBundle</td><td>Base64-encoded secure connect bundle downloaded from Astra</td><td>secureBundle: $(base64 ./secure-connect-my-database.zip > ./b64.txt)</td></tr><tr><td>environment</td><td><a href="https://astra.datastax.com">Astra environment</a></td><td>-PROD</td></tr><tr><td><strong>s3</strong></td><td></td><td></td></tr><tr><td>bucket-name</td><td><a href="https://min.io/docs/minio/kubernetes/upstream/">Minio console</a></td><td>bucketName: "langstream-code-storage"</td></tr><tr><td>endpoint</td><td><a href="https://min.io/docs/minio/kubernetes/upstream/">Minio console</a></td><td>endpoint: "http://minio.minio-dev.svc.cluster.local:9000"</td></tr><tr><td>access-key</td><td><a href="https://min.io/docs/minio/kubernetes/upstream/">Minio console</a></td><td>username: "minioadmin"</td></tr><tr><td>secret</td><td><a href="https://min.io/docs/minio/kubernetes/upstream/">Minio console</a></td><td>password: "minioadmin"</td></tr><tr><td>region</td><td><a href="https://min.io/docs/minio/kubernetes/upstream/">Minio console</a></td><td></td></tr><tr><td><strong>google</strong></td><td></td><td></td></tr><tr><td>client-id</td><td><a href="https://developers.google.com/identity/protocols/oauth2#serviceaccount">Google Service Account</a></td><td>client-id: xxxx</td></tr><tr><td><strong>github</strong></td><td></td><td></td></tr><tr><td>client-id</td><td><a href="https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authenticating-to-the-rest-api-with-an-oauth-app">Github</a></td><td>client-id: xxxx</td></tr><tr><td><strong>pinecone</strong></td><td></td><td></td></tr><tr><td>service</td><td><a href="https://app.pinecone.io/">Pinecone console</a></td><td>service: "pinecone"</td></tr><tr><td>access-key</td><td><a href="https://app.pinecone.io/">Pinecone console</a></td><td>api-key: ""</td></tr><tr><td>project-name</td><td><a href="https://app.pinecone.io/">Pinecone console</a></td><td>project-name: "b4ea705"</td></tr><tr><td>environment</td><td><a href="https://app.pinecone.io/">Pinecone console</a></td><td>environment: "asia-southeast1-gcp-free"</td></tr><tr><td>index-name</td><td><a href="https://app.pinecone.io/">Pinecone console</a></td><td>index-name: "my-pinecone-index"</td></tr></tbody></table>

Please note that the example values provided are taken from the current content and may not accurately reflect the actual values that should be used for each secret.

<table><thead><tr><th width="119">Root</th><th width="91">Node</th><th width="127">Type</th><th>Description</th></tr></thead><tbody><tr><td><br>secrets</td><td></td><td></td><td>The base node in the yaml, Holds the collection of secrets.</td></tr><tr><td></td><td>name</td><td><br></td><td>The secret name used for display</td></tr><tr><td></td><td>id</td><td><br></td><td>The id of the secret used for referencing its value</td></tr><tr><td></td><td>data</td><td>&#x3C;any key:value><br></td><td><p>Object of applicable values, given the secret. Provide any combination of key:value that is applicable to the given secret.</p><p></p><p>To retrieve the values use the format - secrets.&#x3C;name>.&#x3C;key><br><br>(don't include "data" when referencing secrets)</p></td></tr></tbody></table>
