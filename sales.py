import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

num_records = 500

categories = {
    'Electronics': ['Smartphone', 'Laptop', 'Tablet', 'Smartwatch', 'Headphones'],
    'Home Appliances': ['Referigerator', 'Microwave', 'Washing Machine', 'Vacuum Cleaner'],
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
        'Product Name':product,
        'Category':category,
        'Quantity Sold': quantity_sold,
        'Unit Price': unit_price,
        'Total Sales': total_sales,
        'Customer Name': fake.name(),
        'Region': random.choice(regions)
    }
    orders.append(order)

df_sales = pd.DataFrame(orders)

df_sales.to_csv('sales_data.csv', index=False)

print("Dataset generated Successfully and Saved as 'sales_data.csv'. ")