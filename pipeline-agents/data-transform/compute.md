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

### Expression Language

To support [Conditional steps](compute.md#conditional-steps) and the Compute Transform, an expression language is required to evaluate the conditional step `when` or the compute step `expression`. The syntax is [EL](https://javaee.github.io/tutorial/jsf-el001.html#BNAHQ), which uses the dot notation to access field properties or map keys. It supports the following operators and functions:

#### Operators

The Expression Language supports the following operators:

* Arithmetic: +, - (binary), \*, / and div, % and mod, - (unary)
* Logical: and, &&, or, ||, not, !
* Relational: ==, eq, !=, ne, <, lt, >, gt, <=, ge, >=, le.

#### Functions

Utility methods available under the `fn` namespace. For example, to get the current timestamp, use `fn:now()`. The Expression Language supports the following functions:\


| **Name (field)**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| concat(input1, input2)            | Returns a string concatenation of input1 and input2. If either input is null, it is treated as an empty string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| contains(input, value)            | Returns true if value exists in input. It attempts string conversion on both input and value if either is not a string. If input or value is null, ir returns false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coalesce(value, valueIfNull)      | Returns value if it is not null, otherwise returns valueIfNull.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| dateadd(input, delta, unit)       | <p>Performs date/time arithmetic operations on the input date/time.<br><code>input</code> can be either epoch millis or an RFC3339 format like "2022-10-14T10:15:30+01:00"<br><code>delta</code> is the amount of unit to add to input. Can be a negative value to perform subtraction. <code>unit</code> is the unit of time to add or subtract. Can be one of <code>[years, months, days, hours, minutes, seconds, millis]</code>.</p>                                                                                                                                                                                                                                       |
| decimalFromNumber(input)          | <p></p><p>Converts <code>input</code> to a <code>BigDecimal</code>.</p><ul><li><code>input</code> value of the BigDecimal in DOUBLE or FLOAT. If INTEGER or LONG is provided, an unscaled BigDecimal value will be returned.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| decimalFromUnscaled(input, scale) | <p></p><p>Converts <code>input</code> to a <code>BigDecimal</code> with the given <code>scale</code>.</p><ul><li><code>input</code> unscaled value of the BigDecimal. Can be any of STRING, INTEGER, LONG or Array of bytes containing the two's-complement representation in big-endian byte order.</li><li><code>scale</code> the scale of the <code>BigDecimal</code> to create.</li></ul>                                                                                                                                                                                                                                                                                  |
| filter(collection, expression)    | <p>Returns a new collection containing only the elements of <code>collection</code> for which <code>expression</code> is <code>true</code>. The current element is available under the <code>record</code> variable. An example is <code>fn:filter(value.queryResults, "fn:toDouble(record.similarity) >= 0.5")</code></p><p>For all methods, if a parameter is not in the right type, a conversion will be done using the rules described in <a href="https://github.com/datastax/pulsar-transformations/blob/master/README.md#type-conversions">Type conversions</a>. For instance, you can do <code>fn:timestampAdd('2022-10-02T01:02:03Z', '42', 'hours'.bytes)</code></p> |
| fromJson                          | Parse input as JSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| lowercase(input)                  | Changes the capitalization of a string. If input is not a string, it attempts a string conversion. If the input is null, it returns null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| now()                             | Returns the current epoch millis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| replace(input,regex,replacement)  | Replaces each substring of `input` that matches the `regex` regular expression with `replacement`. See [Java's replaceAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#replaceAll\(java.lang.String,java.lang.String\)).                                                                                                                                                                                                                                                                                                                                                                                                                |
| split(input, separatorExpression) | <p></p><p>Split the input to a list of strings, this is internally using the String.split() function. An empty input corresponds to an empty list. The input is convered to a String using the str() function.</p><p><br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| str(input)                        | Converts `input` to a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| timestampAdd(input, delta, unit)  | <p></p><p>Returns a timestamp formed by adding <code>delta</code> in <code>unit</code> to the <code>input</code> timestamp.</p><ul><li><code>input</code> a timestamp to add to.</li><li><code>delta</code> a <code>long</code> amount of <code>unit</code> to add to <code>input</code>. Can be a negative value to perform subtraction.</li><li><code>unit</code> the string unit of time to add or subtract. Can be one of [<code>years</code>, <code>months</code>, <code>days</code>, <code>hours</code>, <code>minutes</code>, <code>seconds</code>, <code>millis</code>].</li></ul>                                                                                     |
| toDouble(input)                   | Converts the input value to a DOUBLE number, If the input is `null`, it returns `null`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| toInt(input)                      | Converts the input value to an INTEGER number, If the input is `null`, it returns `null`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| uppercase(input)                  | Changes the capitalization of a string. If input is not a string, it attempts a string conversion. If the input is null, it returns null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| toJson                            | Converts `input` to a JSON string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| trim(input)                       | Returns the input string with all leading and trailing spaces removed. If the input is not a string, it attempts a string conversion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| unpack(input, fieldsList)         | Returns a map containing the elements of `input`, for each field in the `fieldList` you will see an entry in the map. If the input is a string it is converted to a list using the `split()` function with the '`,`' separator                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

#### Conditional Steps

Each `step` accepts an optional `when` configuration that is evaluated at step execution time against current records (the current step in the transform pipeline).

\
The `when` condition supports the expression language syntax, which provides access to the record attributes as follows:

| **Name (field)**  | **Description**                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| key:              | the key portion of the record in a KeyValue schema.                                                                                |
| value:            | the value portion of the record in a KeyValue schema, or the message payload itself.                                               |
| messageKey:       | the optional key messages are tagged with (aka. Partition Key).                                                                    |
| topicName:        | the optional name of the topic which the record originated from (aka. Input Topic).                                                |
| destinationTopic: | the name of the topic on which the transformed record will be sent (aka. Output Topic).                                            |
| eventTime:        | the optional timestamp attached to the record from its source. For example, the original timestamp attached to the pulsar message. |
| properties:       | the optional user-defined properties attached to record.                                                                           |

You can use the `.` operator to access top level or nested properties on a schema-full key or value.\
For example, `key.keyField1` or `value.valueFiled1.nestedValueField`.
