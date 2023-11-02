# LangStream Web Interface

The LangStream CLI provides a web interface that you can use to test your application.
The web interface is available at [http://localhost:8092/](http://localhost:8092/).

This interface displays:

* the application logs
* a chatbot-like interface to interact with the gateways
* a diagram of the application pipelines
* the JSON description of the application, both the logical and the physical description (execution plan)


The UI is started automatically when you run the application in docker mode (with `langstream docker run...`), but you can also start it manually using the `langstream app ui` command.

```bash
langstream apps ui application-id
```

With this command the CLI starts a local web service bound on local host and proxies the requests to the LangStream services - both the Control Plane and the API gateway.

The connection to the service is defined in the [CLI configuration](./langstream-cli-configuration.md).

