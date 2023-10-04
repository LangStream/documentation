# API Gateways

Learn more about the LangStream project [here.](https://langstream.ai)

### Gateways

Each application can have many different gateways (also known as API Gateways). Each gateway is a means for interacting with an agent via a message topic.&#x20;

Produce gateways are simple clients that create a message and write it to a topic.&#x20;

Consume gateways are clients that watch a topic for new messages.&#x20;

Chat gateways create a producer client ("questions-topic") and a consumer client ("answers-topic") across one connection, optimized for "chat" style interactions between client and server.

If you send messages to the websocket of a consume gateway they will be ignored. Produce gateways will acknowledge receipt with an empty message.&#x20;

### Example manifest and URLs

Given an application in tenant “my-super-cool-tenant” with an id of “some-application” and the following gateway manifest, 2 consume APIs and 1 produce API will be created.

```yaml
gateways:
  - id: "user-input"
    type: produce
    topic: "questions-topic"

  - id: "bot-output"
    type: consume
    topic: "answers-topic"

  - id: "debug"
    type: consume
    topic: "log-topic"
    
  - id: "chat"
    type: chat
    chat-options:
      answers-topic: output-topic
      questions-topic: input-topic
```

The corresponding URLs to the gateways would be…

| <p>ws://localhost:8091/produce/my-super-cool-tenant/some-application/user-input<br>ws://localhost:8091/consume/my-super-cool-tenant/some-application/bot-output<br>ws://localhost:8091/consume/my-super-cool-tenant/some-application/debug<br>ws://localhost:8091/consume/my-super-cool-tenant/some-application/chat</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Websocket

You connect to a gateway via websocket. While connecting to a gateway, the path holds pointers to the type of gateway, the tenant, the application id, and the gateway name.

URL structure:

ws://\<control-plane-domain>:\<api-gateway-port>/\<gateway-type>/\<tenant-name>/\<application-id>/\<gateway-id>



| Name                 | Example                                                                                                                                     | Description                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api-gateway-port     | 8091                                                                                                                                        | This must not be on the same port as the control plane service. The port is not specific to an application.                                                    |
| application-id       | some-application                                                                                                                            | The id either assigned to the application or set in the module manifest.                                                                                       |
| control-plane-domain | <p>If running in local K8s with a port forward: localhost</p><p><br></p><p>If running in hosted K8s with a load balancer: cp.domain.com</p> | The ingress location of the control plane.                                                                                                                     |
| gateway-id           | produce-to-agent                                                                                                                            | A value that corresponds to its setting in the gateway manifest.                                                                                               |
| gateway-type         | produce                                                                                                                                     | <p>Supported values are:</p><ul><li>produce</li><li>consume</li><li>chat<br></li></ul><p>Corresponds to how a gateway was deployed. See manifest for more.</p> |
| tenant-name          | my-super-cool-tenant                                                                                                                        | The tenant name where the application is deployed.                                                                                                             |

{% hint style="warning" %}
When creating a “consume” URL you can optionally provide instructions for reading the next message to be added or reading from the first message saved in the topic. Add a querystring value to the URL with the label: “option:position” and a value of either “earliest” or “latest”.
{% endhint %}

Example of consuming the next message to arrive:

`ws://localhost:8091/consume/my-super-cool-tenant/some-application/bot-output?option:position=latest`

Example of consuming all messages currently on the topic:

`ws://localhost:8091/consume/my-super-cool-tenant/some-application/bot-output?option:position=earliest`

### Manifest

Example

<table><thead><tr><th width="132.33333333333331">Root</th><th width="157">Node</th><th width="117">Type</th><th>Description</th></tr></thead><tbody><tr><td>gateways<br></td><td></td><td></td><td>The base node in the yaml. Holds the collection of gateways.</td></tr><tr><td></td><td>id</td><td>string (required)</td><td>An authentic name for the given gateway. Allowed characters are a-zA-Z0-9._-</td></tr><tr><td></td><td>type</td><td>string (required)</td><td><p>The type of gateway to create. Supported values are:</p><ul><li>produce</li><li>consume</li><li>chat<br></li></ul><p>Set to produce to use the gateway to create messages in the topic. Set to consume to use the gateway to consume messages in the topic. Set to chat to create a producer topic (answers-topic) and a consumer topic (questions-topic) and connect them through the gateway.</p></td></tr><tr><td></td><td>topic</td><td>string (required)</td><td>The mapping of a topic declared in pipeline.yaml manifest. This is where a gateway produces and consumes messages. This value must match the name of a topic in the pipeline manifest.</td></tr><tr><td></td><td>parameters</td><td>string[]</td><td>A string collection of labels to look for in the querystring. See the below filtering example.</td></tr><tr><td><br></td><td>headers</td><td>object</td><td>The values to use as headers on produced messages, that hold the given parameters. </td></tr><tr><td></td><td>authentication</td><td>object</td><td>Configuration of an identity provider. See the below table.</td></tr></tbody></table>

#### headers

<table><thead><tr><th width="244">Label</th><th width="113.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td>key</td><td>string</td><td>An identifier of the value. This can be thought of as the name. Allowed characters are a-zA-Z0-9._-</td></tr><tr><td>valueFromParameters</td><td>string</td><td>The mapped name to connect a querystring value in the Gateway URL to message headers. This must match a value set in the parameters collection.</td></tr><tr><td>valueFromAuthentication</td><td>string</td><td>The mapped name to connect a provided querysting value with the identity provider’s handshake value.</td></tr></tbody></table>

#### authentication

<table><thead><tr><th width="171.33333333333331">Label</th><th width="133">Type</th><th>Description</th></tr></thead><tbody><tr><td>provider</td><td>string</td><td><p>The name of the identity provider. Supported values are:</p><ul><li>“google”</li><li>“github”</li></ul></td></tr><tr><td>configuration</td><td><br></td><td><p>For the google provider, follow the “<a href="https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid">Get your Google API client ID</a>” guide.</p><p>For the github provider, follow the “<a href="https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-login-with-github-button-with-a-github-app">Building a "Login with GitHub" button with a GitHub App</a>” guide.</p></td></tr><tr><td>clientId<br></td><td>string</td><td><p>The token to use for interacting with the given identity provider. Typically this is a pointer to a secret.</p><p><br></p><p>Example: “${ secrets.google.client-id }”</p></td></tr></tbody></table>

#### chat-options

| Label           | Type   | Description                                                                                                                                |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| answers-topic   | string | The name of the chat consumer topic, ex "input-topic".                                                                                     |
| questions-topic | string | The name of the chat producer topic, ex "output-topic".                                                                                    |
| headers         | object | The values to use as headers on produced messages, that hold the given parameters. See the headers table [above.](api-gateways.md#headers) |

### Gateway Message Filtering

Along with the above gateway configurations, you can also limit the messages a client produces or consumes.

Based on the above gateway manifest, you can selectively add filtering to the user-input gateway and the bot-output gateway:

```yaml
gateways:
  - id: "user-input"
    type: produce
    topic: "questions-topic"
    parameters:
      - sessionId
    produceOptions:
      headers:
        - key: langstream-client-session-id
          valueFromParameters: sessionId

  - id: "bot-output"
    type: consume
    topic: "answers-topic"
    parameters:
      - sessionId
    produceOptions:
      headers:
        - key: langstream-client-session-id
          valueFromParameters: sessionId

  - id: "debug"
    type: consume
    topic: "log-topic"
```

Then, to connect with the produce gateway, create an authentic id and use the URL:

```
export MY_UUID=$(uuidgen)

ws://localhost:8091/produce/my-super-cool-tenant/some-application/user-input?param:sessionId=${MY_UUID}
```

To consume, use the same uuid:&#x20;

```
ws://localhost:8091/consume/my-super-cool-tenant/some-application/bot-output?param:sessionId=${MY_UUID}
```

### Gateway Authentication

You can also require authentication when someone attempts a connection to either produce, consume, and chat gateways. To fully implement this, there is quite a bit left up to the developer. The focus of gateway authentication is to provide session id transportation and validation. An identity provider facilitates authentication through a series of handshakes based on a provided token. Someone wanting to produce or consume a message provides an id that was created by the identity provider. The gateway handshakes with the identity provider using the provided token. Using parameters, headers, and clientId to configure the gateway to successfully handshake.

[This authentication example](https://github.com/riptano/streaming-gen-ai/blob/main/examples/applications/gateway-authentication/README.md) application provides more explanation and a working example.

Based on this gateway manifest, you could selectively add authentication to the user-input and bot-output gateways:

```yaml
gateways:
  - id: "user-input"
    type: produce
    topic: "questions-topic"
    parameters:
      - sessionId
    authentication:
      provider: google
      configuration:
        clientId: "${ secrets.google.client-id }"
    produceOptions:
      headers:
        - key: langstream-client-user-id
        valueFromAuthentication: subject
        - key: langstream-client-session-id
          valueFromParameters: sessionId

  - id: "bot-output"
    type: consume
    topic: "answers-topic"
    parameters:
      - sessionId
    authentication:
      provider: google
      configuration:
        clientId: "${ secrets.google.client-id }"
    produceOptions:
      headers:
        - key: langstream-client-user-id
        valueFromAuthentication: subject
        - key: langstream-client-session-id
          valueFromParameters: sessionId

  - id: "debug"
    type: consume
    topic: "log-topic"
    
```
