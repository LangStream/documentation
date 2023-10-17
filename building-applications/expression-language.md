# Expression Language

LangStream uses an expression language to reference fields of a LangStream record.
See [Structure of a record](topics.md#structure-of-a-message) for more on the parts of a record.

The expression language is required to evaluate the conditional step `when` or the compute step `expression`. The syntax is [EL](https://javaee.github.io/tutorial/jsf-el001.html#BNAHQ), which uses dot notation to access field properties or map keys.

For example, when the [query-vector-db](../pipeline-agents/text-processors/query-vector-db.md) agent queries a Pinecone vector database, the agent uses the expression language to reference the values in "embeddings" and "query-result" with "value.embeddings" and "value.query-result".
```yaml
- name: "Execute Query"
  type: "query-vector-db"
  configuration:
    datasource: "PineconeDatasource"
    query: |
      {
            "vector": ?,
            "topK": 5,
            "filter":
              {"$or": [{"genre": "comedy"}, {"year":2019}]}
       }
    fields:
      - "value.embeddings"
    output-field: "value.query-result"
```

## Operators

The Expression Language supports the following operators:

* Arithmetic: +, - (binary), \*, / and div, % and mod, - (unary)
* Logical: and, &&, or, ||, not, !
* Relational: ==, eq, !=, ne, <, lt, >, gt, <=, ge, >=, le.

## Functions

Utility methods available under the `fn` namespace. For example, to get the current timestamp, use `fn:now()`. The Expression Language supports the following functions:


| **Name (field)**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| concat(input1, input2)            | Returns a string concatenation of input1 and input2. If either input is null, it is treated as an empty|
| concat3(input1, input2, input3) | Returns a string concatenation of input1, input2 and input3. If either input is null, it is treated as an empty|
| contains(input, value)            | Returns true if value exists in input. It attempts string conversion on both input and value if either is not a string. If input or value is null, ir returns false. Do not use this function on lists|
| coalesce(value, valueIfNull)      | Returns value if it is not null, otherwise returns valueIfNull.|
| dateadd(input, delta, unit)       | <p>Performs date/time arithmetic operations on the input date/time.<br><code>input</code> can be either epoch millis or an RFC3339 format like "2022-10-14T10:15:30+01:00"<br><code>delta</code> is the amount of unit to add to input. Can be a negative value to perform subtraction. <code>unit</code> is the unit of time to add or subtract. Can be one of <code>[years, months, days, hours, minutes, seconds, millis]</code>.</p>                                                                                                                                                                                                                                       |
| decimalFromNumber(input)          | <p></p><p>Converts <code>input</code> to a <code>BigDecimal</code>.</p><ul><li><code>input</code> value of the BigDecimal in DOUBLE or FLOAT. If INTEGER or LONG is provided, an unscaled BigDecimal value will be returned.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| decimalFromUnscaled(input, scale) | <p></p><p>Converts <code>input</code> to a <code>BigDecimal</code> with the given <code>scale</code>.</p><ul><li><code>input</code> unscaled value of the BigDecimal. Can be any of STRING, INTEGER, LONG or Array of bytes containing the two's-complement representation in big-endian byte order.</li><li><code>scale</code> the scale of the <code>BigDecimal</code> to create.</li></ul>                                                                                                                                                                                                                                                                                  |
| filter(collection, expression)    | <p>Returns a new collection containing only the elements of <code>collection</code> for which <code>expression</code> is <code>true</code>. The current element is available under the <code>record</code> variable. An example is <code>fn:filter(value.queryResults, "fn:toDouble(record.similarity) >= 0.5")</code></p><p>For all methods, if a parameter is not in the right type, a conversion will be done using the rules described in <a href="https://github.com/datastax/pulsar-transformations/blob/master/README.md#type-conversions">Type conversions</a>. For instance, you can do <code>fn:timestampAdd('2022-10-02T01:02:03Z', '42', 'hours'.bytes)</code></p> |
| fromJson                          | Parse input as JSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| lowercase(input)                  | Changes the capitalization of a string. If input is not a string, it attempts a string conversion. If the input is null, it returns null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| now()                             | Returns the current epoch millis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| replace(input,regex,replacement)  | Replaces each substring of `input` that matches the `regex` regular expression with `replacement`. See [Java's replaceAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#replaceAll\(java.lang.String,java.lang.String\)).                                                                                                                                                                                                                                                                                                                                                                                                                |
| str(input)                        | Converts `input` to a string.|
| toString(input)                   | Converts `input` to a string.|
| toDouble(input)                   | Converts the input value to a DOUBLE number, If the input is `null`, it returns `null`.|
| toInt(input)                      | Converts the input value to an INTEGER number, If the input is `null`, it returns `null`.|
| toListOfFloat(input)              | Converts the input value to a list of FLOAT numbers (embeddings vector), If the input is `null`, it returns `null`. The input must already be a list|
| emptyList()                       |Returns a new empty list|
| listAdd(list, item)               |Returns a new list that contains the contents of a given list plus an item. The input list must be a list and not `null` (you can use fn:emptyList() to create an empty list)|
| emptyMap()                        |Returns a new empty map|
| mapToListOfStructs(map, fields)   | Converts a map to a list of one element that contains only a selection of fields from the map. For instance if your map is `{"text":"value","foo":"bar"}` and you call `mapToListOfStructs(map, 'text')` the result is a list list `[{"text":"value"}]` |
| listToListOfStructs(list, field)   | Converts a list of items to a list of maps with one element named after `field` For instance if your list is `'this is a question'` and you call `listToListOfStructs(list, 'text')` the result is a list list `[{"text":"this is a question"}]`. This is very handful when you have to convert a list of texts to a list of structs|
| uppercase(input)                  | Changes the capitalization of a string. If input is not a string, it attempts a string conversion. If the input is null, it returns null.                                                                                                                                                                                                                                                                                                                                           |
| toJson                            | Converts `input` to a JSON string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| trim(input)                       | Returns the input string with all leading and trailing spaces removed. If the input is not a string, it attempts a string conversion. |
| unpack(input, fieldsList)         | Returns a map containing the elements of `input`, for each field in the `fieldList` you will see an entry in the map. If the input is a string it is converted to a list using the `split()` function with the '`,`' separator |
| split(input, separatorExpression) | Split the input to a list of strings, this is internally using the String.split() function. An empty input corresponds to an empty list. The input is convered to a String using the str() function. |
| timestampAdd(input, delta, unit)  | Returns a timestamp formed by adding `delta` in `unit` to the `input` timestamp. `input` is a timestamp to add to. `delta` is a `long` amount of `unit` to add to `input`. Can be a negative value to perform subtraction. `unit` the string unit of time to add or subtract. Can be one of [`years`, `months`, `days`, `hours`, `minutes`, `seconds`, `millis`]. |


## Conditional when steps

Each step accepts an optional `when` configuration that is evaluated at step execution time.
For example, the [Dispatch agent](../pipeline-agents/flow-control/dispatch.md) evaluates the output from the language-detector agent and routes messages based on whether the value in the "properties.language" field is "en" or "fr". (If neither, it routes to default-topic).
```yaml
  - name: "Detect language"
    type: "language-detector"
    input: "input-topic"
    configuration:
      property: "language"

  - name: "Dispatch"
    type: "dispatch"
    output: default-topic
    configuration:
      routes:
        - when: properties.language == "en"
          destination: topic-english
        - when: properties.language == "fr"
          destination: topic-french
        - when: properties.language == "none"
          action: drop
```
Use the `.` operator to access top level or nested properties on a schema-full key or value.\
For example, `properties.language` or `properties.language.nestedValueField`.

The `when` condition supports the expression language syntax by providing access to the record fields below:

| **Name (field)**  | **Description**                                                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| key:              | the key portion of the record in a KeyValue schema.                                                                                |
| value:            | the value portion of the record in a KeyValue schema, or the message payload itself.                                               |
| messageKey:       | the optional key messages are tagged with (aka. Partition Key).                                                                    |
| topicName:        | the optional name of the topic which the record originated from (aka. Input Topic).                                                |
| destinationTopic: | the name of the topic on which the transformed record will be sent (aka. Output Topic).                                            |
| eventTime:        | the optional timestamp attached to the record from its source. For example, the original timestamp attached to the pulsar message. |
| properties:       | the optional user-defined properties attached to record.                                                                           |
| record:         | the name of a "current record" the agent is processing within a list, ex. [loop-over](/patterns/flare-pattern.md#using-the-embedding-service-over-a-list-of-documents) loops over the list `value.documents_to_retrieve` of individual records `record.embeddings`. Must be `record.value`, can't use nested properties like `record.value.nestedProperties`. |

