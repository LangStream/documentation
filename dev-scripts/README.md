# Dev scripts

## Produce API reference

1. Get the latest api.json from LangStream release and generate the new markdown files.
```bash
version=0.1.x

wget "https://github.com/LangStream/langstream/releases/download/v${version}/api.json" -O dev-scripts/api.json
python3 dev-scripts/main.py dev-scripts/api.json building-applications/api-reference
```
2. Create a PR 
