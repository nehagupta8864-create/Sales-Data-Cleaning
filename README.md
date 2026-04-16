# 📊 Sales Data Cleaning & Analysis Project

This project focuses on cleaning messy sales data and generating useful insights using Python, Pandas, and Matplotlib.

---

## 🚀 Project Overview

In real-world datasets, data is often messy and contains:
- Missing values
- Wrong data types
- Duplicate entries
- Inconsistent formatting

This project solves all these problems and creates clean datasets along with reports and charts.

---

## 🛠️ Tools & Technologies Used

- Python 🐍
- Pandas 📊
- Matplotlib 📈

---

## 🧹 Data Cleaning Steps

The following steps are performed in the project:

### 1. Column Cleaning
- Converted column names to lowercase
- Removed extra spaces
- Replaced spaces with underscores

### 2. Data Formatting
- Cleaned text columns like customer name, city, product
- Standardized text (title case, capital letters)

### 3. Handling Missing Values
- Filled missing city with "Unknown"
- Filled missing quantity with 1
- Filled missing payment status

### 4. Fixing Incorrect Values
- Converted "twenty thousand" → 20000

### 5. Data Type Conversion
- Converted quantity and price to numeric
- Converted order_date to datetime

### 6. Feature Engineering
- Created a new column: total = quantity × price

### 7. Duplicate Removal
- Removed duplicate rows in final cleaned dataset

---

## 📂 Output Files

After running the script, the following files are generated:

### 🟢 1. missing_filled_data.csv
- Only missing values are handled
- No duplicates removed

### 🔴 2. fully_cleaned_data.csv
- Fully cleaned dataset
- Duplicates removed

### 📊 3. final_report.xlsx
Contains:
- Clean data
- Sales by city
- Sales by product

### 📈 4. Charts
- city_sales_chart.png
- product_sales_chart.png

---

## 📊 Insights Generated

- Total Sales Calculation
- City-wise Sales Analysis
- Product-wise Sales Analysis

---

## ▶️ How to Run the Project

1. Install required libraries:
`bash
pip install pandas matplotlib
