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

# Configuration

A manifest of additional resources and dependencies to run the pipeline.

Example of a data source that needs drivers as well as credentials:

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
        password: "xxxxxx"
  dependencies:
    - name: "PostGRES JDBC Driver"
      url: "https://jdbc.postgresql.org/download/postgresql-42.6.0.jar"
      sha512sum: "ec3b57d8377715ef6286d457b610a2e056aa99db….1"
      type: "java-library"
```

LangStream has Cassandra (java-driver-core) v4.16.0 built in. Here is an example use (no need for dependency):

```yaml
configuration:
  resources:
    - type: "datasource"
      name: "Cassandra"
      configuration:
        service: "astra"
        username: "{{ secrets.astra.username }}"
        password: "{{ secrets.astra.password }}"
        secure-connect-bundle: "{{ secrets.astra.secure-connect-bundle }}"
```

### Manifest

<table><thead><tr><th width="148">Root</th><th width="144">Node</th><th width="94">Type</th><th>Description</th></tr></thead><tbody><tr><td>configuration</td><td><br></td><td><br></td><td>Top level node</td></tr><tr><td><br></td><td>dependencies</td><td>object<br></td><td><p>A collection of artifacts that a pipeline step of resource may need to run. <a href="configuration.md#dependencies">Refer to the spec below.</a></p><p></p><p>Example collection:</p><ul><li>type: “xxx”<br>name: “xxx”<br>configuration:<br>    …</li><li>type: “xxx”<br>name: “xxx”<br>configuration:<br>    …</li></ul></td></tr><tr><td><br></td><td>resources</td><td><br>object</td><td><p>A collection of resources. <a href="configuration.md#dependencies">Refer to the spec below.</a></p><p></p><p>Example collection:</p><ul><li>type: “xxx”<br>name: “xxx”<br>sha: “xxx”<br>    …</li><li>type: “xxx”<br>name: “xxx”<br>sha: “xxx”<br>    …</li></ul></td></tr></tbody></table>

### dependencies

The given artifact will be downloaded, validated, and made available to the pipeline. \


<table><thead><tr><th width="156.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>type</td><td>string (required)</td><td><p>The type of dependency. Supported values are:</p><ul><li>java-library</li></ul><p>Example: “java-library”</p></td></tr><tr><td>name</td><td>string (required)</td><td><p>The name of the dependency. It is used for display and as a reference pointer.<br></p><p>Example: "Postgres JDBC Driver"</p></td></tr><tr><td>url</td><td>string (required)</td><td><p>A fully qualified URL to the dependency artifact.</p><p></p><p>Example: "https://jdbc.postgresql.org/download/postgresql-42.6.0.jar"</p></td></tr><tr><td>sha512sum</td><td>string (required)</td><td><p>The downloaded artifact is validated against this value.<br></p><p>Example: "ec3b57d8377715ef6286d457…”</p></td></tr></tbody></table>

### resources

<table><thead><tr><th width="165.33333333333331">Label</th><th width="101">Type</th><th>Description</th></tr></thead><tbody><tr><td>type</td><td>string</td><td><p>The type of resource. Refer to the configuration resources reference for naming.</p><p></p><p>Example: “datasource”</p></td></tr><tr><td>name</td><td>string</td><td><p>The name of the resource. It is used for display and as a reference pointer.<br></p><p>Example: "PGDataSource"</p></td></tr><tr><td>configuration</td><td>object</td><td>Custom configuration for the given resource. Refer to the configuration resources reference for options.</td></tr></tbody></table>
