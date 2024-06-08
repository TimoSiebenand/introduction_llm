# Introduction to LLMs

The main item of this repository is the Jupyter Notebook `./introduction_llm/intro_language_model.ipynb`: It contains
several introductory language modelling related topics.

## How to run the notebook?

Make sure
1. Python 3.10 or later is installed.
2. and a HuggingFace account exists.

Clone the repository from GitHub and navigate with a shell into the root directory
of this repository.

Create a virtual python environment:

```
python3 -m venv venv
```

Activate the virtual environment 
```
source venv/bin/activite
```
(The command to activate the virtual environment may differ for Windows users.)

Install all dependencies:
```
pip install -r requirements.txt
```

Login to HuggingFace with 
```
huggingface-cli login
```
(You need a HuggingFace Access Token for that.)

Execute the following python script to load a certain pre-trained model that is used in the Jupyter Notebook: 
```
./introduction_llm/pull_model.py
```

You now are able to run the Notebook as follows:
```
python -m jupyter lab
```

In Jupyter Lab navigate to `intro_language_model.ipynb` and open the notebook.
