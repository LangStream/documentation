# Gateway authentication

You can require authentication when someone attempts a connection to produce, consume, and chat gateways.&#x20;

To fully implement this, there is quite a bit left up to the developer. The focus of gateway authentication is to provide transportation and validation. An identity provider facilitates authentication through a series of handshakes based on a provided token. Someone wanting to produce or consume a message provides an id that was created by the identity provider. The gateway handshakes with the identity provider using the provided token. Use parameters, headers, and clientId to configure the gateway to successfully handshake.

[This authentication example](https://github.com/riptano/streaming-gen-ai/blob/main/examples/applications/gateway-authentication/README.md) application provides more explanation and a working example.

### Example gateways.yaml

This gateway manifest is selectively adding authentication to the user-input and bot-output gateways.

The gateways are filtering messages by two key-value pairs in the message headers: the sessionID parameter value, and the "subject" value from the langstream-client-user-id key.`sessionId` is a UUID generated by the CLI at runtime. Here, let's assume sessionId=123.

`value-from-parameters` defines what value is being used for filtering. Since it's sessionId, the sessionId value is 123.

{% hint style="info" %}
Once a parameter is defined for a gateway, that parameter is required for every subsequent connection.&#x20;
{% endhint %}

The producer will produce to the `questions-topic` with two header values:

1. `langstream-client-session-id,`with the arbitrary value "123" from the gateway parameters&#x20;
2. `langstream-client-user-id` with the "subject" value from Google authentication

The consumer will watch for messages with these values in the headers on the `questions-topic`.

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
        clientId: "{{ secrets.google.client-id }}"
    produceOptions:
      headers:
        - key: langstream-client-user-id
        valueFromAuthentication: subject
        - key: langstream-client-session-id
          valueFromParameters: sessionId

  - id: "bot-output"
    type: consume
    topic: "questions-topic"
    parameters:
      - sessionId
    authentication:
      provider: google
      configuration:
        clientId: "{{ secrets.google.client-id }}"
    produceOptions:
      headers:
        - key: langstream-client-user-id
        valueFromAuthentication: subject
        - key: langstream-client-session-id
          valueFromParameters: sessionId
```

#### Google authentication

Set `provider:google` to use a Google client ID to authenticate LangStream gateway connections.

The Google field that is exposed for authentication is "subject".

Follow the “[Get your Google API client ID](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid)” guide to create your client ID.

The Google client ID looks like this:&#x20;

```
99840107278-4363876v0hker43roujaubqom5g07or8.apps.googleusercontent.com
```

To set it as a secret env variable:

```
export GOOGLE_CLIENT_ID=99840107278-4363876v0hker43roujaubqom5g07or8.apps.googleusercontent.com
```

#### Github authentication

Set `provider:github` to use a GitHub login to authenticate LangStream gateway connections.

The Github field that is exposed for authentication is "login".

Follow the “[Building a "Login with GitHub" button with a GitHub App](https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-login-with-github-button-with-a-github-app)” guide to create your login.

### Configuration

<table><thead><tr><th width="171.33333333333331">Label</th><th width="133">Type</th><th>Description</th></tr></thead><tbody><tr><td>provider</td><td>string</td><td><p>The name of the identity provider. Supported values are:</p><ul><li>“google”</li><li>“github”</li></ul></td></tr><tr><td>configuration</td><td><br>Map</td><td><p>For the google provider, follow the “<a href="https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid">Get your Google API client ID</a>” guide.</p><p>For the github provider, follow the “<a href="https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-login-with-github-button-with-a-github-app">Building a "Login with GitHub" button with a GitHub App</a>” guide.</p></td></tr><tr><td>clientId<br></td><td>string</td><td><p>The token to use for interacting with the given identity provider. Typically this is a pointer to a secret.</p><p></p><p>Example: clientId: "${secrets.google.client-id}"</p></td></tr></tbody></table>