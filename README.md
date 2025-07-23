
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

### 5. Launch the Streamlit App

```bash
python -m streamlit run app.py
```

Visit `http://localhost:8501` to access the web interface.

---

## 💬 Example Questions (Try on the Webpage)

✅ What is my total sales?

📈 Calculate the RoAS (Return on Ad Spend)

💸 Which product had the highest CPC (Cost Per Click)?

---
## 📹 Demo

Watch this [demo video]([https://drive.google.com/file/d/your-demo-video-link/view](https://drive.google.com/file/d/167Y5xcD1GyPZBshVO1ZrZUVJapxr5HpA/view?usp=drivesdk)) where the API answers:

- What is my total sales?
- Calculate the RoAS (Return on Ad Spend)
- Which product had the highest CPC (Cost Per Click)?

The recording shows the API call and terminal output in real-time.

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
