import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 🔧 Config
DATA_FILENAME = 'cleaned_sales_data.csv'
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed_data', DATA_FILENAME)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs', 'descriptive_statistics')
os.makedirs(OUTPUT_DIR, exist_ok=True)


# 📥 Load and validate data
def load_data(path):
    """Loads and validates the cleaned sales data."""
    try:
        df = pd.read_csv(path, parse_dates=['Date'])
        if df.empty or 'Weekly_Sales' not in df.columns or 'Store' not in df.columns:
            raise ValueError("Missing required columns or empty dataset.")
        print(f"✅ Loaded data from '{path}'")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise


# 📊 Plot average sales per store type
def plot_average_sales_per_store_type(df, output_dir):
    """
    Creates a bar chart to compare average weekly sales across store types.
    """
    store_type_sales = df.groupby('Type')['Weekly_Sales'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=store_type_sales, x='Type', y='Weekly_Sales', hue='Type', palette='Set2', legend=False)
    plt.title('Average Weekly Sales by Store Type')
    plt.xlabel('Store Type')
    plt.ylabel('Average Weekly Sales')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'average_sales_per_store_type.png'))
    plt.close()
    print("📊 Saved average sales per store type plot.")


# 📊 Plot markdown presence impact on sales
def plot_sales_by_markdown_presence(df, output_dir):
    """
    Creates a bar chart to compare average sales with and without markdown.
    This function has been updated to fix the FutureWarning.
    """
    markdown_cols = [col for col in df.columns if 'markdown' in col.lower()]
    df['Total_Markdown'] = df[markdown_cols].sum(axis=1) if markdown_cols else 0
    
    df['Markdown_Presence'] = df['Total_Markdown'].apply(
        lambda x: 'With Markdown' if x > 0 else 'No Markdown'
    )
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Markdown_Presence', y='Weekly_Sales', hue='Markdown_Presence', palette='coolwarm', legend=False)
    plt.title('Average Weekly Sales: With vs. Without Markdown')
    plt.xlabel('Markdown Presence')
    plt.ylabel('Average Weekly Sales')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'sales_by_markdown_presence.png'))
    plt.close()
    print("📊 Saved sales by markdown presence plot.")


# 🚀 Main execution
def main():
    try:
        df = load_data(DATA_PATH)
        plot_average_sales_per_store_type(df, OUTPUT_DIR)
        plot_sales_by_markdown_presence(df, OUTPUT_DIR)
    except Exception as e:
        print(f"An error occurred during script execution: {e}")


# Call the main function
if __name__ == '__main__':
    main()