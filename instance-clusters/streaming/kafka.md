# kafka

Configuration for a LangStream streaming instance.

### Configuration

<table><thead><tr><th width="101.33333333333331">Label</th><th width="113">Type</th><th>Description</th></tr></thead><tbody><tr><td>admin</td><td>object</td><td><p>A set of name:value pairs that are used to connect a client with the given messaging platform.</p><p></p><p>Example for kafka with auth:</p><p>  bootstrap.servers:&#x3C;kafka-bootstap-address:9093></p><p>  security.protocol: SASL_SSL</p><p>  sasl.jaas.config: "org.apache.kafka.common.security.plain.PlainLoginModule required username='{{ secrets.kafka.tenant }}' password='token:{{ secrets.kafka.token }}';"</p><p>  sasl.mechanism: PLAIN</p><p>  session.timeout.ms: "45000"</p></td></tr></tbody></table>
