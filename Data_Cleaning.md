## Data Cleaning

### Description
The dataset was cleaned to ensure accuracy in the analysis. The following issues were identified and addressed:

-**Missing Values**: Checked and handled any missing values by either filling them with appropriate values or dropping rows.
-**Duplicate Entries**: Identified and removed any duplicate records to avoid bias.
-**Data Types**: Ensured that columns had the correct data types, especially the 'Order Date' (converted to datetime) and numerical columns like 'Quantity Sold' and 'Total Sales'.
-**Outliers**: Reviewed statistical summaries and handled outliers where necessary.
-**Normalization**: Applied normalization to the 'Total Sales' column for consistency across data.

### Cleaning Steps

```python
# Python code for data cleaning steps

import pandas as pd

# Load the dataset
df_sales = pd.read_csv('sales_data.csv')

# Check for missing values
df_sales = df_sales.dropna()

# Remove duplicate rows
df_sales = df_sales.drop_duplicates()

# Ensure correct data types
df_sales['Order Date'] = pd.to_datetime(df_sales['Order Date'])
df_sales['Quantity Sold'] = pd.to_numeric(df_sales['Quantity Sold'], errors='coerce')
df_sales['Unit Price'] = pd.to_numeric(df_sales['Unit Price'], errors='coerce')
df_sales['Total Sales'] = pd.to_numeric(df_sales['Total Sales'], errors='coerce')

# Handle outliers (optional)
df_sales = df_sales[df_sales['Quantity Sold'] <= 100]

# Normalize 'Total Sales'
df_sales['Total Sales Normalized'] = (df_sales['Total Sales'] - df_sales['Total Sales'].min()) / (df_sales['Total Sales'].max() - df_sales['Total Sales'].min())

# Save the cleaned dataset
df_sales.to_csv('cleaned_sales_data.csv', index=False)
```

### Result
The cleaned dataset has been saved as cleaned_sales_data.csv, and it is ready for exploratory data analysis.