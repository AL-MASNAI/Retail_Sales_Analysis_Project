# 4_comparative_analysis.py

"""
📊 Comparative Analysis

This script performs comparative analysis on ETL-processed data. It compares
sales performance across stores and store types, adjusts for inflation using CPI,
and estimates base-level sales. It uses Matplotlib, Seaborn, and Plotly
to create static and interactive visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
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

# 📊 Compare sales across stores and departments (Matplotlib/Seaborn)
def plot_store_department_trends(df, output_dir):
    top_stores = df.groupby('Store')['Weekly_Sales'].sum().nlargest(3).index
    top_departments = df.groupby('Dept')['Weekly_Sales'].sum().nlargest(3).index

    for store_id in top_stores:
        store_df = df[df['Store'] == store_id].groupby('Date')['Weekly_Sales'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=store_df, x='Date', y='Weekly_Sales')
        plt.title(f'Sales Trend Over Time - Store {store_id} (Static)')
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
        plt.title(f'Sales Trend Over Time - Department {dept_id} (Static)')
        plt.xlabel('Date')
        plt.ylabel('Weekly Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        path = os.path.join(output_dir, f'department_{dept_id}_trend.png')
        plt.savefig(path)
        plt.close()
        print(f"📊 Saved department trend plot to '{path}'")

# 📊 Visualize markdown impact during holidays vs non-holidays (Matplotlib/Seaborn)
def plot_markdown_impact(df, output_dir):
    markdown_cols = [col for col in df.columns if 'markdown' in col.lower()]
    df['Total_Markdown'] = df[markdown_cols].sum(axis=1) if markdown_cols else 0
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
    plt.title('Impact of Markdowns on Weekly Sales (Static)')
    plt.xlabel('Period')
    plt.ylabel('Average Weekly Sales')
    plt.legend(title='Markdown Status')
    plt.tight_layout()

    path = os.path.join(output_dir, 'markdown_impact_by_period.png')
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved markdown impact plot to '{path}'")

# 📊 NEW: Interactive Sales Comparison by Store Type (Plotly)
def plot_interactive_store_comparison(df, output_dir):
    """
    Creates an interactive bar chart to compare average sales by store type.
    """
    store_type_sales = df.groupby('Type')['Weekly_Sales'].mean().reset_index()
    fig = px.bar(
        store_type_sales,
        x='Type',
        y='Weekly_Sales',
        title='Interactive Average Weekly Sales by Store Type',
        labels={'Weekly_Sales': 'Average Weekly Sales', 'Type': 'Store Type'},
        color='Type',
        text=store_type_sales['Weekly_Sales'].round(2)
    )
    fig.write_html(os.path.join(output_dir, 'interactive_sales_by_store_type.html'))
    print(f"📊 Saved interactive store type comparison to '{os.path.join(output_dir, 'interactive_sales_by_store_type.html')}'")

# 🚀 Main
def main():
    df = load_data(DATA_PATH)
    plot_store_department_trends(df, OUTPUT_DIR)
    plot_markdown_impact(df, OUTPUT_DIR)
    
    # NEW: Call the Plotly function
    plot_interactive_store_comparison(df, OUTPUT_DIR)

if __name__ == '__main__':
    main()