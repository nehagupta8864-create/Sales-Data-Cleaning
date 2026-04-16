import pandas as pd
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("sales_dirty_data.csv")

# Backup
raw_df = df.copy()

# ---------------- COMMON CLEANING ---------------- #

# Column names clean
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove spaces
df["customer_name"] = df["customer_name"].str.strip()
df["city"] = df["city"].fillna("Unknown").str.strip()
df["product"] = df["product"].str.strip().str.title()
df["payment_status"] = df["payment_status"].str.strip().str.capitalize()

# Fix wrong values
df["price"] = df["price"].replace("twenty thousand", 20000)

# Convert types
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Fill missing
df["quantity"] = df["quantity"].fillna(1)
df["payment_status"] = df["payment_status"].fillna("Unknown")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Recalculate total
df["total"] = df["quantity"] * df["price"]

# ==================================================
# 🟢 FILE 1 → ONLY MISSING FILLED (NO DUPLICATE REMOVE)
# ==================================================

df.to_csv("missing_filled_data.csv", index=False)

# ==================================================
# 🔴 FILE 2 → FULL CLEANED (REMOVE DUPLICATES ALSO)
# ==================================================

df_clean = df.drop_duplicates()

df_clean.to_csv("fully_cleaned_data.csv", index=False)

# ---------------- REPORT (ONLY CLEAN DATA) ---------------- #

total_sales = df_clean["total"].sum()

city_sales = df_clean.groupby("city")["total"].sum().sort_values(ascending=False)
product_sales = df_clean.groupby("product")["total"].sum().sort_values(ascending=False)

# Save Excel Report
with pd.ExcelWriter("final_report.xlsx") as writer:
    df_clean.to_excel(writer, sheet_name="Clean Data", index=False)
    city_sales.to_excel(writer, sheet_name="City Sales")
    product_sales.to_excel(writer, sheet_name="Product Sales")

# ---------------- CHART ---------------- #

plt.figure()
city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("city_sales_chart.png")

plt.figure()
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("product_sales_chart.png")

# ---------------- OUTPUT ---------------- #

print("✅ 2 Files Created Successfully!")
print("1️⃣ missing_filled_data.csv (only missing filled)")
print("2️⃣ fully_cleaned_data.csv (fully cleaned)")
print("📊 final_report.xlsx + charts bhi ban gaye")