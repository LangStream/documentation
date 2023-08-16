---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Development Workflow

### Development workflow

Using the [LangStream CLI](../installation/langstream-cli.md), a typical workflow is:

1.  The control plane operator creates a tenant for a new application:

    ```
    sgai-cli tenants put "super-cool-app"
    ```
2. The tenant name and control plane address are shared with the application developer
3.  The developer configures their local environment to interact with the control plane

    <pre><code><strong>sgai-cli configure tenant "super-cool-app"
    </strong>sgai-cli configure webServiceUrl "&#x3C;control-plane-address>"
    </code></pre>
4.  When ready, the developer deploys their application to the tenant

    ```
    sgai-cli apps deploy -app ./application -i ./instance.yaml # -s ./secrets.yaml
    ```
5.  Watch the progress of the deployment by watching the logs

    ```
    sgai-cli apps logs "super-cool-app"
    ```

Or if you have access to the K8s namespace of the new application, watch the pod logs:

```
kubectl -n "<helm-namespaceprefix>-super-cool-app" logs -f "sgai-super-cool-app"
```

