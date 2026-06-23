import pandas as pd

file_path = "cleaned_analysis_project.xlsx"

sales = pd.read_excel(file_path, sheet_name="cleaned_sales")
items = pd.read_excel(file_path, sheet_name="cleaned_items")

# =========================
# KPI SUMMARY
# =========================

print("\n" + "="*60)
print("KPI SUMMARY")
print("="*60)

print(f"Total Sales      : ₹{sales['total_amount'].sum():,.2f}")
print(f"Total Receipts   : ₹{sales['received_paid_amount'].sum():,.2f}")
print(f"Total Due        : ₹{sales['balance_due'].sum():,.2f}")
print(f"Invoice Count    : {sales['invoice_no'].nunique()}")
print(f"Unique Customers : {sales['party_name'].nunique()}")

# =========================
# TOP CUSTOMERS
# =========================

print("\n" + "="*60)
print("TOP 10 CUSTOMERS BY SALES")
print("="*60)

top_customers = (
    sales.groupby("party_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

# =========================
# TOP DUE CUSTOMERS
# =========================

print("\n" + "="*60)
print("TOP 10 CUSTOMERS BY DUE")
print("="*60)

top_due = (
    sales.groupby("party_name")["balance_due"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_due)

# =========================
# MONTHLY SALES
# =========================

print("\n" + "="*60)
print("MONTHLY SALES")
print("="*60)

monthly_sales = (
    sales.groupby("month")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print(monthly_sales)

# =========================
# PAYMENT ANALYSIS
# =========================

print("\n" + "="*60)
print("PAYMENT TYPE ANALYSIS")
print("="*60)

payment_analysis = (
    sales.groupby("payment_type")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print(payment_analysis)

# =========================
# TOP PRODUCTS BY SALES
# =========================

print("\n" + "="*60)
print("TOP 10 PRODUCTS BY SALES")
print("="*60)

top_products = (
    items.groupby("item_name")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

# =========================
# TOP PRODUCTS BY QUANTITY
# =========================

print("\n" + "="*60)
print("TOP 10 PRODUCTS BY QUANTITY")
print("="*60)

top_quantity = (
    items.groupby("item_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_quantity)

# =========================
# CATEGORY SALES
# =========================

print("\n" + "="*60)
print("CATEGORY SALES")
print("="*60)

category_sales = (
    items.groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)

# =========================
# DAY WISE SALES
# =========================

print("\n" + "="*60)
print("DAY WISE SALES")
print("="*60)

day_sales = (
    sales.groupby("day_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

print(day_sales)

# =========================
# CUSTOMER PERFORMANCE
# =========================

customer_performance = (
    sales.groupby("party_name")
    .agg(
        Sales=("total_amount", "sum"),
        Received=("received_paid_amount", "sum"),
        Due=("balance_due", "sum"),
        Invoices=("invoice_no", "count")
    )
    .sort_values("Sales", ascending=False)
)

print("\n" + "="*60)
print("TOP CUSTOMER PERFORMANCE")
print("="*60)

print(customer_performance.head(10))

# =========================
# EXPORT TO EXCEL
# =========================

with pd.ExcelWriter("analysis_output.xlsx") as writer:
    top_customers.to_excel(writer, sheet_name="Top_Customers")
    top_due.to_excel(writer, sheet_name="Top_Due_Customers")
    monthly_sales.to_excel(writer, sheet_name="Monthly_Sales")
    payment_analysis.to_excel(writer, sheet_name="Payment_Analysis")
    top_products.to_excel(writer, sheet_name="Top_Products")
    top_quantity.to_excel(writer, sheet_name="Top_Product_Qty")
    category_sales.to_excel(writer, sheet_name="Category_Sales")
    day_sales.to_excel(writer, sheet_name="Day_Sales")
    customer_performance.to_excel(writer, sheet_name="Customer_Performance")

print("\nAnalysis exported successfully to analysis_output.xlsx")

#monthly sales 

import matplotlib.pyplot as plt

monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

#top customers
top_customers.head(10).plot(kind='bar')
plt.title("Top Customers")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig("top_customers.png")
plt.show()

#top product

top_products.head(10).plot(kind='bar')
plt.title("Top Products")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

#payment type analysis

payment_analysis.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Payment Type Distribution")
plt.tight_layout()
plt.savefig("payment_type.png")
plt.show()
