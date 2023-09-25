# LangStream CLI Conmmands

Use the CLI to manage your control plane, deploy applications, and interact with an application's gateway.

To install the CLI, see [Installation](../installation/langstream-cli.md).
To configure the CLI, see [Configuration](./langstream-cli-configuration.md)

* [apps](/langstream-cli/langstream-cli-commands.md#apps)
* [configure](/langstream-cli/langstream-cli-commands.md#configure) [DEPRECATED]
* [docker run](/langstream-cli/langstream-cli-commands.md#docker-run)
* [gateways](/langstream-cli/langstream-cli-commands.md#gateway)
* [profiles](/langstream-cli/langstream-cli-commands.md#profiles)
* [tenants](/langstream-cli/langstream-cli-commands.md#tenants)

## apps
| Directive  | Description                       | Arguments and Example                                                                                                                                                |
|------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| list       | List all applications             | Example: langstream apps list                                                                                                                                        |
| get        | Get application status            | Example: langstream apps get "some-app-id" -o: optional output format, supported values are “json”, “yaml”, “raw”. Default is “raw”.                                  |
| delete     | Remove an application              | Example: langstream apps delete “some-app-id”                                                                                                                         |
| deploy     | Deploy a new application          | Example: langstream apps deploy my-app-id --app “./my-app-files” --i “./instances.yaml” --s “./secrets.yaml”                                                         |
| download   | Download LangStream application code | Example: langstream apps download myapp -o /myfile.zip                                                                                                               |
| update     | Update an existing application    | Example: langstream apps update my-app-id --app “./my-app-files” --i “./instances.yaml” --s “./secrets.yaml”                                                         |
| logs       | Get application logs              | Example: langstream apps logs my-app-id -f “some-app-worker, another-app-worker”                                                                                     |

## configure

[NOTE]
Configuration is deprecated. Use [langstream profiles](/langstream-cli/langstream-cli-commands.md#profiles) instead.


| Directive       | Description            | Arguments and Example                                                                                         |
|-----------------|------------------------|---------------------------------------------------------------------------------------------------------------|
| tenant          | Tenant name            | Example: langstream configure tenant “a-tenant”                                                               |
| webServiceUrl   | Control plane URL      | Example: langstream configure webServiceUrl http://localhost:8090                                             |
| apiGatewayUrl   | Gateway api URL        | Example: langstream configure apiGatewayUrl http://localhost:8091                                             |
| token           | Authentication token   | Currently not used, held for future feature.                                                                  |

## docker run

| Directive                      | Description                     | Arguments and Example                                                                                                                                |
|--------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| --application, -app            | Application directory path      | Example: --application="./app-files" Path where the application files are located. Required.                                                          |
| --instance, -i                 | Instance file path              | Example: --instance="./instance.yaml" Optional; path to the instance file.                                                                            |
| --start-broker                 | Start the broker                | Example: --start-broker="true" Should the broker be started? Default: true.                                                                           |
| --start-s3                     | Start the S3 service            | Example: --start-s3="true" Should the S3 service be started? Default: true.                                                                           |
| --start-webservices            | Start LangStream web services   | Example: --start-webservices="true" Should LangStream web services be started? Default: true.                                                         |
| --only-agent                   | Run only one agent              | Example: --only-agent="AgentID" ID of a single agent to run (optional).                                                                               |
| --secrets, -s                  | Secrets file path               | Example: --secrets="./secrets.yaml" Optional; path to the secrets file.                                                                               |
| --memory                       | Memory for Docker               | Example: --memory="4G" Memory allocated to the Docker container.                                                                                      |
| --cpus                         | CPU for Docker                  | Example: --cpus="2" CPU cores allocated to the Docker container.                                                                                      |
| --docker-args                  | Additional Docker arguments     | Example: --docker-args "--add-host=example.com:192.168.1.10" Additional arguments to pass to Docker.                                                   |
| --docker-command               | Command to run Docker           | Example: --docker-command="docker-compose" Command used to run

## gateway

| Directive | Description                                         | Arguments and Example                                                                                                                                                            |
|-----------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| chat      | Produce and consume messages from gateway in a chat-like fashion | Example: langstream gateway chat my-app-id -cg “some-gateway-id” -pg “another-gateway-id” -p “key=value” -c “some-credentials” --connect-timeout: Connect timeout in seconds.       |
| consume   | Consume messages from a gateway                     | Example: langstream gateway consume my-app-id “some-gateway-id” -p “key=value” -c “some-credentials” --position “latest” --connect-timeout: Connect timeout in seconds.           |
| produce   | Produce messages to a gateway                      | Example: langstream gateway produce my-app-id “some-gateway-id” -p “key=value” -c “some-credentials” -v “some-message” -k “some-key” --header “key=value” --connect-timeout: Connect timeout in seconds.|

## profiles

| Directive   | Description                   | Arguments and Example                                                                                                                                                 |
|-------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| create      | Create a new profile         | Example: langstream profiles create my-profile --set-current --web-service-url: webServiceUrl of the profile (REQUIRED) --api-gateway-url: apiGatewayUrl of the profile --tenant: tenant of the profile --token: token of the profile |
| update      | Update an existing profile   | Example: langstream profiles update my-profile --set-current --web-service-url: webServiceUrl of the profile --api-gateway-url: apiGatewayUrl of the profile --tenant: tenant of the profile --token: token of the profile |
| delete      | Delete an existing profile   | Example: langstream profiles delete my-profile                                                                                                                        |
| get-current | Get current profile          | Example: langstream profiles get-current                                                                                                                               |
| get         | Get a profile configuration  | Example: langstream profiles get my-profile -o=json                                                                                                                    |
| import      | Import profile from file or inline json | Example: langstream profiles import my-profile -f file.json -i -u --set-current                                                                                        |
| list        | List profiles                | Example: langstream profiles list -o=json                                                                                                                              |
| set-current | Set a profile as the current profile | Example: langstream profiles set-current my-profile                                                                                                                    |

## tenants
| Directive  | Description                    | Arguments and Example                                                                                                                                                  |
|------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| create     | Create a tenant                | Example: langstream tenants create "a-tenant" --max-total-resource-units: integer defining the maximum resources the tenant can use. Can be null.                      |
| delete     | Remove a tenant                | Example: langstream tenants delete "a-tenant"                                                                                                                           |
| get        | Get tenant configuration      | Example: langstream tenants get "a-tenant"                                                                                                                              |
| list       | List all tenants               | Example: langstream tenants list                                                                                                                                        |
| put        | Save a tenant                  | Example: langstream tenants put "a-tenant"                                                                                                                              |
| update     | Update an existing tenant      | Example: langstream tenants update "a-tenant" --max-total-resource-units: integer defining the maximum resources the tenant can use. Can be null.                      |
