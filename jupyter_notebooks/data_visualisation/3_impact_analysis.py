import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🔧 Config
DATA_FILENAME = 'cleaned_sales_data.csv'
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed_data', DATA_FILENAME)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'impact_analysis')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# 📥 Load and validate data
def load_data(path):
    """Loads and validates the cleaned sales data."""
    try:
        df = pd.read_csv(path, parse_dates=['Date'])
        if df.empty or 'Weekly_Sales' not in df.columns:
            raise ValueError("Missing required columns or empty dataset.")
        print(f"✅ Loaded data from '{path}'")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise


# 📊 Perform Impact Analysis
def perform_impact_analysis(df):
    """
    Prepares data for impact analysis plots.
    """
    impact_df = df.copy()
    impact_df['Holiday_Flag'] = impact_df['IsHoliday'].apply(
        lambda x: 'Holiday Week' if x == True else 'Non-Holiday Week'
    )
    
    # Calculate a 'Total_Markdown' column
    markdown_cols = [col for col in impact_df.columns if 'markdown' in col.lower()]
    impact_df['Total_Markdown'] = impact_df[markdown_cols].sum(axis=1) if markdown_cols else 0
    
    return impact_df


# 📈 Plot sales impact by holiday
def plot_sales_impact(df, output_dir):
    """
    Creates a bar chart to compare average sales on holiday vs. non-holiday weeks.
    """
    plt.figure(figsize=(10, 6))
    # This line has been updated to fix the FutureWarning
    sns.barplot(data=df, x='Holiday_Flag', y='Weekly_Sales', hue='Holiday_Flag', palette='viridis', errorbar=None, legend=False)
    plt.title('Average Weekly Sales: Holiday vs. Non-Holiday')
    plt.xlabel('Week Type')
    plt.ylabel('Average Weekly Sales')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_by_holiday_impact.png'))
    plt.close()
    print("📊 Saved sales impact by holiday plot.")


# 📉 Plot markdown impact on sales
def plot_markdown_impact(df, output_dir):
    """
    Creates a scatter plot to visualize the relationship between markdown and sales.
    """
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data=df, x='Total_Markdown', y='Weekly_Sales', hue='Holiday_Flag', alpha=0.6)
    plt.title('Markdown Impact on Weekly Sales')
    plt.xlabel('Total Markdown')
    plt.ylabel('Weekly Sales')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'markdown_by_holiday_impact.png'))
    plt.close()
    print("📊 Saved markdown impact on sales plot.")


# 🚀 Main
def main():
    try:
        df = load_data(DATA_PATH)
        impact_df = perform_impact_analysis(df)
        plot_sales_impact(impact_df, OUTPUT_DIR)
        plot_markdown_impact(impact_df, OUTPUT_DIR)
    except Exception as e:
        print(f"An error occurred during script execution: {e}")


# Call the main function
if __name__ == '__main__':
    main()