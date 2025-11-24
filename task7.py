import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------------------
# DELETE OLD FILE IF EXISTS (avoid errors)
# ----------------------------------------
if os.path.exists("sales_data.db"):
    os.remove("sales_data.db")

# ----------------------------------------
# CREATE NEW DATABASE + TABLE
# ----------------------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    date TEXT NOT NULL
)
""")

# ----------------------------------------
# INSERT CLEAN SAMPLE DATA
# ----------------------------------------
sample_data = [
    ("Cake", 5, 300, "2025-01-01"),
    ("Pastry", 10, 80, "2025-01-01"),
    ("Bread", 8, 40, "2025-01-02"),
    ("Cake", 3, 300, "2025-01-03"),
    ("Cookies", 15, 20, "2025-01-03"),
    ("Brownie", 12, 50, "2025-01-04"),
    ("Muffin", 7, 60, "2025-01-05"),
    ("Donut", 9, 30, "2025-01-06")
]

cursor.executemany("""
INSERT INTO sales (product, quantity, price, date)
VALUES (?, ?, ?, ?)
""", sample_data)

conn.commit()

# ----------------------------------------
# RUN SQL QUERY
# ----------------------------------------
query = """
SELECT product,
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)
print("SALES SUMMARY:\n")
print(df)

# ----------------------------------------
# BAR CHART
# ----------------------------------------
plt.figure(figsize=(8,5))
plt.bar(df['product'], df['total_revenue'])
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# ----------------------------------------
# TOTAL QUANTITY BAR CHART
# ----------------------------------------
plt.figure(figsize=(8,5))
plt.bar(df['product'], df['total_quantity'])
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.title("Total Quantity Sold by Product")
plt.tight_layout()
plt.savefig("quantity_chart.png")
plt.show()

conn.close()
