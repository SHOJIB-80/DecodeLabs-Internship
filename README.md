# DecodeLabs Internship AI Projects

A small collection of Python projects developed during the DecodeLabs internship, featuring a rule-based command-line chatbot and an Iris flower classification example using scikit-learn.

## Overview

This repository contains two independent projects that demonstrate introductory AI and machine learning workflows:

- **DecodeBot** matches user input against a fixed set of conversational prompts and prints predefined responses.
- **Iris classification** trains and evaluates a K-Nearest Neighbors (KNN) model using scikit-learn's built-in Iris dataset, then predicts the class of a sample flower.

These are standalone command-line programs; the repository does not include a web application, database, or deployment setup.

## Features

- Interactive terminal chatbot with predefined responses and an `exit` command
- Iris dataset inspection and stratified train/test split
- Feature scaling and a five-neighbor KNN classifier in a scikit-learn pipeline
- Accuracy, confusion matrix, and classification report output
- Example prediction for a new flower sample

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Implements both command-line projects |
| scikit-learn | Provides the Iris dataset, preprocessing, KNN model, and evaluation metrics |
| pandas | Creates and displays a DataFrame for dataset inspection |

## Project Structure

```text
DecodeLabs-Internship/
├── AI-Chatbot-Project/
│   ├── assests/
│   │   └── images/
│   └── chatbot.py
├── DecodeLabs-AI-Project-2/
│   ├── Dataset for Data Analytics - Sheet1.csv
│   └── main.py
├── LICENSE
└── README.md
```

`DecodeLabs-AI-Project-2/main.py` uses scikit-learn's built-in Iris dataset. The CSV file is present in the project directory but is not loaded by the current script.

## Requirements

- Python 3
- `pandas`
- `scikit-learn`

## Installation

Clone the repository and install the Python dependencies:

```bash
git clone https://github.com/SHOJIB-80/DecodeLabs-Internship.git
cd DecodeLabs-Internship
python -m pip install pandas scikit-learn
```

## Running the Projects

### Rule-Based Chatbot

```bash
python "AI-Chatbot-Project/chatbot.py"
```

Enter a supported prompt such as `hello`, `hi`, or `help`. Responses are matched against the complete input after trimming whitespace and converting it to lowercase. Enter `exit` to end the session.

### Iris Flower Classification

```bash
python "DecodeLabs-AI-Project-2/main.py"
```

The script displays a preview and shape of the Iris data, trains the model using an 80/20 stratified split, prints evaluation metrics, and predicts the class for a hardcoded sample flower.

## How the Projects Work

### Chatbot

The chatbot uses a Python dictionary to map exact text inputs to fixed responses. Inputs that do not match a dictionary key receive a fallback response. It does not use a trained language model or an external AI service.

### Iris Classifier

The classification script loads the built-in Iris dataset, creates a pandas DataFrame for display, and splits the feature data into training and test sets. A scikit-learn pipeline standardizes the features and applies a KNN classifier with five neighbors. The model is evaluated on the test split and used to predict one sample.

## Authentication and Data

The projects do not implement user accounts, authentication, authorization, or a database. The chatbot processes input in the local terminal. The classifier uses scikit-learn's built-in Iris dataset; it does not read the CSV file included in the repository.

## Testing

No automated test suite or CI configuration is included. Each project can be run directly using the commands above.

## Limitations

- The chatbot recognizes only exact phrases in its predefined response dictionary and has no conversation memory.
- The Iris model is a small example and does not save a trained model or provide a reusable API.
- The CSV file in the classifier project is not used by the current implementation.
- The repository does not include a web interface, deployment configuration, or automated tests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the full text.

## Author

SHOJIB-80
