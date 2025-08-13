"""
### Trend Analysis

This script visualizes sales trends over time using the cleaned data from the ETL.
It generates plots to show the overall sales trend, a comparative view of sales
for selected stores, and a comparative view of sales for selected departments.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data from the ETL pipeline and convert 'Date' to datetime
df = pd.read_csv('data/cleaned_sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# --- 1. Overall Sales Trend ---
overall_sales_trend = df.groupby('Date')['Weekly_Sales'].sum()

plt.figure(figsize=(15, 6))
plt.plot(overall_sales_trend.index, overall_sales_trend.values)
plt.title('Overall Weekly Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Weekly Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('images/overall_sales_trend.png')
plt.show()
plt.clf()

# --- 2. Selected Stores Sales Trend ---
selected_stores = [1, 2, 3]
plt.figure(figsize=(15, 6))
for store in selected_stores:
    store_df = df[df['Store'] == store]
    store_sales_trend = store_df.groupby('Date')['Weekly_Sales'].sum()
    plt.plot(store_sales_trend.index, store_sales_trend.values, label=f'Store {store}')

plt.title('Weekly Sales Trend for Selected Stores')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/selected_stores_sales_trend.png')
plt.show()
plt.clf()

# --- 3. Selected Departments Sales Trend ---
selected_depts = [1, 2, 3]
plt.figure(figsize=(15, 6))
for dept in selected_depts:
    dept_df = df[df['Dept'] == dept]
    dept_sales_trend = dept_df.groupby('Date')['Weekly_Sales'].sum()
    plt.plot(dept_sales_trend.index, dept_sales_trend.values, label=f'Department {dept}')

plt.title('Weekly Sales Trend for Selected Departments')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('images/selected_departments_sales_trend.png')
plt.show()