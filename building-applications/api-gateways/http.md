# HTTP

You connect to a gateway via standard HTTP 1.1. While connecting to a gateway, the path holds pointers to the type of gateway, the tenant, the application id, and the gateway name.

The URL structure is http://\<control-plane-domain>:\<api-gateway-port>/api/gateways/\<gateway-type>/\<tenant-name>/\<application-id>/\<gateway-id>.

Authentication (`credentials,test-credentials`), options (`option:`) and parameters (`param:`) are expected to be in the query string. HTTP headers are ignored by the API Gateway service.


## Produce messages

In order to produce messages via HTTP, you have to configure a `produce` gateway:
```yaml

gateways:
  - id: "user-input"
    type: produce
    topic: "questions-topic"
    parameters:
    - sessionId
```

Then you can use whathever HTTP client you prefer to connect. This is the example with Curl:

```bash

curl -X POST --body '{\"value\": \"hello\"}' "http://localhost:8091/api/gateways/produce/my-tenant/my-app/user-input?param:sessionId=12543yusi1"
```

You can also use the LangStream CLI:

```bash
langstream gateway produce my-app user-input --protocol http -v '{\"value\": \"hello\"}' -p sessionId=12543yusi1
```


## Produce messages and await for a message

In order to produce messages via HTTP and await for a message, you have to configure a `service` gateway:
```yaml

gateways:
  - id: "user-input-await"
    type: service
    parameters:
    - sessionId
    service-options:
        input-topic: inputs
        output-topic: results
```

Then you can use whathever HTTP client you prefer to connect. This is the example with Curl:

```bash
curl -X POST --body '{\"value\": \"hello\"}' "http://localhost:8091/api/gateways/service/my-tenant/my-app/user-input-await"
```

The timeout of the wait is the TCP timeout of the connection, usually 30 seconds (may vary depending on the http client).

## Proxy service agent requests

In order to proxy requests to a specific `service` agent via HTTP, you have to configure a `service` gateway:

```yaml
gateways:
  - id: "my-service"
    type: service
    parameters:
    - sessionId
    service-options:
        agent-id: my-service-agent
     
```

A service agent might look like this in the pipeline configuration: 
```yaml
pipeline:
  - name: "Start my service"
    id: my-service-agent
    type: "python-service"
    configuration:
      className: example.ChatBotService
```


Then you can use whathever HTTP client you prefer to connect. This is the example with Curl:

```bash
curl -X POST \
    --body '{\"value\": \"hello\"}' \
    --H 'Authorization: Bearer XXX' \
    "http://localhost:8091/api/gateways/service/my-tenant/my-app/my-service/the/custom/path?service-param-1=yes"
```

The final part of the URL, query string, HTTP method and headers will be sent to the service agent.

POST, GET, DELETE and PUT are all supported.

In the above case, the agent service will receive an equivalent request of:

```
curl -X POST \
    --body '{\"value\": \"hello\"}' \
    --H 'Authorization: Bearer XXX' \
    "http://localhost:8000/the/custom/path?service-param-1=yes"
```


Exceptionally, the `credentials`, `test-credentials`, `option:xx`, `param:xx` are stripped out from the routed requests.
Note that if the gateway has the authentication enabled, it will be performed as for other gateways.

Leveraging the API gateway to expose your service, automatically covers aspects like authentication, HTTPS, high-availability and scalability out of the box. 


The timeout of the wait is the TCP timeout of the connection, usually 30 seconds (may vary depending on the http client).
