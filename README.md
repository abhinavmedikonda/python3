# Python3 Learning and Experiments

This repository contains a collection of Python scripts, algorithms, and notebooks for learning, experimenting, and demonstrating various programming concepts, data structures, algorithms, AWS Bedrock, and OOP principles.

## Directory Structure

- **algorithms/**: Classic algorithm problems and solutions (anagrams, bracket matching, API-based tasks, etc.)
- **AWS/**: Amazon Bedrock chatbot notebook and Bedrock API usage scripts.
- **DSA/**: Data Structures and Algorithms examples.
- **examples/**: Basic Python examples (arrays, loops, conditions, JSON, primitives, globals).
- **files/**: File handling utilities (acronym lookup/add, file organization).
- **OOPs/**: Object-Oriented Programming concepts (classes, inheritance, dunder methods, decorators, abstract classes).

## Notable Files

- [`AWS/bedrock_chatbot.ipynb`](AWS/bedrock_chatbot.ipynb): Jupyter notebook for building a chatbot using Amazon Bedrock and LangChain.
- [`AWS/bedrock.py`](AWS/bedrock.py): Script for interacting with Amazon Bedrock models.
- [`files/acronyms.py`](files/acronyms.py): CLI tool to look up or add acronyms.
- [`files/organise.py`](files/organise.py): Script to organize files in directories by type.
- [`OOPs/`](OOPs/): Demonstrates OOP concepts such as inheritance, class/instance variables, decorators, and abstract base classes.

## Requirements

- Python 3.11+
- [boto3](https://pypi.org/project/boto3/) (for AWS scripts)
- [requests](https://pypi.org/project/requests/) (for API and web requests)
- [langchain](https://python.langchain.com/) and [langchain_aws](https://github.com/langchain-ai/langchain-aws) (for Bedrock chatbot, see notebook for details)

## Usage

Clone the repository and run any script directly:

```sh
python files/acronyms.py
python files/organise.py
python algorithms/anagrams_check.py
```

To use the Bedrock chatbot notebook, open [`AWS/bedrock_chatbot.ipynb`](AWS/bedrock_chatbot.ipynb) in JupyterLab or VS Code.

## Notes

- Some scripts require AWS credentials and region configuration.
- The Bedrock chatbot notebook requires the `langchain_aws` package, which may need to be installed separately.
- Example data files are provided in the `files/` directory.

## License

This repository is for