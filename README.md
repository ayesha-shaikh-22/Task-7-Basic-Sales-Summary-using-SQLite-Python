

# **Task 7 – Basic Sales Summary using SQLite & Python**

## **Overview**

This project demonstrates how to create a small SQLite database in Python, insert sample sales data, execute SQL queries, and visualize the results using bar charts.
The aim is to understand how SQL works inside Python and practice basic data analysis.

---

## **Tools Used**

* **Python**
* **SQLite3** (built-in database; no installation required)
* **Pandas**
* **Matplotlib**

---

## **Dataset Information**

There is no pre-given dataset.
You create your own dataset by inserting sample rows into a SQLite database called **`sales_data.db`**.

---

## **Database Structure**

**Table Name:** `sales`

| Column   | Type                                  |
| -------- | ------------------------------------- |
| id       | INTEGER (Primary Key, Auto Increment) |
| product  | TEXT                                  |
| quantity | INTEGER                               |
| price    | REAL                                  |
| date     | TEXT                                  |


---

## **Steps Performed**

### **1. Created a fresh SQLite database**

* Deleted existing `sales_data.db` (if any) to avoid duplicates
* Created a new database file
* Added the `sales` table

### **2. Inserted sample sales records**

Each record includes:

* product name
* quantity sold
* price
* date of sale

### **3. Executed SQL Query**

Aggregated values using:

```
SUM(quantity) AS total_quantity
SUM(quantity * price) AS total_revenue
```

Grouped by product to get totals.

### **4. Loaded results into pandas**

Used `pd.read_sql_query()` to convert SQL output into a DataFrame for easier analysis.

### **5. Created visualizations**

Two bar charts were generated:

1. **Revenue by Product** → `sales_chart.png`
2. **Total Quantity Sold by Product** → `quantity_chart.png`

### **6. Saved all outputs**

The database, code, and charts are saved in the project folder.

---

## **Output**

Project outputs include:

* Sales summary DataFrame (printed in console)
* Product-wise Total Revenue
* Product-wise Total Quantity Sold
* Bar Chart → **sales_chart.png**
* Bar Chart → **quantity_chart.png**

---
This repository contains:

* Python code
* Auto-generated SQLite database
* Two bar chart images
* README.md explaining the entire task

