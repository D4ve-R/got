![License](https://img.shields.io/badge/license-MIT-green)
# `got`
## git, but with ai

`got` is a Python package that automates the process of generating meaningful commit messages based on the output of `git diff`. It utilizes AI to analyze code changes and creates descriptive commit messages, reducing the burden on developers to come up with commit messages.

## Features

- Automatically generates informative commit messages.
- Supports multiple AI models for commit message generation.


## Usage

You can use `got` just like git, in fact it is git under the hood.

```bash
got add . 
got commit
```

`got` will analyze the changes in your codebase using AI and provide a commit message based on that.

## Installation
`got` depends on `git` and `python3`.
### from source
```bash
cd got
pip install -e .
```

## Integrations

`got` supports multiple backends. Currently, it supports the following backends:
* huggingface, which will run models locally using the huggingface transformers library
* openai, which will use the openai API to generate commit messages (requires an API key) 

You can add your own backend by implementing `got.backend.client`.

## Todo
- [ ] Train a better model
- [ ] Add more models
- [ ] Add more backends

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Experiments

running hf model [mamiksik/T5-commit-message-generation](https://huggingface.co/mamiksik/T5-commit-message-generation) takes roughly 10 seconds on a 2019 macbook pro.
Quality is not great, but it's a start.

openai gpt-turbo-3.5 usage with 20 commits costs ~$0.02, depending on the length of the commit messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
