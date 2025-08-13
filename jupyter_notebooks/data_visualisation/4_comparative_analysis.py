"""
Comparative Analysis

This script performs comparative analysis on ETL-processed data. It compares
sales performance across stores and store types, adjusts for inflation using CPI,
and estimates base-level sales excluding promotional and inflation effects.

It also visualizes markdown impact during holiday vs. non-holiday periods.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🔧 Config
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed_data', 'cleaned_sales_data.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'comparative_analysis')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 📥 Load data
def load_data(path):
    try:
        df = pd.read_csv(path, parse_dates=['Date'])
        print(f"✅ Loaded data from '{path}'")
        return df
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        raise

# 📊 Compare sales across stores and departments
def plot_store_department_trends(df, output_dir):
    top_stores = df.groupby('Store')['Weekly_Sales'].sum().nlargest(3).index
    top_departments = df.groupby('Dept')['Weekly_Sales'].sum().nlargest(3).index

    for store_id in top_stores:
        store_df = df[df['Store'] == store_id].groupby('Date')['Weekly_Sales'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=store_df, x='Date', y='Weekly_Sales')
        plt.title(f'Sales Trend Over Time - Store {store_id}')
        plt.xlabel('Date')
        plt.ylabel('Weekly Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        path = os.path.join(output_dir, f'store_{store_id}_trend.png')
        plt.savefig(path)
        plt.close()
        print(f"📊 Saved store trend plot to '{path}'")

    for dept_id in top_departments:
        dept_df = df[df['Dept'] == dept_id].groupby('Date')['Weekly_Sales'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=dept_df, x='Date', y='Weekly_Sales')
        plt.title(f'Sales Trend Over Time - Department {dept_id}')
        plt.xlabel('Date')
        plt.ylabel('Weekly Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        path = os.path.join(output_dir, f'department_{dept_id}_trend.png')
        plt.savefig(path)
        plt.close()
        print(f"📊 Saved department trend plot to '{path}'")

# 💸 Adjust for inflation using CPI
def adjust_for_inflation(df):
    if 'CPI' not in df.columns:
        print("⚠️ CPI column not found. Skipping inflation adjustment.")
        df['Sales_Adjusted'] = df['Weekly_Sales']
        return df

    base_cpi = df['CPI'].median()
    df['Sales_Adjusted'] = df['Weekly_Sales'] * (base_cpi / df['CPI'])
    print("🧮 Adjusted sales for inflation using CPI.")
    return df

# 🧮 Estimate base-level sales excluding markdowns and inflation
def estimate_base_sales(df):
    markdown_cols = [col for col in df.columns if 'markdown' in col.lower()]
    df['Total_Markdown'] = df[markdown_cols].sum(axis=1) if markdown_cols else 0
    df['Base_Sales'] = df['Sales_Adjusted'] - df['Total_Markdown']
    print("📉 Estimated base-level sales excluding markdowns and inflation.")
    return df

# 📊 Visualize markdown impact during holidays vs non-holidays
def plot_markdown_impact(df, output_dir):
    df['Has_Markdown'] = df['Total_Markdown'] > 0
    df['Period'] = df['IsHoliday'].map({True: 'Holiday', False: 'Non-Holiday'})

    impact_df = (
        df.groupby(['Period', 'Has_Markdown'])['Weekly_Sales']
        .mean()
        .reset_index()
        .rename(columns={'Weekly_Sales': 'Avg_Weekly_Sales'})
    )

    impact_df['Markdown Status'] = impact_df['Has_Markdown'].map({True: 'With Markdown', False: 'No Markdown'})

    plt.figure(figsize=(10, 6))
    sns.barplot(data=impact_df, x='Period', y='Avg_Weekly_Sales', hue='Markdown Status', palette='Set2')
    plt.title('Impact of Markdowns on Weekly Sales: Holiday vs Non-Holiday')
    plt.xlabel('Period')
    plt.ylabel('Average Weekly Sales')
    plt.legend(title='Markdown Status')
    plt.tight_layout()

    path = os.path.join(output_dir, 'markdown_impact_by_period.png')
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved markdown impact plot to '{path}'")

# 🚀 Main
def main():
    df = load_data(DATA_PATH)
    df = adjust_for_inflation(df)
    df = estimate_base_sales(df)
    plot_store_department_trends(df, OUTPUT_DIR)
    plot_markdown_impact(df, OUTPUT_DIR)

if __name__ == '__main__':
    main()