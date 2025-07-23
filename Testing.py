import sqlite3
import pandas as pd
from llama_cpp import Llama

# Initialize SQLite connection
db_path = "ecommerce.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tables in your database
tables = ['total_sales_metrics', 'ad_sales_metrics', 'total_sales_metric', 'ad_sales_metric', 'product_eligibility']

# Print schema of each table
def print_schema(table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print(f"\nTable: {table_name}")
    for col in columns:
        print(f"  - {col[1]} ({col[2]})")

# Print schema for all tables
for table in tables:
    print_schema(table)

# Generate schema description for prompt
def get_schema_description():
    schema_text = ""
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        cols = cursor.fetchall()
        schema_text += f"Table {table}:\n"
        for col in cols:
            schema_text += f"  - {col[1]} ({col[2]})\n"
        schema_text += "\n"
    return schema_text

# Initialize LLM (DeepSeek)
llm = Llama(model_path="C:/Users/sanja/Desktop/Ai/models/deepseek-coder-6.7b-instruct.Q4_K_M.gguf")

# Generate SQL query using LLM
def generate_sql(question, schema_desc):
    prompt = f"""### You are an expert in SQL for SQLite databases.
Generate only one SQL query. Do not include explanations.

### Database Schema:
{schema_desc}

### Question:
{question}

### SQL Query:
SELECT """
    # Run inference
    output = llm(prompt, max_tokens=256, stop=[";", "\n\n"])
    sql_query = "SELECT " + output["choices"][0]["text"].strip()
    return sql_query

# Run the generated SQL
def run_query(sql, conn):
    print("\nGenerated SQL:\n", sql)
    try:
        df = pd.read_sql_query(sql, conn)
        return df
    except Exception as e:
        return f"❌ SQL Error: {e}"

# -------------------
# Main workflow
# -------------------
schema_desc = get_schema_description()
question = "What is my total sales? "
sql_query = generate_sql(question, schema_desc)
result = run_query(sql_query, conn)

print("\nQuery Result:")
print(result)
