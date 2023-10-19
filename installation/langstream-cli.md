# LangStream CLI

Use the CLI to manage your control plane, deploy applications, and interact with an application's gateway.

For LangStream CLI commands, see [CLI commands.](../langstream-cli/langstream-cli-commands.md)

To configure the LangStream CLI, see [CLI configuration.](../langstream-cli/langstream-cli-configuration.md)

## Download the CLI

### Mac

```bash
brew install LangStream/langstream/langstream
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

```bash
langstream -h
```

### Enable auto-completion
Installing the binary directly will enable auto-completion for the CLI.

If you installed the CLI with Homebrew, you can enable auto-completion with the following command:

#### ZSH

```zsh
[[ $(grep 'langstream generate-completion' "$HOME/.zshrc") ]] || echo -e "source <(langstream generate-completion)" >> "$HOME/.zshrc"
source $HOME/.zshrc # or open another terminal
```

#### Bash

```bash
[[ $(grep 'langstream generate-completion' "$HOME/.bashrc") ]] || echo -e "source <(langstream generate-completion)" >> "$HOME/.bashrc"
source $HOME/.bashrc # or open another terminal
```



### Step by step guide on Amazon Linux VM

If for some reasons you prefer to install the CLI and test the applications on a remote machine, this is setup you need to go through.

After creating the VM on [EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html), you can run the following commands:

```bash
sudo yum update
# jq, unzip are for the installer
sudo yum install -y docker jq unzip java-11-amazon-corretto-headless
# setup docker

sudo usermod -a -G docker ec2-user
id ec2-user
newgrp docker
sudo systemctl enable docker.service
sudo systemctl start docker.service

# download the CLI
curl -Ls "https://raw.githubusercontent.com/LangStream/langstream/main/bin/get-cli.sh" | bash
source ~/.bashrc

# run the sample application
export OPEN_AI_ACCESS_KEY=your-key-here
langstream docker run test -app https://github.com/LangStream/langstream/blob/main/examples/applications/openai-completions -s https://github.com/LangStream/langstream/blob/main/examples/secrets/secrets.yaml
```



