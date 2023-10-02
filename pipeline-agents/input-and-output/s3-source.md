# s3-source

This source agent reads documents as they are posted to an S3-compatible bucket. The bucket will be created if it doesn’t exist.

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

### Topics

**Input**

* Supported document types
  * pdf
  * doc(x)
  * txt

**Output**

* Structured text (document contents will be byte\[]) [?](../agent-messaging.md#implicit-input-and-output-topics)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

<table><thead><tr><th width="147.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>bucketName</td><td>string (required)</td><td>The name of the bucket.</td></tr><tr><td>endpoint</td><td>string (required)</td><td>The URL of the S3 service.</td></tr><tr><td>username</td><td>string (optional)</td><td>Optional user name credential.</td></tr><tr><td>password</td><td>string (optional)</td><td>Optional password credential.</td></tr></tbody></table>
