# CLI Configuration

Use the LangStream CLI to manage your control plane, deploy applications, and interact with an application's gateway.

For LangStream CLI commands, see [CLI Commands](langstream-cli-commands.md).&#x20;

To install the CLI, see [Installation](../installation/langstream-cli.md).

## Langstream profiles

LangStream profiles replace the `langstream configure` option, which is now deprecated.

Profiles are created by users to interact with different LangStream environments. For example, you could have a "local" profile to test your application locally, and a "stage" profile to deploy your changes to a shared development space.

The default LangStream profile values for a local deployment are:

```
webServiceUrl: "http://localhost:8090"
apiGatewayUrl: "ws://localhost:8091"
tenant: "default"
token: null
```

To create a new profile for a staging environment and set it as the current LangStream profile, use:

```
langstream profiles create staging \
--web-service-url="https://pulsar-gcp-useast1.api.streaming.datastax.com" \
--tenant="staging-tenant" \
--set-current
```

To update these values in the "staging" profile, use `langstream profiles update staging --command-option="value"`.

| Command Option    | Description                  |
| ----------------- | ---------------------------- |
| --set-current     | Set this profile as current  |
| --web-service-url | webServiceUrl of the profile |
| --api-gateway-url | apiGatewayUrl of the profile |
| --tenant          | tenant of the profile        |
| --token           | token of the profile         |

For more profile commands, see [Profiles](langstream-cli-commands.md#profiles).

## Multi tenancy

LangStream is multi-tenant. You can create multiple tenants and deploy applications to them. Each tenant has its own control plane and API gateway. When you first install LangStream, a **default** tenant is created for you. You can use this tenant or create a new one. This works well if you are running LangStream locally, but if you are running LangStream in a cluster, you will need to create a new tenant.

The CLI is able to handle multiple profiles, and each profile defines:

* the tenant
* the control plane URL
* the API gateway URL
* the credentials to connect to the control plane (currently there is support for a token, that can be a JWT or OAuth2 token, depending on the authentication method used by the control plane)

These commands will help you manage your profiles and the tenant you are currenly using:

```
langstream profiles list
langstream profiles get-current
langstream profiles get default
```

All the commands always refer to the current tenant configured in the current profile.

## Configure env vars

<table data-header-hidden><thead><tr><th width="295">Var label</th><th>Description</th></tr></thead><tbody><tr><td>LANGSTREAM_webServiceUrl</td><td><p>The fully qualified URL to the control plane service</p><p><br></p><p>Example: https://controlplane.my-domain.com:XXX</p></td></tr><tr><td>LANGSTREAM_tenant</td><td>The tenant to use for app interactions</td></tr><tr><td>LANGSTREAM_apiGatewayUrl</td><td>The fully qualified URL to the gateway api service</td></tr><tr><td>LANGSTREAM_token</td><td>unused</td></tr></tbody></table>
