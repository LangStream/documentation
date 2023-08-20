# LangStream CLI

Use the CLI to manage your control plane, deploy applications, and interact with an application's gateway.

### Download the CLI

#### Mac

```
brew tap LangStream/langstream
brew install langstream
```

#### Linux

```bash
curl -Ls "https://raw.githubusercontent.com/LangStream/langstream/main/bin/get-cli.sh" | bash
```

#### Windows

Use [WSL](https://learn.microsoft.com/en-us/windows/wsl/about).

### Confirm the installation

Once installed you can test the CLI with the following command.

```
langstream -h
```

### Commands

<table data-full-width="false"><thead><tr><th width="125">Command</th><th width="120">Directive</th><th>Description</th><th>Arguments example</th></tr></thead><tbody><tr><td>tenants</td><td><br></td><td>Manage tenants</td><td><br></td></tr><tr><td><br></td><td>delete</td><td>Remove a tenant</td><td><p>tenantId: the id of a tenant</p><p><br></p><p>Example: langstream tenants delete “a-tenant”</p></td></tr><tr><td><br></td><td>get</td><td>Get tenant configuration</td><td><p>tenantId: the id of a tenant</p><p><br></p><p>Example: langstream tenants get “a-tenant”</p></td></tr><tr><td><br></td><td>list</td><td>List all tenants</td><td><p><br><br></p><p>Example: langstream tenants list</p></td></tr><tr><td><br></td><td>put</td><td>Save a tenant</td><td><p>tenantId: the id of a tenant</p><p><br></p><p>Example: langstream tenants put “a-tenant”</p></td></tr><tr><td>apps</td><td><br></td><td>Manage applications</td><td><br></td></tr><tr><td><br></td><td>list</td><td>List all applications</td><td><p><br><br></p><p>Example: langstream apps list</p></td></tr><tr><td><br></td><td>get</td><td>Get application status</td><td><p>applicationId: the id of the application</p><p>-o: optional output format, supported values are “json”, “yaml”, “raw”. Default is “raw”.</p><p><br></p><p>Example: langstream apps get “some-app-id”</p></td></tr><tr><td><br></td><td>delete</td><td>Remove an application</td><td><p>Name : application name</p><p><br></p><p>Example: langstream apps delete “some-app-id”</p></td></tr><tr><td><br></td><td>deploy</td><td>Deploy a new application</td><td><p>applicationId: the id of the application</p><p>–app | –application: application directory path REQUIRED<br>-i: instance file path REUQIRED</p><p>-s: secrets file path OPTIONAL</p><p><br></p><p>Learn more about the contents of the application directory <a href="../building-applications/development-environment.md">here.</a></p><p><br></p><p>Example: langstream apps deploy my-app-id \</p><p>    --app “./my-app-files” \</p><p>    --i “./instances.yaml”\</p><p>    --s “./secrets.yaml”</p></td></tr><tr><td><br></td><td>update</td><td>Update an existing application</td><td><p>applicationId: the id of the application</p><p>–app | –application: application directory path REQUIRED<br>-i: instance file path REQUIRED</p><p>-s: secrets file path OPTIONAL</p><p><br></p><p>Learn more about the contents of the application directory <a href="../building-applications/development-environment.md">here.</a></p><p><br></p><p>Example: langstream apps update my-app-id \</p><p>    --app “./my-app-files” \</p><p>    --i “./instances.yaml”\</p><p>    --s “./secrets.yaml”</p></td></tr><tr><td><br></td><td>logs</td><td>Get application logs</td><td><p>applicationId: the id of the application</p><p>-f : filter by worker id, comma delimited list</p><p><br></p><p>Example: langstream apps logs my-app-id  -f “some-app-worker, another-app-worker”</p></td></tr><tr><td>configure</td><td><br></td><td>Configure tenant and authentication</td><td><br></td></tr><tr><td><br></td><td>tenant</td><td>Tenant name</td><td><p>The tenant to use for app interactions.</p><p><br></p><p>Example: langstream configure tenant “a-tenant”</p></td></tr><tr><td><br></td><td>webServiceUrl</td><td>Control plane URL</td><td><p>The URL of the control plane service.</p><p><br></p><p>Example: langstream configure webServiceUrl http://localhost:8090</p></td></tr><tr><td><br></td><td>apiGatewayUrl</td><td>Gateway api URL</td><td><p>The URL of the API Gateway service.</p><p><br></p><p>Example: langstream configure apiGatewayUrl http://localhost:8091</p></td></tr><tr><td><br></td><td>token</td><td>Authentication token</td><td>Currently not used, held for future feature.</td></tr><tr><td>gateway</td><td><br></td><td>Interact with application gateway</td><td><br></td></tr><tr><td><br></td><td>chat</td><td>Produce and consume messages from gateway in a chat-like fashion</td><td><p>applicationId: the id of the application</p><p>-cg | --consume-from-gateway: id of gateway to consume messages from</p><p>-pg | --produce-to-gateway: id of gateway to produce messages to</p><p>-p | --param: Gateway parameters. Format: key=value</p><p>-c | --credentials: Credentials for the gateway. Required if the gateway requires authentication.</p></td></tr><tr><td><br></td><td>consume</td><td>Consume messages from a gateway</td><td><p>applicationId: the id of the application</p><p>gatewayId: the id of the consume gateway</p><p>-p | --param: Gateway parameters. Format: key=value</p><p>-c | --credentials: Credentials for the gateway. Required if the gateway requires authentication.</p><p>--position: Initial position of the consumer. "latest", "earliest" or a offset value. The offset value can be retrieved after consuming a message of the same topic.</p></td></tr><tr><td><br></td><td>produce</td><td>Produce messages to a gateway</td><td><p>applicationId: the id of the application</p><p>gatewayId: the id of the consume gateway</p><p>-p | --param: optional gateway parameters. Format: key=value</p><p>-c | --credentials: Credentials for the gateway. Required if the gateway requires authentication.</p><p>-v | --value: the message value to send</p><p>-k | --key: optional message key</p><p>--header: optional messages headers. Format: key=value</p></td></tr></tbody></table>

### Options

| –conf          | The path to a configuration file |
| -------------- | -------------------------------- |
| -v \| –verbose | Output a log of actions          |

### Config file (yaml)

```yaml
webServiceUrl: "<The fully qualified URL to the control plane service>"
tenant: "<The tenant to use for app interactions>"
apiGatewayUrl: "<The fully qualified URL to the gateway api service>"
token: "<unused>"
```

### Config env vars

<table data-header-hidden><thead><tr><th width="295">Var label</th><th>Description</th></tr></thead><tbody><tr><td>LANGSTREAM_webServiceUrl</td><td><p>The fully qualified URL to the control plane service</p><p><br></p><p>Example: https://controlplane.my-domain.com:XXX</p></td></tr><tr><td>LANGSTREAM_tenant</td><td>The tenant to use for app interactions</td></tr><tr><td>LANGSTREAM_apiGatewayUrl</td><td>The fully qualified URL to the gateway api service</td></tr><tr><td>LANGSTREAM_token</td><td>unused</td></tr></tbody></table>
