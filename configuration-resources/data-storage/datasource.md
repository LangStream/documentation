# datasource

A data source resource used to interact with a database.

### **Configuration**

<table><thead><tr><th width="182.33333333333331">Label</th><th width="139">Type</th><th>Description</th></tr></thead><tbody><tr><td>service</td><td>string</td><td><p>The type of service. Currently supported values are:</p><ul><li>jdbc</li><li>astra</li></ul><p>Example: “jdbc”</p></td></tr><tr><td>driverClass</td><td>string</td><td>If using “jdbc” type, the class namespace of the data source</td></tr><tr><td>url</td><td>string</td><td>If using “jdbc” type, the data source connection string</td></tr><tr><td>user</td><td>string</td><td>the creds</td></tr><tr><td>password</td><td>string</td><td>the creds</td></tr><tr><td>secureBundle</td><td>string</td><td>If using “astra” type, this is the base64 encoded secure bundle of the database.</td></tr></tbody></table>
