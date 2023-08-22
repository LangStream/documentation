# webcrawler-source

The webcrawler-source agent crawls a website and outputs the site's URL and an HTML document. Crawling a website is an ideal first step in a [text embeddings pipeline](https://github.com/LangStream/langstream/tree/main/examples/applications/webcrawler-source).

The S3 bucket only stores metadata about the website and the status of the crawler -  it won’t contain a copy of the crawl data, but a single JSON file with a name computed from the name of the agent and the id of the LangStream application.

### Example

Example webcrawler agent in a pipeline:

```python
pipeline:
  - name: "Crawl the WebSite"
    type: "webcrawler-source"
    configuration:
      seed-urls: "https://docs.langstream.ai/"
      allowed-domains: "https://docs.langstream.ai"
      min-time-between-requests: 100
      max-unflushed-pages: 100
      user-agent: "langstream.ai-webcrawler/1.0"
      bucketName: "{{{secrets.s3-credentials.bucket-name}}}"
      endpoint: "{{{secrets.s3-credentials.endpoint}}}"
      access-key: "{{{secrets.s3-credentials.access-key}}}"
      secret-key: "{{{secrets.s3-credentials.secret}}}"
      region: "{{{secrets.s3-credentials.region}}}"
      idle-time: 5
```

### Topics

**Input**

* None, it’s a source

**Output**

* Structured text (JSON) [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### **Configuration**

<table><thead><tr><th width="145.33333333333331">Label</th><th width="164">Type</th><th>Description</th></tr></thead><tbody><tr><td>allowed-domains</td><td>string</td><td>Checks that seed-url belongs to a domain that is allowed for crawling.</td></tr><tr><td><p></p><p>allowedTags</p></td><td>string</td><td>Controls which HTML meta tags the crawler consumes. Default is "href".</td></tr><tr><td>idle-time</td><td>int</td><td>Time that the agent waits when there are no unprocessed documents available to read from the <code>foundDocuments</code> queue before going to sleep.</td></tr><tr><td>max-unflushed-pages</td><td>int</td><td>Maximum number of unflushed pages before the agent persists the crawl data.</td></tr><tr><td>min-time-between-requests</td><td>int</td><td>Prevents getting banned from site for too many requests. Default value is 100 seconds.</td></tr><tr><td>seed-urls</td><td>string</td><td>The URL to be crawled.</td></tr><tr><td>user-agent</td><td><br>string</td><td>Name of user agent used in connection to server. If none is present, defaults to "langstream.ai-webcrawler/1.0".</td></tr></tbody></table>

### S3 credentials

<table><thead><tr><th width="147.33333333333331">Label</th><th width="165">Type</th><th>Description</th></tr></thead><tbody><tr><td>bucketName</td><td>string (required)</td><td>The name of the bucket.</td></tr><tr><td>endpoint</td><td>string (required)</td><td>The URL of the S3 service.</td></tr><tr><td>username</td><td>string (optional)</td><td>Optional user name credential.</td></tr><tr><td>password</td><td>string (optional)</td><td>Optional password credential.</td></tr></tbody></table>

### Webcrawler-status

| Label         | Type   | Description                                                           |
| ------------- | ------ | --------------------------------------------------------------------- |
| pendingUrls   | String | Holds the URLs that have been discovered but are yet to be processed. |
| remainingUrls | String | Holds the URLs that have been discovered but are yet to be processed. |
| visitedUrls   | String | Holds all URLs that have been visited to prevent cyclic crawling.     |
