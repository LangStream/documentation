# Secrets

Learn more about the LangStream project [here](../about/what-is-langstream.md).

## Secrets

A place to hold secrets. Each label:value in this file is used as a reference in configuration and pipeline manifests. Their values carry on to a step’s environment where it is applied. Secret values can be modified directly in secrets.yaml, or you can [pass secrets as environment variables.](secrets.md#pass-secrets-as-environment-variables)

### Manifest

An example secrets.yaml manifest contains the credentials necessary to connect to Astra and OpenAI.

The `:-` characters designate a default value. For example, `provider: "${OPEN_AI_PROVIDER:-openai}"` designates `openai` as the default.

For finding these credentials, see [Credentials.](secrets.md#credentials)

```yaml
secrets:
  - id: astra
    data:
      clientId: ${ASTRA_CLIENT_ID:-}
      secret: ${ASTRA_SECRET:-}
      token: ${ASTRA_TOKEN:-}
      database: ${ASTRA_DATABASE:-}
      # uncomment this and link to a file containing the secure connect bundle
      # secureBundle: "<file:secure-connect-bundle.zip>"
      secureBundle: ${ASTRA_SECURE_BUNDLE:-}
      environment: ${ASTRA_ENVIRONMENT:-PROD}
  - id: open-ai
    data:
      access-key: "${OPEN_AI_ACCESS_KEY:-}"
      url: "${OPEN_AI_URL:-}"
      provider: "${OPEN_AI_PROVIDER:-openai}"
      embeddings-model: "${OPEN_AI_EMBEDDINGS_MODEL:-text-embedding-ada-002}"
      chat-completions-model: "${OPEN_AI_CHAT_COMPLETIONS_MODEL:-gpt-3.5-turbo}"
      text-completions-model: "${OPEN_AI_TEXT_COMPLETIONS_MODEL:-gpt-3.5-turbo-instruct}"
 
```

### Pass secrets as environment variables

Secret values can be modified directly in secrets.yaml, or you can pass your secrets as environment variables. The secrets.yaml resolves these environment variables.

```bash
export ASTRA_CLIENT_ID=...
export ASTRA_SECRET=...
export ASTRA_DATABASE=...
export ASTRA_TOKEN=...
```

When you go to production, you should create a dedicated secrets.yaml file for each environment.

### Credentials

Where do you find credentials for these items? Here's a little help:
<table>
  <thead>
    <tr>
      <th width="249.33333333333331">Secret</th>
      <th>Location</th>
      <th>Notes and Example Value</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>astra</strong></td><td></td><td></td></tr>
    <tr><td>clientID</td><td><a href="https://astra.datastax.com/">Astra</a></td><td>ASTRA_CLIENT_ID=fnsNZtMgvgBHurHJjfSbgQwifnsNZtMgvgBHurHJjfSbgQwi<br><br>ClientID is generated with token</td></tr>
    <tr><td>database</td><td><a href="https://astra.datastax.com">Astra</a></td><td><p>ASTRA_DATABASE=my-database</p><p>The name of your Astra database</p></td></tr>
    <tr><td>database-id</td><td><a href="https://astra.datastax.com">Astra</a></td><td>ASTRA_LANGCHAIN_DATABASE_ID</td></tr>
    <tr><td>environment</td><td><a href="https://astra.datastax.com">Astra</a></td><td>ASTRA_ENVIRONMENT=PROD</td></tr>
    <tr><td>keyspace</td><td><a href="https://astra.datastax.com">Astra</a></td><td>ASTRA_LANGCHAIN_KEYSPACE</td></tr>
    <tr><td>secret</td><td><a href="https://astra.datastax.com">Astra</a></td><td>ASTRA_SECRET=xxxx<br>Secret is generated with token</td></tr>
    <tr><td>secureBundle</td><td>Base64-encoded secure connect bundle downloaded from <a href="https://astra.datastax.com">Astra</a></td><td>ASTRA_SECURE_BUNDLE="<a href="file:secure-connect-bundle.zip">file:secure-connect-bundle.zip</a>"</td></tr>
    <tr><td>table</td><td><a href="https://astra.datastax.com">Astra</a></td><td>ASTRA_LANGCHAIN_TABLE</td></tr>
    <tr><td>token</td><td><a href="https://astra.datastax.com/">Astra</a></td><td>ASTRA_TOKEN=AstraCSxxxx</td></tr>
    <tr><td><strong>azure</strong></td><td></td><td></td></tr>
    <tr><td>container</td><td>Azure Storage</td><td>AZURE_STORAGE_CONTAINER_NAME</td></tr>
    <tr><td>storage-access-key</td><td>Azure Storage</td><td>AZURE_STORAGE_ACCESS_KEY</td></tr>
    <tr><td>storage-account-name</td><td>Azure Storage</td><td>AZURE_STORAGE_ACCOUNT_NAME</td></tr>
    <tr><td><strong>bedrock</strong></td><td></td><td></td></tr>
    <tr><td>access-key</td><td>Bedrock service</td><td>BEDROCK_ACCESS_KEY</td></tr>
    <tr><td>completions-model</td><td>Bedrock service</td><td>BEDROCK_COMPLETIONS_MODEL</td></tr>
    <tr><td>region</td><td>Bedrock service</td><td>REGION=us-east-1</td></tr>
    <tr><td>secret-key</td><td>Bedrock service</td><td>BEDROCK_SECRET_KEY</td></tr>
    <tr><td><strong>camel-github-source</strong></td><td></td><td></td></tr>
    <tr><td>branch</td><td>GitHub repository</td><td>CAMEL_GITHUB_BRANCH=main</td></tr>
    <tr><td>oauthToken</td><td>GitHub repository</td><td>CAMEL_GITHUB_OAUTH_TOKEN=xxxx</td></tr>
    <tr><td>repoName</td><td>GitHub repository</td><td>CAMEL_GITHUB_REPO_NAME=langstream</td></tr>
    <tr><td>repoOwner</td><td>GitHub repository</td><td>CAMEL_GITHUB_REPO_OWNER=langstream</td></tr>
    <tr><td>webhookSecret</td><td>GitHub repository</td><td>CAMEL_GITHUB_WEBHOOK_SECRET=xxxx</td></tr>
    <tr><td><strong>lang-smith</strong></td><td></td><td></td></tr>
    <tr><td>api-key</td><td><a href="https://smith.langchain.com/">LangSmith</a></td><td>LANGSMITH_APIKEY=xxxx</td></tr>
    <tr><td>api-url</td><<td><a href="https://smith.langchain.com/">LangSmith</a></td><td>LANGSMITH_API_URL=https://api.smith.langchain.com</td></tr>
    <tr><td><strong>slack</strong></td><td></td><td></td></tr>
    <tr><td>token</td><td><a href="https://api.slack.com/authentication">Slack</a></td><td>SLACK_TOKEN</td></tr>
    <tr><td>url</td><td><a href="https://api.slack.com/authentication">Slack</a></td><td>SLACK_URL</td></tr>
    <tr><td>provider</td><td><a href="https://api.slack.com/authentication">Slack</a></td><td>SLACK_PROVIDER</td></tr>
  </tbody>
</table>


Please note that the example values provided are taken from the current content and may not accurately reflect the actual values that should be used for each secret.

<table><thead><tr><th width="119">Root</th><th width="91">Node</th><th width="127">Type</th><th>Description</th></tr></thead><tbody><tr><td><br>secrets</td><td></td><td></td><td>The base node in the yaml, Holds the collection of secrets.</td></tr><tr><td></td><td>name</td><td><br></td><td>The secret name used for display</td></tr><tr><td></td><td>id</td><td><br></td><td>The id of the secret used for referencing its value</td></tr><tr><td></td><td>data</td><td>&#x3C;any key:value><br></td><td><p>Object of applicable values, given the secret. Provide any combination of key:value that is applicable to the given secret.</p><p>To retrieve the values use the format - secrets.&#x3C;name>.&#x3C;key><br><br>(don't include "data" when referencing secrets)</p></td></tr></tbody></table>
