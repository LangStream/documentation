# API Gateways

API gateways in LangStream are HTTP/WebSocket endpoints that allow applications to interact with agents via message topics.

Messages contain a key, a value, and headers for metadata. This metadata is used to connect clients to topics and can be used to [filter messages.](message-filtering.md)

LangStream applications can have three different gateway types:

**Producer** gateways are clients that create a message and write it to a topic.&#x20;

**Consumer** gateways are clients that watch a topic for messages from a given position. This gateway can only be accessed via WebSocket. &#x20;

**Chat** gateways create a producer client (`questions-topic`) and a consumer client (`answers-topic`) across one connection, optimized for "chat" style interactions between client and server. This gateway can only be accessed via WebSocket.&#x20;

**Service (topics)** gateways create a producer client (`input-topic`) and a consumer client (`output-topic`), writing a single message and awaiting for the receivement of another message. This gateway can only be accessed via HTTP.&#x20;

**Service (agents)** gateways send requests directly to a `service` agent and return the response to the client. This gateway can only be accessed via HTTP.

### Example gateways

Given an application in tenant “my-super-cool-tenant” with an id of “some-application” and the following gateway manifest, 1 gateway of each type is created:

```yaml
gateways:
  - id: "user-input"
    type: produce
    topic: "questions-topic"

  - id: "bot-output"
    type: consume
    topic: "answers-topic"
    
  - id: "chat"
    type: chat
    chat-options:
      questions-topic: questions-topic
      answers-topic: answers-topic

  - id: "service"
    type: service
    service-options:
      input-topic: questions-topic
      output-topic: answers-topic
```

The corresponding URLs to the gateways would be:

**Produce gateway:** ws://localhost:8091/produce/my-super-cool-tenant/some-application/user-input&#x20;

**Consume gateway:** ws://localhost:8091/consume/my-super-cool-tenant/some-application/bot-output

**Chat gateway:** ws://localhost:8091/consume/my-super-cool-tenant/some-application/chat

**Service gateway:** http://localhost:8091/api/gateways/service/my-super-cool-tenant/some-application/service

The URL structure is ws://\<control-plane-domain>:\<api-gateway-port>/\<gateway-type>/\<tenant-name>/\<application-id>/\<gateway-id> for WebSocket.

The URL structure is http://\<control-plane-domain>:\<api-gateway-port>/api/gateways/\<gateway-type>/\<tenant-name>/\<application-id>/\<gateway-id> for HTTP.


### Gateways configuration

<table><thead><tr><th width="132.33333333333331">Root</th><th width="157">Node</th><th width="117">Type</th><th>Description</th></tr></thead><tbody><tr><td>gateways<br></td><td></td><td></td><td>The base node in the yaml. Holds the collection of gateways.</td></tr><tr><td></td><td>id</td><td>string (required)</td><td>An authentic name for the given gateway. Allowed characters are a-zA-Z0-9._-</td></tr><tr><td></td><td>type</td><td>string (required)</td><td><p>The type of gateway to create. Supported values are:</p><ul><li>produce</li><li>consume</li><li>chat</li></ul><p>Set to "produce" to use the gateway to create messages in the topic. Set to "consume" to use the gateway to consume messages in the topic. Set to "chat" to create a producer topic (answers-topic) and a consumer topic (questions-topic) and connect them through the gateway.</p></td></tr><tr><td></td><td>topic</td><td>string (required)</td><td>The mapping of a topic declared in pipeline.yaml manifest. This is where a gateway produces and consumes messages. This value must match the name of a topic in the pipeline manifest.</td></tr><tr><td></td><td>parameters</td><td>string[]</td><td>A string collection of labels to look for in the querystring. See <a href="message-filtering.md">Message filtering.</a></td></tr><tr><td><br></td><td>headers</td><td>object</td><td>The values to use as headers on produced messages, that hold the given parameters. </td></tr><tr><td></td><td>authentication</td><td>object</td><td>Configuration of an identity provider. See <a href="gateway-authentication.md">Gateway authentication.</a></td></tr><tr><td></td><td>produce-options</td><td>object</td><td>See <a href="./#headers">headers.</a></td></tr><tr><td></td><td>consume-options</td><td>object</td><td>See <a href="./#headers">headers.</a></td></tr><tr><td></td><td>chat-options</td><td>object</td><td>See <a href="./#chat-options">chat-options.</a></td></tr><tr><td></td><td>headers</td><td>map&#x3C;String, String></td><td>See <a href="./#headers">headers.</a></td></tr></tbody></table>

#### chat-options

| Label           | Type   | Description                                                                                                   |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| answers-topic   | string | The name of the chat consumer topic, ex "input-topic".                                                        |
| questions-topic | string | The name of the chat producer topic, ex "output-topic".                                                       |
| headers         | object | The values to use as headers on produced messages, that hold the given parameters. See [headers.](./#headers) |

#### headers

<table><thead><tr><th width="244">Label</th><th width="113.33333333333331">Type</th><th>Description</th></tr></thead><tbody><tr><td>key</td><td>string</td><td>An identifier of the value. This can be thought of as the name. Allowed characters are a-zA-Z0-9._-</td></tr><tr><td>value-from-parameters</td><td>string</td><td>The mapped name to connect a querystring value in the Gateway URL to message headers. This must match a value set in the parameters collection.</td></tr><tr><td>value-from-authentication</td><td>string</td><td>The mapped name to connect a provided querysting value with the identity provider’s handshake value. See <a href="gateway-authentication.md">Gateway authentication.</a></td></tr></tbody></table>

### Example gateways manifest

{% @github-files/github-code-block url="https://github.com/LangStream/langstream/blob/main/examples/applications/gateway-authentication/gateways.yaml" %}
