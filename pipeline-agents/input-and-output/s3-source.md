# s3-source

This source agent reads documents as they are uploaded to an S3-compatible bucket. The bucket will be created if it doesn’t exist.

### Example

Example of reading from an S3 bucket, extracting the document text, splitting the text into chunks, and outputting each chunk as a message to the output topic.

```yaml
- name: "Read from S3"
  type: "s3-source"
  output: "output-topic" # optional
  configuration:
    bucketName: documents
    endpoint: "https://s3.eu-west-2.amazonaws.com" # aws s3
    #endpoint: "http://minio.minio-dev.svc.cluster.local:9000" # compatible s3
    username: "${ secrets.s3.username }"
    password: "${ secrets.s3.password }"
```

Example aws S3 command to upload a local document to the bucket:

```bash
aws s3 cp <./a-local-file.txt> s3://documents/a-local-file.txt
```

### Configuration

Checkout the full configuration properties in the [API Reference page](../../building-applications/api-reference/agents.md#s3-source)
