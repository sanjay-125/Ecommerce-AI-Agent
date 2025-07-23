import pandas as pd
import sqlite3

# Load Excel files
ad_sales = pd.read_excel("C:/Users/sanja/Desktop/Ai/Product-Level Ad Sales and Metrics (mapped).xlsx")
total_sales = pd.read_excel("C:/Users/sanja/Desktop/Ai/Product-Level Total Sales and Metrics (mapped).xlsx")
eligibility = pd.read_excel("C:/Users/sanja/Desktop/Ai/Product-Level Eligibility Table (mapped).xlsx")

# Connect to SQLite DB
conn = sqlite3.connect("C:/Users/sanja/Desktop/Ai/ecommerce.db")

# Save data to SQL tables
ad_sales.to_sql("ad_sales_metrics", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales_metrics", conn, if_exists="replace", index=False)
eligibility.to_sql("product_eligibility", conn, if_exists="replace", index=False)

print("✅ All data loaded into ecommerce.db")
conn.close()
