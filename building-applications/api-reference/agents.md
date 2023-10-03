# Agents

LangStream Version: **0.0.23**

<a href="#web-crawler-source-webcrawler-source">Link1</a>
<a href="#webcrawler-source">Link2</a>

## <a name="webcrawler-source"></a>Web crawler source (`webcrawler-source`)

Crawl a website and extract the content of the pages.

|  | Description | Type | Required | Default Value |
| --- | --- | --- | --- | --- |
| `access-key` | Configuration for handling the agent status.<br>Access key for the S3 server. | string |  | minioadmin |
| `allowed-domains` | Domains that the crawler is allowed to access. | array of string |  |  |
| `bucketName` | Configuration for handling the agent status.<br>The name of the bucket. | string |  | langstream-source |
| `endpoint` | Configuration for handling the agent status.<br>The S3 endpoint. | string |  | http://minio-endpoint.-not-set:9090 |
| `forbidden-paths` | Paths that the crawler is not allowed to access. | array of string |  |  |
| `handle-cookies` | Whether to handle cookies. | boolean |  | true |
| `handle-robots-file` | Whether to scan the HTML documents to find links to other pages. | boolean |  | true |
| `http-timeout` | Timeout for HTTP requests. (in milliseconds) | integer |  | 10000 |
| `max-depth` | Maximum depth of the crawl. | integer |  | 50 |
| `max-error-count` | Maximum number of errors allowed before stopping. | integer |  | 5 |
| `max-unflushed-pages` | Maximum number of unflushed pages before the agent persists the crawl data. | integer |  | 100 |
| `max-urls` | Maximum number of URLs that can be crawled. | integer |  | 1000 |
| `min-time-between-requests` | Minimum time between two requests to the same domain. (in milliseconds) | integer |  | 500 |
| `region` | Configuration for handling the agent status.<br>Region for the S3 server. | string |  |  |
| `reindex-interval-seconds` | Time interval between reindexing of the pages. | integer |  | 86400 |
| `scan-html-documents` | Whether to scan HTML documents for links to other sites. | boolean |  | true |
| `secret-key` | Configuration for handling the agent status.<br>Secret key for the S3 server. | string |  | minioadmin |
| `seed-urls` | The starting URLs for the crawl. | array of string |  |  |
| `user-agent` | User agent to use for the requests. | string |  | Mozilla/5.0 (compatible; LangStream.ai/0.1; +https://langstream.ai) |


