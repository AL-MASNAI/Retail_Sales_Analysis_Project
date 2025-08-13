"""
📊 Descriptive Statistics Analysis

Calculates average weekly sales per store and department from cleaned ETL output.
"""

import pandas as pd
import os

# 📂 Define correct relative path to cleaned data
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed_data', 'cleaned_sales_data.csv')

# 🧼 Load the cleaned dataset with error handling
try:
    df = pd.read_csv(data_path)
    print(f"✅ Loaded data from '{data_path}'\n")
except FileNotFoundError:
    print(f"❌ File not found: '{data_path}'")
    raise

# 📊 Calculate average weekly sales per store
average_sales_per_store = (
    df.groupby('Store')['Weekly_Sales']
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# 📊 Calculate average weekly sales per department
average_sales_per_dept = (
    df.groupby('Dept')['Weekly_Sales']
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# 📋 Display results
print("### 🏬 Average Weekly Sales per Store")
print(average_sales_per_store.to_string())

print("\n### 🗂️ Average Weekly Sales per Department")
print(average_sales_per_dept.to_string())

# 💾 Optional: Save summary stats
summary_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'summary_stats')
os.makedirs(summary_dir, exist_ok=True)

average_sales_per_store.to_csv(os.path.join(summary_dir, 'avg_sales_per_store.csv'))
average_sales_per_dept.to_csv(os.path.join(summary_dir, 'avg_sales_per_dept.csv'))

print(f"\n📁 Summary statistics saved to '{summary_dir}'")