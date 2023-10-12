# azure-blob-storage-source

This source agent reads documents as they are uploaded to an Azure blob container. The container will be created if it doesn’t exist.

### Example

Example of reading from a container, extracting the document text, splitting the text into chunks, and outputting each chunk as a message to the output topic.

```yaml
- name: "Read from Azure"
  type: "azure-blob-storage-source"
  output: "output-topic" # optional
  configuration:
    container: documents
    endpoint: "https://<storage-account-name>.blob.core.windows.net."
    storage-account-connection-string: "${ secrets.azure.connection-string }"
```

Use Azure CLI to upload a local file to the container

```bash
az storage container create -n documents
az storage blob upload -f <localfile.txt> -c documents -n new-file.txt
```


### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#azure-blob-storage).