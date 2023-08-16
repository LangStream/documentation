# Application Lifecycle

### Application lifecycle

When a developer deploys a new application to the LangStream control plane, a few steps are taken to ensure the application's success. Once the topics and agents are built, the control plane monitors the application's health and reports on issues.

Here is the typical lifecycle of a LangStream application:

1. Deploy to control plane
2. Download dependencies (if declared)
3. Create a final application artifact
4. Plan the topic and agent layout
5. Validate connections to resources (if declared) and message brokers
6. Create the topics (in the messaging platform)
7. Create the processing agent(s) (as a statefulset)
8. Start processing data
9. Monitor agent's health (and report)

If you are familiar with the design of Kubernetes, then you will understand the choice of an agent being a StatefulSet. A desired number of pods in the set is established, and in the event of a crash, Kubernetes will make every effort to reconcile with a new pod. Each pod has a “sticky” identity. This makes debugging and reporting easier to understand.

\
The base image of a pod is custom to LangStream. There is quite a bit of additional management and tooling included, to help enhance the agent’s processing capabilities. Because LangStream's focus is on generative AI, many of these tools are centered around that. Libraries like LangChain and OpenAI are included in the image.

### Promoting an application through environments

Once you have the application in a stable place, you’ll need to promote it off your desktop into a higher managed environment. Hopefully, your environments keep a minimum parity between them and the only addressable changes are to the infrastructure (urls, passwords, etc). This is the purpose of the secrets and instance manifests being separate from the application manifest. You can interchange these files while still using the same application and promote in a stable, known way.
