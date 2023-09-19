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

{% hint style="info" %}
Want to get started a little quicker? Check out the [LangStream VSCode Extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) for pre-made applications and agent code snippets.
{% endhint %}

### Confirm the installation

Once installed you can test the CLI with the following command.

```
langstream -h
```

### Commands

<table data-full-width="false"><thead><tr><th width="125">Command</th><th width="120">Directive</th><th>Description</th><th>Arguments and example</th></tr></thead><tbody><tr><td>tenants</td><td><br></td><td>Manage tenants</td><td><br></td></tr><tr><td></td><td>create</td><td>Create a tenant</td><td>Example: langstream tenants create "a-tenant"<br><br>--max-total-resource-units: integer defining the maximum resources the tenant can use. Can be null.</td></tr><tr><td><br></td><td>delete</td><td>Remove a tenant</td><td>Example: langstream tenants delete “a-tenant”</td></tr><tr><td><br></td><td>get</td><td>Get tenant configuration</td><td>Example: langstream tenants get “a-tenant”</td></tr><tr><td><br></td><td>list</td><td>List all tenants</td><td>Example: langstream tenants list</td></tr><tr><td><br></td><td>put</td><td>Save a tenant</td><td>Example: langstream tenants put “a-tenant”</td></tr><tr><td></td><td>update</td><td>Update an existing tenant</td><td><p>Example: langstream tenants update "a-tenant"</p><p></p><p>--max-total-resource-units: integer defining the maximum resources the tenant can use. Can be null.</p></td></tr><tr><td>apps</td><td><br></td><td>Manage applications</td><td><br></td></tr><tr><td><br></td><td>list</td><td>List all applications</td><td>Example: langstream apps list</td></tr><tr><td><br></td><td>get</td><td>Get application status</td><td><p>applicationId: the id of the application</p><p>-o: optional output format, supported values are “json”, “yaml”, “raw”. Default is “raw”.</p><p><br></p><p>Example: langstream apps get “some-app-id”</p></td></tr><tr><td><br></td><td>delete</td><td>Remove an application</td><td><p>Name : application name</p><p><br></p><p>Example: langstream apps delete “some-app-id”</p></td></tr><tr><td><br></td><td>deploy</td><td>Deploy a new application</td><td><p>applicationId: the id of the application</p><p>–app | –-application: application directory path REQUIRED<br>-i | --instance: instance file path REQUIRED</p><p>-s | --secrets: secrets file path OPTIONAL</p><p><br></p><p>Learn more about the contents of the application directory <a href="../building-applications/development-environment.md">here.</a></p><p><br></p><p>Example: langstream apps deploy my-app-id \</p><p>--app “./my-app-files” \</p><p>--i “./instances.yaml”\</p><p>--s “./secrets.yaml”<br><br>You can also deploy an application from a GitHub URL.<br><br>Example: langstream apps deploy test -app https://github.com/LangStream/langstream/tree/main/examples/applications/astradb-sink</p></td></tr><tr><td></td><td>download</td><td>Download LangStream application code</td><td><p>applicationId: the id of the application</p><p>-o | --output-file:</p><p>output file path for downloaded code</p><p></p><p>Example with output file:</p><p><br>langstream apps download myapp -o /myfile.zip</p></td></tr><tr><td><br></td><td>update</td><td>Update an existing application</td><td><p>applicationId: the id of the application</p><p>–app | –-application: application directory path REQUIRED<br>-i | --instance: instance file path REQUIRED</p><p>-s | --secrets: secrets file path OPTIONAL</p><p><br></p><p>Learn more about the contents of the application directory <a href="../building-applications/development-environment.md">here.</a></p><p><br></p><p>Example: langstream apps update my-app-id \</p><p>-app “./my-app-files” \</p><p>-i “./instances.yaml”\</p><p>-s “./secrets.yaml”</p></td></tr><tr><td><br></td><td>logs</td><td>Get application logs</td><td><p>applicationId: the id of the application</p><p>-f : filter by worker id, comma delimited list</p><p><br></p><p>Example: langstream apps logs my-app-id -f “some-app-worker, another-app-worker”</p></td></tr><tr><td>configure</td><td><br></td><td>Configure tenant and authentication</td><td><br></td></tr><tr><td><br></td><td>tenant</td><td>Tenant name</td><td><p>The tenant to use for app interactions.</p><p><br></p><p>Example: langstream configure tenant “a-tenant”</p></td></tr><tr><td><br></td><td>webServiceUrl</td><td>Control plane URL</td><td><p>The URL of the control plane service.</p><p><br></p><p>Example: langstream configure webServiceUrl http://localhost:8090</p></td></tr><tr><td><br></td><td>apiGatewayUrl</td><td>Gateway api URL</td><td><p>The URL of the API Gateway service.</p><p><br></p><p>Example: langstream configure apiGatewayUrl http://localhost:8091</p></td></tr><tr><td><br></td><td>token</td><td>Authentication token</td><td>Currently not used, held for future feature.</td></tr><tr><td>gateway</td><td><br></td><td>Interact with application gateway</td><td><br></td></tr><tr><td><br></td><td>chat</td><td>Produce and consume messages from gateway in a chat-like fashion</td><td><p>applicationId: the id of the application</p><p>-cg | --consume-from-gateway: id of gateway to consume messages from</p><p>-pg | --produce-to-gateway: id of gateway to produce messages to</p><p>-p | --param: Gateway parameters. Format: key=value</p><p>-c | --credentials: Credentials for the gateway. Required if the gateway requires authentication<br>--connect-timeout: Connect timeout for WebSocket connections in seconds.</p></td></tr><tr><td><br></td><td>consume</td><td>Consume messages from a gateway</td><td><p>applicationId: the id of the application</p><p>gatewayId: the id of the consume gateway</p><p>-p | --param: Gateway parameters. Format: key=value</p><p>-c | --credentials: Credentials for the gateway. Required if the gateway requires authentication.</p><p>--position: Initial position of the consumer. "latest", "earliest" or a offset value. The offset value can be retrieved after consuming a message of the same topic.<br>--connect-timeout: Connect timeout for WebSocket connections in seconds.</p></td></tr><tr><td><br></td><td>produce</td><td>Produce messages to a gateway</td><td><p>applicationId: the id of the application</p><p>gatewayId: the id of the consume gateway</p><p>-p | --param: optional gateway parameters. Format: key=value</p><p>-c | --credentials: Credentials for the gateway. Required if the gateway requires authentication.</p><p>-v | --value: the message value to send</p><p>-k | --key: optional message key</p><p>--header: optional messages headers. Format: key=value<br>--connect-timeout: Connect timeout for WebSocket connections in seconds.</p></td></tr><tr><td>profiles</td><td></td><td>Manage CLI profiles</td><td></td></tr><tr><td></td><td>create</td><td>Create a new profile</td><td><p>example: langstream profiles create my-profile<br><br>--set-current: Set this profile as current </p><p>--web-service-url: webServiceUrl of the profile (REQUIRED)</p><p>--api-gateway-url: apiGatewayUrl of the profile </p><p>--tenant: tenant of the profile </p><p>--token: token of the profile</p></td></tr><tr><td></td><td>update</td><td>Update an existing profile</td><td><p>example: langstream profiles update my-profile<br><br>--set-current: Set this profile as current </p><p>--web-service-url: webServiceUrl of the profile </p><p>--api-gateway-url: apiGatewayUrl of the profile </p><p>--tenant: tenant of the profile </p><p>--token: token of the profile</p></td></tr><tr><td></td><td>delete</td><td>Delete an existing profile</td><td>example: langstream profiles delete my-profile</td></tr><tr><td></td><td>get-current</td><td>Get current profile</td><td>example: langstream profiles get-current</td></tr><tr><td></td><td>get</td><td>Get a profile configuration</td><td>example: langstream profiles get my-profile<br><br>-o | --output-format<br><br>example: langstream profiles get my-profile -o=json</td></tr><tr><td></td><td>import</td><td>Import profile from file or inline json</td><td><p>example: langstream profiles import my-profile -f file.json</p><p>-f | --file: Import profile from file </p><p>-i | --inline: Import profile from inline json </p><p>-u | --update: Allow updating the profile if it already exists </p><p>--set-current: Set this profile as current</p></td></tr><tr><td></td><td>list</td><td>List profiles</td><td><p>langstream profiles list<br><br>-o | --output-format</p><p>example: langstream profiles list my-profile -o=json</p></td></tr><tr><td></td><td>set-current</td><td>Set a profile as the current profile</td><td>langstream profiles set-current my-profile</td></tr><tr><td>docker</td><td><br></td><td>Manage LangStream runtime</td><td><br></td></tr>

