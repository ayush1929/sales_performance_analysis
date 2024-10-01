import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df_sales_cleaned = pd.read_csv('cleaned_sales_data.csv')

# 1. Total Sales Over Time
df_sales_cleaned['Order Date'] = pd.to_datetime(df_sales_cleaned['Order Date'])
sales_by_date = df_sales_cleaned.groupby('Order Date')['Total Sales'].sum()

plt.figure(figsize=(10, 6))
plt.plot(sales_by_date.index, sales_by_date.values, marker='o', linestyle='-', color='b')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# 2. Top 10 Best-Selling Products
product_sales = df_sales_cleaned.groupby('Product Name')['Total Sales'].sum()
top_10_products = product_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_10_products.plot(kind='bar', color='green')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

# 3. Sales by Category
category_sales = df_sales_cleaned.groupby('Category')['Total Sales'].sum()

plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color='purple')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

# 4. Sales by Region
region_sales = df_sales_cleaned.groupby('Region')['Total Sales'].sum()

plt.figure(figsize=(8, 6))
region_sales.plot(kind='bar', color='orange')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

# 5. Top 10 Customers by Total Sales
customer_sales = df_sales_cleaned.groupby('Customer Name')['Total Sales'].sum()
top_10_customers = customer_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_10_customers.plot(kind='bar', color='blue')
plt.title('Top 10 Customers by Total Sales')
plt.xlabel('Customer Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()
