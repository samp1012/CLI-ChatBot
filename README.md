# CLI ChatBot

A local command-line chatbot built using a Hugging Face-supported language model. This chatbot maintains short-term conversational memory using a sliding window buffer to simulate coherent multi-turn conversation.

## Table of Contents

- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Sample Interaction](#sample-interaction)  
- [Technologies Used](#technologies-used)  
- [Contact](#contact)  

## Features

- 💬 **Interactive CLI Chat** – Responds to continuous user input in real-time  
- 🧠 **Sliding Window Memory** – Remembers the last 3–5 turns for contextual replies  
- 🧩 **Modular Codebase** – Separated into model, memory, and interface components  
- 🔐 **Environment-safe Authentication** – Uses `.env` to secure Hugging Face token  

## Project Structure

```
CLI-ChatBot/
├── interface.py         # CLI interface loop
├── model_loader.py      # Hugging Face model loader using InferenceClient
├── chat_memory.py       # Sliding window memory logic (last 10 messages)
├── .env                 # Hugging Face API token (not committed)
├── .gitignore           # Ignores virtual environment, cache
└── README.md            # Project documentation
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samp1012/CLI-ChatBot.git
   cd CLI-ChatBot
   ```

2. **Create a virtual environment** *(optional but recommended)*:
   ```bash
   python -m venv myenv
   source myenv/bin/activate     # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install huggingface_hub python-dotenv
   ```

4. **Set your Hugging Face token** in `.env`:
   ```
   HF_TOKEN=your_actual_token_here
   ```

## Usage

Start the chatbot with:

```bash
python interface.py
```

Use `/exit` to terminate the session.

## Sample Interaction

```
Query: What is the capital of France?
Response: The capital of France is Paris.

Query: And what about Italy?
Response: The capital of Italy is Rome.

Query: /exit
Exiting chatbot. Goodbye!
```

## Technologies Used

- **Python 3**
- **Hugging Face Hub** – Text generation
- **dotenv** – Token management
- **Command-line Interface** – Terminal chat execution

## Contact

For any queries or feedback:

- **GitHub**: [samp1012](https://github.com/samp1012)  
- **Email**: samparkadas@gmail.com  
- **LinkedIn**: [Samparka Das](https://www.linkedin.com/in/samparka-das-b4317726b/)  

---
