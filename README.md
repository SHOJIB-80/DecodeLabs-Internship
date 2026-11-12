# DecodeLabs Internship AI Projects

This repository contains two Python-based AI projects completed during the DecodeLabs internship: a rule-based conversational chatbot and an Iris flower classification model built with scikit-learn. Both projects are implemented as standalone scripts and are designed to demonstrate core AI and machine learning concepts through simple, practical examples.

## Overview

The repository is organized into two independent project folders:

- `AI-Chatbot-Project/chatbot.py` implements a command-line chatbot that responds to a small set of predefined prompts.
- `DecodeLabs-AI-Project-2/main.py` loads the Iris dataset, preprocesses the data, trains a K-Nearest Neighbors classifier, and prints evaluation metrics and predictions.

This project set focuses on introductory AI workflows rather than a full-stack web application or production deployment system.

## Features

- Rule-based chatbot with predefined responses for common conversational inputs
- Interactive command-line chat loop with an exit command
- Iris dataset loading and inspection
- Data splitting into training and testing sets
- Feature scaling using `StandardScaler`
- KNN classifier training and evaluation
- Accuracy score, confusion matrix, and classification report output
- Prediction for a new sample flower using the trained model

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application language |
| scikit-learn | Machine learning model creation and evaluation |
| pandas | Dataset loading and data frame handling |
| StandardScaler | Feature normalization before model training |

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
├── README.md
└── .gitignore
```

### Key Files

- `AI-Chatbot-Project/chatbot.py`: Contains the chatbot logic and command-line interaction flow.
- `DecodeLabs-AI-Project-2/main.py`: Implements the supervised learning workflow using the Iris dataset.
- `DecodeLabs-AI-Project-2/Dataset for Data Analytics - Sheet1.csv`: Input dataset used by the classification model.
- `LICENSE`: Repository license file.

## System Architecture

```text
User
  ↓
Python CLI Script
  ↓
Rule-Based Response Logic / scikit-learn Pipeline
  ↓
Output in Terminal
```

The chatbot operates as a simple local script that matches user input against a dictionary of known responses. The machine learning project follows a standard supervised learning workflow: load dataset → split data → scale features → train KNN model → evaluate results → predict a new input.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/SHOJIB-80/DecodeLabs-Internship.git
cd DecodeLabs-Internship
```

Install the required Python dependencies:

```bash
pip install pandas scikit-learn
```

## Running the Project

### 1. Chatbot

```bash
python "AI-Chatbot-Project/chatbot.py"
```

The script starts an interactive terminal session. Type a supported prompt such as `hello`, `hi`, or `help`, and type `exit` to close the session.

### 2. Iris Classification Model

```bash
python "DecodeLabs-AI-Project-2/main.py"
```

This script loads the dataset, displays the first rows, trains a KNN model, prints the accuracy score, confusion matrix, and classification report, and predicts the class of a sample flower.

## Application Usage

### Chatbot Workflow

1. Launch the chatbot script.
2. Enter a command or greeting.
3. The program checks the input against a predefined dictionary.
4. A matching response is printed in the terminal.
5. The session continues until the user enters `exit`.

### Machine Learning Workflow

1. Load the Iris dataset.
2. Inspect the dataset structure.
3. Split the data into training and testing sets.
4. Scale the feature values.
5. Train the KNN model.
6. Evaluate the model using accuracy and classification metrics.
7. Predict the class of a new flower sample.

## Authentication and Authorization

This repository does not include a user authentication system, admin panel, or role-based authorization layer. The scripts are standalone Python programs designed for local execution and demonstration purposes only.

## Testing

This repository does not include an automated test suite or testing framework. Validation is performed by running the scripts directly in the terminal and checking the generated output.

## Known Limitations

- The chatbot only recognizes a small, hardcoded set of inputs.
- The chatbot does not support persistent memory or external API integration.
- The machine learning project uses a built-in example dataset rather than a custom domain-specific dataset.
- There is no deployment configuration, database layer, or web interface in this repository.
- No automated tests or CI pipeline are included.

## Security Considerations

This repository does not implement a production security model. The code does not contain authentication, authorization, user sessions, environment variable management, or secret storage. The chatbot accepts raw terminal input and compares it against a static dictionary, while the machine learning script uses local data and does not expose credentials or API keys.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

SHOJIB-80
