---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Build and install (source)

LangStream uses Maven as its build system. When the below script is run the project source will be tested, compiled, and the container images will be built.

### Requirements

* Docker
* Java 17
* Git
* Python 3.11+ and PIP

### Clone the project

This will clone the latest code of the [project](https://github.com/LangStream/langstream) into the "langstream" folder.

```
git clone https://github.com/LangStream/langstream
```

### Build the project

These commands will compile source, build the CLI tarball, and install Docker images.

```bash
cd langstream
pip install -r requirements.txt
./docker/build.sh
```

### Test local changes with mini-langstream

If you want to test local code changes, you can use `mini-langstream`.

```bash
mini-langstream dev start
```

This command will build the images in the `minikube` context and install all the LangStream services with the snapshot image.

Once the cluster is running, if you want to build abd load a new version of a specific service you can run:

```bash
mini-langstream dev build <service>
```

or for all the services
```bash
mini-langstream dev build
```


### Locate the CLI

During the build, the latest CLI has created in the `bin` folder.

```bash
./bin/langstream --version
```

Please note that this CLI uses the conf/cli.yaml file and it does not behave the same way as the CLI installed with brew, that uses the $HOME/.langstream/config file with a different format.