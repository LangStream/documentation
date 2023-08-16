# open-ai-configuration

An OpenAI resource used for LLM functions.

### **Configuration**

<table><thead><tr><th width="158.33333333333331">Labele</th><th width="111">Type</th><th>Description</th></tr></thead><tbody><tr><td>url</td><td>string</td><td><p>Connection to OpenAI api. Typically this is a reference to a secret.</p><p></p><p>Example: “{{ secrets.open-ai.url }}”</p></td></tr><tr><td>access-key</td><td>string</td><td><p>Your OpenAI key. Typically this is a reference to a secret.</p><p></p><p>Example: "{{ secrets.open-ai.access-key }}"</p></td></tr><tr><td>provider</td><td>string</td><td><p>OpenAI provider type. Supported values are:</p><ul><li>“azure”</li></ul></td></tr></tbody></table>
