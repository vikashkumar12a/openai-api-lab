# OpenAI API Lab

A beginner-friendly Python project for learning how to integrate and work with the OpenAI API.

## 📌 Project Overview

This project demonstrates how to:

* Connect a Python application with the OpenAI API
* Load API credentials securely using environment variables
* Send user questions to an AI model
* Display the AI-generated response
* Manage the project using Git and GitHub

## 🛠️ Technologies Used

* Python
* OpenAI API
* python-dotenv
* Git
* GitHub
* VS Code

## 📂 Project Structure

```text
openai-api-lab/
│
├── app.py
├── .gitignore
└── .env
```

> `.env` is kept locally and is not uploaded to GitHub because it contains the API key.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/vikashkumar12a/openai-api-lab.git
```

### 2. Open the project

```bash
cd openai-api-lab
```

### 3. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install openai python-dotenv
```

### 5. Create `.env`

Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your_api_key_here
```

**Never upload your real API key to GitHub.**

### 6. Run the application

```bash
python app.py
```

Enter your question when prompted, and the application will display the AI response.

## 🔐 Security

API keys and other sensitive credentials should be stored in `.env` and excluded from Git using `.gitignore`.

## 🎯 Learning Goals

This project was created to practice:

* Python API integration
* Environment variables
* Git version control
* GitHub repository management
* Commit and push workflow

## 👨‍💻 Author

**Vikash Kumar**

GitHub: https://github.com/vikashkumar12a
