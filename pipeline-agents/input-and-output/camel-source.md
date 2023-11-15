# camel-source

This source agent reads from an [Apache Camel](https://camel.apache.org) source connector.
Apache Camel is an open-source integration framework for messaging solutions.
LangStream leverages Camel's source connector integration to support any source connector that Camel supports, without having to package a massive library of JARs.

## Example

Documentation for supported Apache Camel source connectors is available [here](https://camel.apache.org/components/4.0.x/).

From the connector's documentation, you'll need the **component-uri** and the **component-options**.

`component-uri` is the URI of the Camel component that the source connector will connect to. This URI defines the source system (like a database, message queue, API endpoint, etc.) and can include various parameters specific to that component.

`component options` are a map of additional options specific to the Camel component being used. These options are appended to the component-uri as query parameters to further configure the behavior of the Camel component.

According to [the Camel documentation](https://camel.apache.org/components/4.0.x/azure-storage-blob-component.html), the Azure blob storage connector's URI structure is `azure-storage-blob://accountName[/containerName][?options]`. The component URI will be populated by the Azure `accountName/containerName`, and the `[?options]` is a `Map.of("blobName", "value1", "credentialType", "accessKey")`.

Declare the **dependency** to the connector in your configuration.yaml file, and LangStream will download it and deploy it into your application.
```yaml
configuration:
  dependencies:
    - name: "Azure blob storage component"
      url: "https://repo1.maven.org/maven2/org/apache/camel/camel-azure-storage-blob/4.1.0/"
      sha512sum: "84bc0574a13e2e8868df4337e9f2b34d57665db2b00ecfff9f651100e6c4e2b5c6c8335e793b292f32ca1c234f87ec9e586f8c06ec15373a880d4a4e75d42c1e"
      type: "java-library"
```

The sha512sum value can be calculated with online tools like [SHA512 File Hash online](https://emn178.github.io/online-tools/sha512_file_hash.html).

## Add Camel component to application
According to [the Camel documentation](https://camel.apache.org/components/4.0.x/azure-storage-blob-component.html), the Azure blob storage connector's URI structure is `azure-storage-blob://accountName[/containerName][?options]`.

Replace the sensitive values in the connector's URI with values from secrets.yaml, so it becomes `azure-storage-blob://{secrets.camel-azure-source.accountName}/${secrets.camel-azure-source.containerName}?blobName=${secrets.camel-azure-source.blobName}`.

Add these secret values to be resolved in your application's secrets.yaml file:
```yaml
  - name: camel-azure-source
    id: camel-azure-source
    data:
      accountName: "${CAMEL_AZURE_SOURCE_ACCOUNT_NAME:-}"
      containerName: "${CAMEL_AZURE_SOURCE_CONTAINER_NAME:-}"
      blobName: "${CAMEL_AZURE_SOURCE_BLOB_NAME:-}"
```

Export the secret values in your environment:
```bash
export CAMEL_AZURE_SOURCE_ACCOUNT_NAME=langstream
export CAMEL_AZURE_SOURCE_CONTAINER_NAME=langstream-container
export CAMEL_AZURE_SOURCE_BLOB_NAME=logs
```

You can now add the camel-source agent to your application pipeline:
```yaml
topics:
  - name: "output-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "read-from-azure"
    type: "camel-source"
    configuration:
      component-uri: "azure-storage-blob://{secrets.camel-azure-source.accountName}/${secrets.camel-azure-source.containerName}?blobName=${secrets.camel-azure-source.blobName}"
      component-options:
         accountName: "${secrets.camel-azure-source.accountName}"
         containerName: "${secrets.camel-azure-source.containerName}"
         blobName: "${secrets.camel-azure-source.blobName}"
```

You **must** provide the component-uri and the component-options in the "configuration" section.

Other values you can configure in `camel-source` are:

`max-buffered-records` is the maximum number of records to buffer in the internal queue (records) before they are processed or read. This setting helps manage memory usage and control the flow of data.

`key-header` specifies the header key that will be used to extract the key of the message from the Camel Exchange. If this header is present in the message, its value will be used as the key of the CamelRecord.

### Configuration

Check out the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#apache-camel-source-camel-source-)
