# 🤖 AI Chatbot GUI (using GPT-2 + Transformers)

A simple chatbot with graphical interface (Tkinter), using the GPT-2 model powered by `transformers`.  
Includes full test coverage with `pytest` and `behave` and structured in MVC architecture.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/youruser/chatbot-ai-gui.git
cd chatbot-ai-gui
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🧠 GPT-2 Model (via transformers)

This project uses gpt2 from Hugging Face, locally via the transformers library:

```bash
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
```

No token is needed — the model is downloaded the first time you run.

## 🖥️ Run the GUI

```bash
python main.py
```
## ✅ Running Tests

### 1. Unit Tests

```bash
python -m pytest tests/unit
```

### 2. BDD (with behave)
```bash
behave tests/bdd
```
## 📁 Project Structure
### CHATBOT/
├── app/
│ ├── model/
│ ├── view/
│ └── controller/
├── tests/
│ ├── unit/
│ └── bdd/
├── venv
├── main.py
├── requirements.txt
└── README.md

## 🙋‍♂️ Author

Developed by Renato Souza 
🔗 https://rena7osouza.github.io/
📫 renatofrancisco@hotmail.com