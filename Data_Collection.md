# Sales Performance Analysis for Retail Business

## Objective
Analyze sales data for a retail business to identify key trends, top-performing products, and customer segments, and provide actionable insights.

---

## Data Collection

### Description
The dataset for this project was simulated using Python’s `Faker` library. It includes sales transactions for a fictional retail company. Each record contains information about the product sold, the customer, and the total sales amount.

### Dataset Fields
- **Order ID**: A unique identifier for each sales transaction.
- **Order Date**: The date on which the order was placed.
- **Product Name**: The name of the product sold.
- **Category**: The product's category (e.g., Electronics, Furniture).
- **Quantity Sold**: The number of units sold in each transaction.
- **Unit Price**: The price per unit of the product.
- **Total Sales**: The total amount for the order (`Quantity Sold * Unit Price`).
- **Customer Name**: The name of the customer who made the purchase.
- **Region**: The geographical region of the customer, such as North, South, East, or West.

### Tools Used
- **Python**: Used for simulating the sales dataset.
- **Faker Library**: To generate realistic customer names, order dates, and unique order IDs.
- **Pandas**: For handling the dataset and saving it as a CSV file.

### Code Snippet

```python
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

num_records = 500
categories = {
    'Electronics': ['Smartphone', 'Laptop', 'Tablet', 'Smartwatch', 'Headphones'],
    'Home Appliances': ['Refrigerator', 'Microwave', 'Washing Machine', 'Vacuum Cleaner'],
    'Furniture': ['Sofa', 'Dining Table', 'Chair', 'Bed', 'Desk'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Sweater']
}
regions = ['North', 'South', 'East', 'West']
orders = []

for _ in range(num_records):
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    quantity_sold = random.randint(1, 10)
    unit_price = round(random.uniform(10.0, 1000.0), 2)
    total_sales = round(quantity_sold * unit_price, 2)

    order = {
        'Order ID': fake.uuid4(),
        'Order Date': fake.date_between(start_date='-1y', end_date='today'),
        'Product Name': product,
        'Category': category,
        'Quantity Sold': quantity_sold,
        'Unit Price': unit_price,
        'Total Sales': total_sales,
        'Customer Name': fake.name(),
        'Region': random.choice(regions)
    }
    orders.append(order)

df_sales = pd.DataFrame(orders)
df_sales.to_csv('sales_data.csv', index=False)
```
### Result

A dataset containing 500 sales records was successfully generated and saved as sales_data.csv.