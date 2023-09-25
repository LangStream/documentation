# LangStream CLI

Use the CLI to manage your control plane, deploy applications, and interact with an application's gateway.

For LangStream CLI commands, see [CLI commands.](../langstream-cli/langstream-cli-commands.md)

To configure the LangStream CLI, see [CLI configuration.](../langstream-cli/langstream-cli-configuration.md)

## Download the CLI

### Mac

```
brew tap LangStream/langstream
brew install langstream
```

### Linux

```bash
curl -Ls "https://raw.githubusercontent.com/LangStream/langstream/main/bin/get-cli.sh" | bash
```

### Windows

Use [WSL](https://learn.microsoft.com/en-us/windows/wsl/about).

{% hint style="info" %}
Want to get started a little quicker? Check out the [LangStream VSCode Extension](https://marketplace.visualstudio.com/items?itemName=DataStax.langstream) for pre-made applications and agent code snippets.
{% endhint %}

### Confirm the installation

Once installed you can test the CLI with the following command.

```
langstream -h
```
