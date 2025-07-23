
# 🛒 E-commerce AI Agent

A local AI-powered agent that answers natural language queries about product-level sales, ad spend, and eligibility metrics using your Excel data.

[![GitHub](https://img.shields.io/badge/Repo-Link-informational?style=flat&logo=github)](https://github.com/sanjay-125/Ecommerce-AI-Agent.git)

---

## 🚀 Features

- 🔎 Ask questions like:
  - "What is the total RoAS for item X?"
  - "Which products are eligible but have low ad spend?"
  - "What’s the most profitable product?"
- 🤖 Uses a local LLM (DeepSeek-Coder 6.7B) for privacy & efficiency.
- 💽 Converts Excel sheets to SQLite DB for structured querying.
- 🌐 Flask-powered local web API for interaction.

---

## 📁 File Structure

```
📦Ecommerce-AI-Agent
 ┣ 📂Dataset
 ┃ ┣ 📄 Product-Level Ad Sales and Metrics (mapped).xlsx
 ┃ ┣ 📄 Product-Level Eligibility Table (mapped).xlsx
 ┃ ┣ 📄 Product-Level Total Sales and Metrics (mapped).xlsx
 ┣ 📂models
 ┣ 📄 app.py
 ┣ 📄 download_model.py
 ┣ 📄 load_data_to_sqlite.py
 ┣ 📄 Testing.py
 ┣ 📄 ecommerce.db
 ┣ 📄 README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/sanjay-125/Ecommerce-AI-Agent.git
cd Ecommerce-AI-Agent
```

### 2. Create Environment

```bash
pip install -r requirements.txt
```

### 3. Download the Model

```bash
python download_model.py
```

This will download `deepseek-coder-6.7b-instruct.Q4_K_M.gguf` into the `models/` folder.

### 4. Load the Data to SQLite

```bash
python load_data_to_sqlite.py
```

### 5. Start the API

```bash
python app.py
```

Use `http://127.0.0.1:5000/ask` to send queries to the agent.

---

## 📌 API Usage

Send a POST request to:

```http
POST /ask
Content-Type: application/json

{
  "question": "What is the RoAS for item 123?"
}
```

---

## 📊 Data Sources

- Product-Level Ad Sales and Metrics
- Product-Level Total Sales
- Product-Level Eligibility Table

---

## 🤝 Credits

Built with ❤️ by [Sanjay R](https://github.com/sanjay-125)

Model: [DeepSeek-Coder 6.7B](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct)

---

## 📜 License

MIT License
