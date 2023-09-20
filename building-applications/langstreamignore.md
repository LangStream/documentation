# Langstreamignore

Similar to .gitignore, `.langstreamignore` allows you to specify which files or folders should be excluded from the ZIP package when deploying or updating a LangStream application.

If a `.langstreamignore` file exists in your application directory, LangStream traverses the directory structure to decide which files should be included in or excluded from the ZIP file based on the rules in `.langstreamignore`.

There is currently no support for .langstreamignore files in subfolders.&#x20;

You can also associate `.langstreamignore` with the `.gitignore` filetype in your IDE to ignore the listed file types.&#x20;

See an example`.langstreamignore`file [here.](https://github.com/LangStream/langstream/blob/main/examples/applications/langchain-source/.langstreamignore)
