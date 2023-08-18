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
    langstream tenants put "super-cool-tenant"
    ```
2. The tenant name and control plane address are shared with the application developer
3.  The developer configures their local environment to interact with the control plane

    <pre><code><strong>langstream configure tenant "super-cool-tenant"
    </strong>langstream configure webServiceUrl "&#x3C;control-plane-address>"
    </code></pre>
4.  When ready, the developer deploys their application to the tenant

    ```
    langstream apps deploy super-cool-app -app ./application -i ./instance.yaml # -s ./secrets.yaml
    ```
5.  Watch the progress of the deployment by watching the logs

    ```
    langstream apps logs "super-cool-app"
    ```