<tr><td><br></td><td>--application, -app</td><td>Application directory path</td><td>Example: langstream runtime --application ./app-files<br>Path where the application files are located. Required.</td></tr>

<tr><td><br></td><td>--instance, -i</td><td>Instance file path</td><td>Example: langstream runtime --instance ./instance.yaml<br>Optional; path to the instance file.</td></tr>

<tr><td><br></td><td>--start-broker</td><td>Start the broker</td><td>Example: langstream runtime --start-broker<br>Should the broker be started? Default: true.</td></tr>

<tr><td><br></td><td>--start-s3</td><td>Start the S3 service</td><td>Example: langstream runtime --start-s3<br>Should the S3 service be started? Default: true.</td></tr>

<tr><td><br></td><td>--start-webservices</td><td>Start LangStream web services</td><td>Example: langstream runtime --start-webservices<br>Should LangStream web services be started? Default: true.</td></tr>

<tr><td><br></td><td>--only-agent</td><td>Run only one agent</td><td>Example: langstream runtime --only-agent "AgentID"<br>ID of a single agent to run (optional).</td></tr>

<tr><td><br></td><td>--secrets, -s</td><td>Secrets file path</td><td>Example: langstream runtime --secrets "./secrets.yaml"<br>Optional; path to the secrets file.</td></tr>

<tr><td><br></td><td>--memory</td><td>Memory for Docker</td><td>Example: langstream runtime --memory "4G"<br>Memory allocated to the Docker container.</td></tr>

<tr><td><br></td><td>--cpus</td><td>CPU for Docker</td><td>Example: langstream runtime --cpus "2"<br>CPU cores allocated to the Docker container.</td></tr>

<tr><td><br></td><td>--docker-args</td><td>Additional Docker arguments</td><td>Example: langstream runtime --docker-args "--add-host=example.com:192.168.1.10"<br>Additional arguments to pass to Docker.</td></tr>

<tr><td><br></td><td>--docker-command</td><td>Command to run Docker</td><td>Example: langstream runtime --docker-command "docker-compose"<br>Command used to run Docker. Default: "docker".</td></tr>

<tr><td><br></td><td>--langstream-runtime-version</td><td>LangStream runtime version</td><td>Example: langstream runtime --langstream-runtime-version "1.0.0"<br>Version of LangStream runtime to use. Default: Maven Version.</td></tr>

<tr><td><br></td><td>--langstream-runtime-docker-image</td><td>LangStream Docker image</td><td>Example: langstream runtime --langstream-runtime-docker-image "langstream/runtime:latest"<br>Docker image to use for LangStream runtime.</td></tr>
</tbody></table>

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
