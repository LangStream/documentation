# compute

The compute agent computes field values based on expressions evaluated at runtime. If the field already exists, it will be overwritten.

### Example

Given the input:

```json
{
  "key": {
    "compound": {
      "uuid": "uuidValue",
      "timestamp": 1663616014
    }
  },
  "value" : {
    "first" : "joe",
    "last" : "schmoe",
    "rank" : 1,
    "address" : {
      "zipcode" : "abc-def"
    }
  }
}
```

With an agent configuration of:

```yaml
- name: "Compute a new record"
  type: "compute"
  input: "input-topic" # optional
  output: "output-topic" # optional
  configuration:
    fields:
      - name: "key.newKeyField"
        expression: "5*3"
        type: "INT32"
        optional: true
      - name: "value.first"
        expression: "fn:concat(value.first, ' ')"
        type: "STRING"
        optional: false
      - name: "value.fullName"
        expression: "fn:concat(value.first, value.last)"
        type: "STRING"
        optional: false
```

The output would be:

```json
{
  key: {
    newKeyField: 15
  },
  value: {
    first: “joe ”,
    fullName: “joe schmoe”
  }
}
```

### Topics

#### Input

* Structured only text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

#### Output

* Structured text [?](../agent-messaging.md)
* Implicit topic [?](../agent-messaging.md#implicit-input-and-output-topics)

### Configuration

<table><thead><tr><th width="153.33333333333331">Label</th><th width="160">Type</th><th>Description</th></tr></thead><tbody><tr><td>fields</td><td>object[] (required)</td><td>An array of objects describing how to calculate the field values. Refer to the field table for more info.</td></tr></tbody></table>

#### field

<table><thead><tr><th width="137.33333333333331">Label</th><th width="168">Type</th><th>Description</th></tr></thead><tbody><tr><td>name</td><td>string (required)</td><td><p>The name of the field to be computed. Prefix with “key.” or “value.” to compute the fields in the key or value parts of the message.<br></p><p>Example:</p><p>name: “value.first-name”</p></td></tr><tr><td>expression</td><td>string (required)</td><td>Supports the Expression language syntax. It is evaluated at runtime and the result of the evaluation is assigned to the field (do not include mustache brackets, the agent will fill the value correctly).</td></tr><tr><td>type</td><td>string (required)</td><td>The type of the computed field. this will translate to the schema type of the new field in the transformed message. See type reference below.</td></tr><tr><td>optional</td><td>boolean (optional)</td><td><p>If true, it marks the field as optional in the schema of the transformed message. This is useful when null is a possible value of the compute expression.</p><p></p><p>The default value is “true”</p></td></tr></tbody></table>

field type

<table><thead><tr><th width="128.33333333333331">Label</th><th width="267">Type</th><th>Description</th></tr></thead><tbody><tr><td>INT32</td><td>represents 32-bit integer.</td><td>expression1: "2147483647", expression2: "1 + 1"</td></tr><tr><td>INT64</td><td>represents 64-bit integer.</td><td>expression1: "9223372036854775807", expression2: "1 + 1"</td></tr><tr><td>FLOAT</td><td>represents 32-bit floating point.</td><td>expression1: "340282346638528859999999999999999999999.999999", expression2: "1.1 + 1.1"</td></tr><tr><td>DOUBLE</td><td>represents 64-bit floating point.</td><td>expression1: "1.79769313486231570e+308", expression2: "1.1 + 1.1"</td></tr><tr><td>BOOLEAN</td><td>true or false</td><td>expression1: "true", expression2: "1 == 1", expression3: "value.stringField == 'matching string'"</td></tr><tr><td>DATE</td><td>a date without a time-zone in the <a href="https://www.rfc-editor.org/rfc/rfc3339">RFC3339 format</a></td><td>expression1: "2021-12-03"</td></tr><tr><td>TIME</td><td>a time without a time-zone in the <a href="https://www.rfc-editor.org/rfc/rfc3339">RFC3339 format</a></td><td>expression1: "20:15:45"</td></tr><tr><td>DATETIME</td><td>a date-time with an offset from UTC in the <a href="https://www.rfc-editor.org/rfc/rfc3339">RFC3339 format</a></td><td>expression1: "2022-10-02T01:02:03+02:00", expression2: "2019-10-02T01:02:03Z", expression3: "fn:now()"</td></tr></tbody></table>

{% hint style="info" %}
For more about the expression language, supported functions, and the optional ‘when’ clause, [read the full docs](https://docs.datastax.com/en/streaming/streaming-learning/functions/compute.html#expression-language).
{% endhint %}
