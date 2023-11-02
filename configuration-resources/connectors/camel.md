# Using Apache Camel connectors

Configuration for LangStream Sources using Apache Camel.

### Deplying the component into your LangStream application

LangStream doesn't bundle all the Camel connectors, but you can easily deploy them into your application.

In your configuration.yaml file you declare the **dependency** to the connector, and LangStream will download it and deploy it into your application.

```yaml
configuration:
  dependencies:
    - name: "Apache Camel GitHub component"
      url: "https://repo1.maven.org/maven2/org/apache/camel/camel-github/4.1.0/camel-github-4.1.0.jar"
      sha512sum: "f40e55ddfde21e11e6a26fbb50e4f75df37976c673dbc4aeeaa350257b0179f4a9a71f099f8ac3cbc60cc9d8ff9559984a304fb7d6785bcfb22a9943ceb8d7bd"
      type: "java-library"
    - name: "Apache Camel GitHub component - dependency"
      url: "https://repo1.maven.org/maven2/org/eclipse/mylyn/github/org.eclipse.egit.github.core/2.1.5/org.eclipse.egit.github.core-2.1.5.jar"
      sha512sum: "4fab14efed656b6705ad74ab9c05a346fe4fdc737b1b5130842aee7ebba98b895b7cb8c35d15e3da150116f445ae3b5c88daaaa5319c39144cb365247b9d0630"
      type: "java-library"
```

You have to bundle all the jars needed by the connector, in this example the Apache Camel GitHub component requires the org.eclipse.egit.github.core jar file.

The jar files are downloaded by the LangStream CLI when you are deploying the application and then copied to the java/lib directory.
You are not required to use this mechanism, you can copy manually the jar files.
But if you use the dependency mechanism, the LangStream CLI will check the sha512sum of the files to make sure that they are not corrupted.

It is suggested to add a .gitignore file into your application in order to not commit the jar file into your git repository.


### Apache Camel Sources

Once you have your connector deployed into your application, you can use it in your pipeline.

This is an example about how to configure a Source that reads events from GitHub

```yaml
topics:
  - name: "output-topic"
    creation-mode: create-if-not-exists
pipeline:
  - name: "read-from-github"
    type: "camel-source"

    configuration:
      component-uri: "github:PULLREQUESTCOMMENT/${secrets.camel-github-source.branch}"
      component-options:
         oauthToken: "${secrets.camel-github-source.oauthToken}"
         repoName: "${secrets.camel-github-source.repoName}"
         repoOwner: "${secrets.camel-github-source.repoOwner}"
  - name: "keep only the contents of the comment"
    type: "compute"
    output: "output-topic"
    configuration:
        fields:
           - name: "value"
             expression: "value.body"
```

In the "configuration" section you must provide the component-uri and the component-options.

All the component-options are passed to the component as additional parameters in the query string, appended to the component-uri.
This mechanism helps you in defining each property in a separate secret, so that you can easily rotate the secrets without changing the pipeline configuration.
Also The camel-source agent will automatically URL encode the values of the parameters passed to the querystring.
