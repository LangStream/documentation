# HTTP

You connect to a gateway via standard HTTP 1.1. While connecting to a gateway, the path holds pointers to the type of gateway, the tenant, the application id, and the gateway name.

The URL structure is http://\<control-plane-domain>:\<api-gateway-port>/api/gateways/\<gateway-type>/\<tenant-name>/\<application-id>/\<gateway-id>.

Authentication (`credentials,test-credentials`), options (`option:`) and parameters (`param:`) are expected to be in the query string. HTTP headers are ignored by the API Gateway service.


## Produce messages

To produce messages via HTTP, configure a `produce` gateway:
```yaml

gateways:
  - id: "user-input"
    type: produce
    topic: "questions-topic"
    parameters:
    - sessionId
```

Once a gateway is configured, you can use whatever HTTP client you prefer to connect. This is an example with Curl:

```bash
curl -X POST -d "Hello" "http://localhost:8091/api/gateways/produce/my-tenant/my-app/user-input?param:sessionId=12543yusi1"
```

or if you would like to add the record key, headers or a structured value you can pass the body as JSON setting `Content-Type: application/json`

```bash
curl -X POST -d '{"value": {"question": "hello"}, "key": "k1", headers: {"h1": "v1"}}' -H 'Content-Type: application/json' "http://localhost:8091/api/gateways/produce/my-tenant/my-app/user-input?param:sessionId=12543yusi1"
```


You can also use the LangStream CLI:

```bash
langstream gateway produce my-app user-input --protocol http -v '{"value": "hello"}' -p sessionId=12543yusi1
```


## Produce messages and wait for a message

To produce messages via HTTP and wait for a message, configure a `service` gateway:
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

Once a gateway is configured, you can use whatever HTTP client you prefer to connect. This is an example with Curl:

```bash
curl -X POST -d '{"value": "hello"}' -H 'Content-Type: application/json' "http://localhost:8091/api/gateways/service/my-tenant/my-app/user-input-await"
```

The timeout of the wait is the TCP timeout of the connection, which is usually 30 seconds (may vary depending on the http client).

## Proxy service agent requests

To proxy requests to a specific `service` agent via HTTP, configure a `service` gateway:

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


Once a gateway is configured, you can use whatever HTTP client you prefer to connect. This is an example with Curl:

```bash
curl -X POST \
    -d '{"value": "hello"}' \
    -H 'Authorization: Bearer XXX' \
    -H 'Content-Type: application/json' \
    "http://localhost:8091/api/gateways/service/my-tenant/my-app/my-service/the/custom/path?service-param-1=yes"
```

The final part of the URL, query string, HTTP method, and headers will be sent to the service agent.


In the above case, the agent service will receive an equivalent request of:

```
curl -X POST \
    -d '{"value": "hello"}' \
    -H 'Authorization: Bearer XXX' \
    -H 'Content-Type: application/json' \
    "http://localhost:8000/the/custom/path?service-param-1=yes"
```


The `credentials`, `test-credentials`, `option:xx`, `param:xx` are stripped out from the routed requests.
If the gateway has authentication enabled, it will be performed as for other gateways.

POST, GET, DELETE and PUT are all supported.

Leveraging the API gateway to expose your service solves authentication, HTTPS, high-availability, and scalability out of the box. 
