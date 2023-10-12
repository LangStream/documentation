# query

Given a datasource specified in the application configuration, this agent enables submitting queries to that source and outputting the results.

This is very similar to the [query-vector-db](query-vector-db.md) agent, but it is not limited to vector databases.

### Example

Install PostgreSQL in a local minikube cluster:

```bash
minikube start
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-postgresql bitnami/postgresql --version 12.8.2
```

Specify a datasource in configuration.yaml:

```yaml
configuration:
  resources:
    - type: "datasource"
      name: "PGDataSource"
      configuration:
        service: "jdbc"
        driverClass: "org.postgresql.Driver"
        url: "jdbc:postgresql://postgresql.default.svc.cluster.local:5432/"
        user: "postgres"
        password: "xxxxxxxx"
```

Reference that datasource and submit a query using input message values:

```yaml
- name: "Execute Query"
  type: "query"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    datasource: "PGDataSource"
    query: "SELECT * FROM products WHERE id = ?"
    fields:
      - "value.id"
    output-field: "value.query-result"
```

### **Topics**

#### **Input**

* Structured and unstructured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### **Output**

* Structured text [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#query).