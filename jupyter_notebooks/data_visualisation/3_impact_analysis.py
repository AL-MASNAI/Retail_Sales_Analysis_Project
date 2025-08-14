# 3_impact_analysis.py

"""
📊 Impact Analysis

This script visualizes the impact of markdowns on weekly sales by comparing
holiday and non-holiday periods. It helps assess the effectiveness of
promotional activities using processed data from the ETL pipeline.
It generates static plots with Matplotlib and an interactive plot with Plotly.
"""

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# 🔧 Config
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed_data', 'cleaned_sales_data.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'impact_analysis')
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

# 📊 Perform impact analysis
def perform_impact_analysis(df):
    if 'MarkDown1' not in df.columns:
        print("⚠️ 'MarkDown1' column not found. Skipping markdown analysis.")
        df['MarkDown1'] = 0

    impact_df = df.groupby('IsHoliday').agg(
        Average_Weekly_Sales=('Weekly_Sales', 'mean'),
        Average_Markdown=('MarkDown1', 'mean')
    ).reset_index()
    return impact_df

# 📈 Plot sales impact (Matplotlib)
def plot_sales_impact(impact_df, output_dir):
    plt.figure(figsize=(10, 6))
    plt.bar(impact_df['IsHoliday'].astype(str), impact_df['Average_Weekly_Sales'], color=['skyblue', 'salmon'])
    plt.title('Average Weekly Sales: Holiday vs. Non-Holiday (Static)')
    plt.xlabel('Is Holiday Week?')
    plt.ylabel('Average Weekly Sales')
    plt.xticks([0, 1], ['False', 'True'])
    plt.tight_layout()
    path = os.path.join(output_dir, 'sales_by_holiday_impact.png')
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved sales impact plot to '{path}'")

# 📈 Plot markdown impact (Matplotlib)
def plot_markdown_impact(impact_df, output_dir):
    plt.figure(figsize=(10, 6))
    plt.bar(impact_df['IsHoliday'].astype(str), impact_df['Average_Markdown'], color=['lightgreen', 'orange'])
    plt.title('Average Markdown Amount: Holiday vs. Non-Holiday (Static)')
    plt.xlabel('Is Holiday Week?')
    plt.ylabel('Average Markdown')
    plt.xticks([0, 1], ['False', 'True'])
    plt.tight_layout()
    path = os.path.join(output_dir, 'markdown_by_holiday_impact.png')
    plt.savefig(path)
    plt.close()
    print(f"📊 Saved markdown impact plot to '{path}'")

# 📉 NEW: Interactive Markdown Impact Scatter Plot (Plotly)
def plot_interactive_markdown_impact(df, output_dir):
    """
    Creates an interactive scatter plot to visualize markdown impact.
    """
    markdown_cols = [col for col in df.columns if 'markdown' in col.lower()]
    df['Total_Markdown'] = df[markdown_cols].sum(axis=1) if markdown_cols else 0
    
    fig = px.scatter(
        df,
        x='Total_Markdown',
        y='Weekly_Sales',
        color='IsHoliday',
        hover_data=['Store', 'Date'],
        title='Interactive Markdown Impact on Weekly Sales',
        labels={'Total_Markdown': 'Total Markdown Amount', 'Weekly_Sales': 'Weekly Sales', 'IsHoliday': 'Is Holiday Week'}
    )
    fig.write_html(os.path.join(output_dir, 'interactive_markdown_impact.html'))
    print(f"📊 Saved interactive markdown impact plot to '{os.path.join(output_dir, 'interactive_markdown_impact.html')}'")

# 🚀 Main
def main():
    df = load_data(DATA_PATH)
    impact_df = perform_impact_analysis(df)
    plot_sales_impact(impact_df, OUTPUT_DIR)
    plot_markdown_impact(impact_df, OUTPUT_DIR)

    # NEW: Call the Plotly function
    plot_interactive_markdown_impact(df, OUTPUT_DIR)

if __name__ == '__main__':
    main()