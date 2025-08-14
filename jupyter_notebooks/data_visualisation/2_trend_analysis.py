# 📈 Plot Overall Weekly Sales Trend
def plot_overall_trend(df, output_dir):
    """
    Plots the overall weekly sales trend.
    """
    plt.figure(figsize=(15, 7))
    sns.lineplot(data=df, x='Date', y='Weekly_Sales')
    plt.title('Overall Weekly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Weekly Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'overall_weekly_sales_trend.png'))
    plt.close()
    print("📊 Saved overall weekly sales trend plot.")


# 📈 Plot Weekly Sales Trend for a specific store
def plot_store_trend(df, store_id, output_dir):
    """
    Plots the weekly sales trend for a specific store.
    """
    store_df = df[df['Store'] == store_id]
    plt.figure(figsize=(15, 7))
    sns.lineplot(data=store_df, x='Date', y='Weekly_Sales')
    plt.title(f'Weekly Sales Trend for Store {store_id}')
    plt.xlabel('Date')
    plt.ylabel('Weekly Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'store_{store_id}_sales_trend.png'))
    plt.close()
    print(f"📊 Saved weekly sales trend for Store {store_id}.")