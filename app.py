import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from llama_cpp import Llama

# Load Local LLM (DeepSeek)
llm = Llama(model_path="models/deepseek-coder-6.7b-instruct.Q4_K_M.gguf")

# Connect to SQLite DB
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Get schema from known tables
def get_schema():
    tables = ['total_sales_metrics', 'ad_sales_metrics', 'total_sales_metric', 'ad_sales_metric', 'product_eligibility']
    schema = ""
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        cols = cursor.fetchall()
        schema += f"Table {table}:\n"
        for col in cols:
            schema += f"  - {col[1]} ({col[2]})\n"
        schema += "\n"
    return schema.strip()

schema_text = get_schema()

# SQL Generator via DeepSeek
def generate_sql(question, schema_desc):
    prompt = f"""
You are a helpful assistant that writes correct, executable SQLite SQL queries based only on the given schema.

Schema:
{schema_desc}

Question: "{question}"

Write only a valid SQL query (no explanation), and ensure it ends with a semicolon.
SQL:
"""
    response = llm(prompt, max_tokens=1024, stop=[";"])
    raw_sql = response['choices'][0]['text'].strip()

    # 🧹 Clean SQL: remove ``` blocks if present
    if raw_sql.startswith("```"):
        raw_sql = raw_sql.strip("`")  # removes leading and trailing backticks
        raw_sql = raw_sql.split("\n", 1)[-1]  # remove first line like ```sql
        if raw_sql.endswith("```"):
            raw_sql = raw_sql.rsplit("```", 1)[0]

    return raw_sql.strip()



# Run SQL and return DataFrame or error
def run_query(sql):
    try:
        df = pd.read_sql_query(sql, conn)
        return df
    except Exception as e:
        return f"❌ SQL Error: {e}"

# Optional: show bar chart if suitable
def plot_if_possible(df):
    try:
        if df.shape[1] == 2 and pd.api.types.is_numeric_dtype(df.iloc[:, 1]):
            fig, ax = plt.subplots()
            df.plot(kind='bar', x=df.columns[0], y=df.columns[1], ax=ax, legend=False)
            ax.set_ylabel(df.columns[1])
            st.pyplot(fig)
    except Exception as e:
        st.warning(f"⚠️ Could not plot chart: {e}")

# Streamlit UI
st.set_page_config(page_title="🧠 E-commerce AI SQL Assistant", layout="centered")
st.title("🛒 AI-Powered E-commerce SQL Assistant")
st.markdown("Ask questions about your **ecommerce.db** in plain English. The AI will generate and execute SQL queries for you.")

user_question = st.text_input("💬 Ask your question:")

if user_question:
    with st.spinner("🤖 Generating SQL query..."):
        sql = generate_sql(user_question, schema_text)
        st.code(sql, language="sql")
        result = run_query(sql)

        if isinstance(result, pd.DataFrame):
            st.success("✅ Query executed successfully!")
            st.dataframe(result)
            plot_if_possible(result)
        else:
            st.error(result)
