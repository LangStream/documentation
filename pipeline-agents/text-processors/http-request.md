# http-request

This is an agent that make http requests to a specified endpoint.

### Example

An example that calls a mock GeoCoding API service and store the result in the `response` field.

```yaml
  - name: "Get timezone info from geocoding API"
    type: "http-request"
    configuration:
      url: "https://geocoding-api-service/v1/search"
      query-string:
        name: "{{{ value.city }}}"
        count: "1"
        format: "json"
      output-field: "value.response"
      method: "GET"
```


### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#http-request).