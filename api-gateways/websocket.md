# Websocket

You connect to a gateway via websocket. While connecting to a gateway, the path holds pointers to the type of gateway, the tenant, the application id, and the gateway name.

The URL structure is ws://\<control-plane-domain>:\<api-gateway-port>/\<gateway-type>/\<tenant-name>/\<application-id>/\<gateway-id>

These values are in the table below.

### Websocket configuration

| Name                 | Example                                                                                                                                     | Description                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api-gateway-port     | 8091                                                                                                                                        | This must not be on the same port as the control plane service. The port is not specific to an application.                                                    |
| application-id       | some-application                                                                                                                            | The id either assigned to the application or set in the module manifest.                                                                                       |
| control-plane-domain | <p>If running in local K8s with a port forward: localhost</p><p><br></p><p>If running in hosted K8s with a load balancer: cp.domain.com</p> | The ingress location of the control plane.                                                                                                                     |
| gateway-id           | produce-to-agent                                                                                                                            | A value that corresponds to its setting in the gateway manifest.                                                                                               |
| gateway-type         | produce                                                                                                                                     | <p>Supported values are:</p><ul><li>produce</li><li>consume</li><li>chat<br></li></ul><p>Corresponds to how a gateway was deployed. See manifest for more.</p> |
| tenant-name          | my-super-cool-tenant                                                                                                                        | The tenant name where the application is deployed.                                                                                                             |

