## Exploratory Data Analysis (EDA)

### Description
This step involves analyzing the cleaned dataset to uncover important insights regarding total sales, top-performing products, customer behavior, and regional sales performance.

### EDA Insights

1. **Total Sales Over Time**: 
   The total sales were plotted over time to observe trends and any potential seasonality in the sales data.

2. **Top 10 Best-Selling Products**: 
   The top 10 products were identified based on total sales. These products contribute significantly to the overall sales revenue.

3. **Sales by Category**: 
   An analysis of sales by product category was conducted to identify which categories generate the most revenue.

4. **Sales by Region**: 
   Regional sales were analyzed to determine which geographical areas have the highest total sales.

5. **Top 10 Customers**: 
   The top 10 customers were identified based on their total spending, which helps target high-value customers for potential marketing campaigns.

### Code Snippets

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df_sales_cleaned = pd.read_csv('cleaned_sales_data.csv')

# Total Sales Over Time
df_sales_cleaned['Order Date'] = pd.to_datetime(df_sales_cleaned['Order Date'])
sales_by_date = df_sales_cleaned.groupby('Order Date')['Total Sales'].sum()
plt.figure(figsize=(10, 6))
plt.plot(sales_by_date.index, sales_by_date.values, marker='o', linestyle='-', color='b')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Top 10 Best-Selling Products
product_sales = df_sales_cleaned.groupby('Product Name')['Total Sales'].sum()
top_10_products = product_sales.sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_10_products.plot(kind='bar', color='green')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

# Sales by Category
category_sales = df_sales_cleaned.groupby('Category')['Total Sales'].sum()
plt.figure(figsize=(8, 6))
category_sales.plot(kind='bar', color='purple')
plt.title('Total Sales by Category')
plt.xlabel('Category
```

### Result
Several insights were derived from the exploratory data analysis, including trends in total sales, top-performing products, regional performance, and top customers. These insights can be used to drive business strategies, such as targeting high-value customers or focusing on top-selling products.