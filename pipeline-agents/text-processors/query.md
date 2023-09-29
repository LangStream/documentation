# query

Given a datasource specified in the application configuration, this agent enables submitting queries to that source and outputting the results.

This is very similar to the [query-vector-db](query-vector-db.md) agent, but it is not limited to vector databases.

### Example

Install PostgreSQL in a local minikube cluster:

```
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

### **Configuration**

<table><thead><tr><th width="155.33333333333331">Label</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td>datasource</td><td>string</td><td>A reference to the datasource name declared in resources.datasources of the configuration.yaml manifest.</td></tr><tr><td>query</td><td>string</td><td><p>The query statement to run. Each placeholder “?” will be replaced with fields value in order.<br></p><p>Example:</p><p>SELECT * FROM products WHERE id = ?</p></td></tr><tr><td>fields</td><td>string[]</td><td><p>A collection of field values. Each value will be used in order to replace placeholders in the query (do not include mustache brackets, this not a templated value).<br></p><p>Example collection:</p><ul><li>“value.id”</li></ul><p>If value.id == 123 then the query would be</p><p>SELECT * FROM products WHERE id = 123</p></td></tr><tr><td>output-field</td><td>string</td><td><p>The name of an additional field to be added to message data containing query result (do not include mustache brackets, this is not a templated value).</p><p></p><p>Provide in the form: “value.&#x3C;field-name>”</p></td></tr></tbody></table>

\
