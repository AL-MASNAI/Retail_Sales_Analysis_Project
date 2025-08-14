# 2_trend_analysis.py

"""
📊 Trend Analysis

This script analyzes weekly sales patterns from the cleaned dataset.
It visualizes:

- Overall weekly sales trends across all stores
- Individual store-level sales trends over time

The script generates static plots using Matplotlib/Seaborn and an interactive
plot using Plotly to help identify seasonality, promotional impacts, and long-term shifts.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# 🔧 Config
DATA_FILENAME = 'cleaned_sales_data.csv'
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed_data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'trend_analysis')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 📥 Load and validate data
def load_data(path):
    try:
        df = pd.read_csv(path, parse_dates=['Date'])
        if df.empty or 'Weekly_Sales' not in df.columns or 'Store' not in df.columns:
            raise ValueError("Missing required columns or empty dataset.")
        print(f"✅ Loaded data from '{path}'")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise

# 📈 Plot overall weekly sales trend (Matplotlib)
def plot_overall_trend(df, output_dir):
    weekly = df.groupby('Date')['Weekly_Sales'].sum().reset_index().sort_values('Date')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=weekly, x='Date', y='Weekly_Sales', marker='o')
    plt.title('Overall Weekly Sales Trend (Static)')
    plt.xlabel('Date')
    plt.ylabel('Total Weekly Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    path = os.path.join(output_dir, 'overall_weekly_sales_trend.png')
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved overall trend plot to '{path}'")

# 📈 Plot store-level weekly sales trend (Matplotlib)
def plot_store_trend(df, store_id, output_dir):
    store_df = df[df['Store'] == store_id].groupby('Date')['Weekly_Sales'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=store_df, x='Date', y='Weekly_Sales', marker='o')
    plt.title(f'Weekly Sales Trend - Store {store_id} (Static)')
    plt.xlabel('Date')
    plt.ylabel('Weekly Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    filename = f'store_{store_id}_sales_trend.png'
    path = os.path.join(output_dir, filename)
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved Store {store_id} trend plot to '{path}'")

# 📈 NEW: Interactive Sales Trend Plot (Plotly)
def plot_interactive_sales_trend(df, output_dir):
    """
    Creates an interactive line chart of overall weekly sales trend.
    """
    weekly_sales = df.groupby('Date')['Weekly_Sales'].sum().reset_index()
    fig = px.line(
        weekly_sales,
        x='Date',
        y='Weekly_Sales',
        title='Interactive Overall Weekly Sales Trend',
        labels={'Weekly_Sales': 'Total Weekly Sales'}
    )
    fig.write_html(os.path.join(output_dir, 'interactive_sales_trend.html'))
    print(f"📊 Saved interactive sales trend to '{os.path.join(output_dir, 'interactive_sales_trend.html')}'")

# 🚀 Main execution
def main():
    data_path = os.path.join(DATA_DIR, DATA_FILENAME)
    df = load_data(data_path)

    plot_overall_trend(df, OUTPUT_DIR)
    
    top_stores = df.groupby('Store')['Weekly_Sales'].sum().nlargest(3).index
    for store_id in top_stores:
        plot_store_trend(df, store_id, OUTPUT_DIR)
    
    # NEW: Call the Plotly function for an interactive plot
    plot_interactive_sales_trend(df, OUTPUT_DIR)

if __name__ == '__main__':
    main()