# Retail Sales Data Analysis Project


# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The analysis is based on a retail sales dataset provided by a Kaggle. The dataset is comprised of three key files: Sales.csv, Features.csv, and Stores.csv. These files contain transactional data, external factors such as holidays and markdown promotions, and store-specific details, respectively. The dataset is of a manageable size, allowing for efficient processing without exceeding typical repository size limits.


## Business Requirements
* The business requirements for this project are to provide actionable insights for a retail company. The key requirements are to:

1. Identify Sales Trends: Understand weekly, monthly, and seasonal sales patterns.

2. Assess Promotional Impact: Quantify the effect of holiday weeks and markdown promotions on sales performance.

3. Compare Store Performance: Benchmark the performance of different store types (A, B, C) and individual stores against each other.


## Hypothesis and how to validate?
* Hypothesis 1: Holiday weeks have a significant positive impact on weekly sales.
    - Validation: I will validate this by comparing the average weekly sales during holiday weeks (e.g., Thanksgiving, Christmas) to the average weekly sales during non-holiday weeks. Visualizations will show sales spikes during these periods.
* Hypothesis 2: Store type is a major predictor of sales performance, with larger store types (e.g., Type A) outperforming smaller ones.
   - Validation: I will validate this by calculating and visualizing the average weekly sales for each store type. A comparative analysis will show a clear hierarchy in sales performance based on store type.

* Hypothesis 3: Markdown promotions are correlated with an increase in sales.
   - Validation: I will validate this by plotting markdown values against weekly sales. The visualization will highlight a relationship between markdown events and a corresponding increase in sales, especially during holiday periods.



## Project Plan
* Outline the high-level steps taken for the analysis.
The analysis followed a structured pipeline based on the Extract, Transform, Load (ETL) process detailed in the ETL_Pipeline.ipynb notebook.

1. Extract: Raw data from three CSV files (Features.csv, Sales.csv, Stores.csv) was loaded into pandas DataFrames.

2. Transform: The data was cleaned, merged, and enhanced with new features.

3. Validate: Data quality checks were performed to ensure integrity after transformation.

4. Load: The final, cleaned dataset was saved as a single CSV file.

5. Analyze: The cleaned data will be used for in-depth visualization and analysis.


* How was the data managed throughout the collection, processing, analysis and interpretation steps?
Data was managed by separating raw and processed data. The original CSV files were left untouched in the data folder. A Jupyter Notebook (ETL_Pipeline.ipynb) was used for the entire data cleaning and processing workflow. The final cleaned dataset, cleaned_sales_data.csv, was saved as the output of this process. This approach ensures the raw data remains separate and the transformation steps are fully documented and reproducible.


* Why did you choose the research methodologies you used?
I chose a quantitative research methodology focused on descriptive and comparative analysis. This approach was ideal for this project because the business requirements were to understand and compare existing patterns and trends in the sales data. Using a pipeline of ETL followed by visualization allowed for a systematic and reproducible way to answer the business questions.


## The rationale to map the business requirements to the Data Visualisations
Requirement: Identify Sales Trends.

Rationale: To identify trends, I will use line plots. A plot of overall_sales_trend.png will show the sales patterns over time, revealing seasonality and peaks. Additional plots like selected_stores_sales_trend.png and selected_departments_sales_trend.png will allow for granular trend analysis and comparison.

Requirement: Assess Promotional Impact.

Rationale: To assess the impact of promotions, a comparative bar chart and a scatter plot will be used. A bar chart sales_by_holiday_impact.png will effectively contrast sales during holiday and non-holiday weeks. A scatter plot markdown_by_holiday_impact.png will visualize the relationship between markdown values and sales, helping to identify a correlation.

Requirement: Compare Store Performance.

Rationale: To compare performance, I will use bar charts. average_sales_per_store.png and average_sales_per_store_type.png will provide a clear visual comparison of average sales across different individual stores and store types, making it easy for stakeholders to see which stores are top performers.

## Analysis techniques used
* Methods and Justification
The analysis relies on descriptive statistics and time series analysis.

Descriptive Statistics: I will calculate and analyze measures like mean, median, and standard deviation for sales data. This is used to understand the central tendency and spread of sales across different stores and departments.

Time Series Analysis: I will use line plots to visualize sales data over time, which is a fundamental technique for identifying trends, seasonality, and cycles.


* How I Structured the Data Analysis
The analysis is structured into four distinct, logical Python scripts (1_descriptive_statistics.py, 2_trend_analysis.py, etc.). This modular approach ensures that each script focuses on a single aspect of the business requirements. For example, 2_trend_analysis.py is solely responsible for generating all the trend-related plots, which makes the code easier to read, maintain, and debug.

* Limitations and Challenges
A limitation was the lack of more advanced forecasting techniques. The project focuses on historical analysis rather than predictive modeling. An alternative approach would have been to use models like ARIMA or Prophet to forecast future sales based on the historical data and holiday effects.

* Use of Generative AI Tools
Generative AI, specifically ChatGPT, was used to assist in several key areas:

Ideation: I used it to brainstorm different visualization types that could best represent the data.

Design Thinking: It helped me structure the README.md and organize the project workflow in a logical manner.

Code Optimization: I used it to refine and optimize Python scripts for data cleaning and plotting, such as finding more efficient ways to merge dataframes or customize matplotlib plots.

## Ethical considerations
There were no significant data privacy or bias issues with this dataset. The data is anonymized, containing no personal customer information. It focuses solely on transactional and store-level data. The dataset is a sanitized and public-facing record from a competition, so there were no legal or societal issues to overcome.

## Dashboard Design
Dashboard Pages and Content: The project did not include a live dashboard, but the analysis served as the foundation for a potential dashboard. Each script was designed to generate a single visual output that would serve as a widget on a dashboard page.

Page 1: Sales Trends: Contains overall_sales_trend.png and selected_stores_sales_trend.png.

Page 2: Impact Analysis: Contains sales_by_holiday_impact.png and markdown_by_holiday_impact.png.

Page 3: Comparative Analysis: Contains average_sales_per_store.png and average_sales_per_store_type.png.

Communicating Insights:

Technical Audience: The detailed code and comments within the Jupyter Notebook (ETL_Pipeline.ipynb) and Python scripts (1_descriptive_statistics.py, etc.) are tailored for a technical audience.

Non-technical Audience: The generated images and the Key Findings section of this README.md were designed for a non-technical audience. The visualizations are clear and the accompanying text explains the findings in plain, business-oriented language.


## Unfixed Bugs
No critical bugs were encountered during the analysis phase. The scripts run as intended and produce the expected outputs. One minor shortcoming of the Matplotlib library is that the plots are not interactive, which could be a useful feature for a dashboard. However, this was not a priority for this project's scope. I addressed this by acknowledging it as a limitation and noting that a library like Plotly would be a better choice for interactive visualizations in future iterations.


## Development Roadmap
Challenges and Strategies: A key challenge was efficiently merging the three large datasets while handling the different data types and missing values. The strategy to overcome this was to use the powerful data manipulation capabilities of the pandas library, specifically the merge() and fillna() methods, and to carefully inspect the dataframes at each step.

Future Skills: Based on this experience, I plan to learn Plotly for creating interactive and dynamic visualizations. I also want to explore predictive modeling and machine learning with libraries like Scikit-learn to build a sales forecasting model.

## Deployment
### Heroku

This project is not a web application and does not require deployment to Heroku. However, if it were to be deployed as a dashboard, the process would follow these steps:

1. Log in to Heroku and create an App.

2. Select GitHub as the deployment method.

3. Connect the repository.

4. Set the runtime.txt Python version to a supported version for the Heroku stack.

Deploy the chosen branch.

5. If the slug size is too large, add large files not required for the app to the .slugignore file.



## Main Data Analysis Libraries
pandas: Used for all data manipulation, cleaning, and transformation tasks.

Example: Merging the datasets df_sales = pd.merge(df_sales, df_features, on=['Store', 'Date', 'IsHoliday'], how='left').

matplotlib: Used for creating static visualizations.

Example: Generating a line plot plt.plot(sales_by_week['Date'], sales_by_week['Weekly_Sales']).

jupyter: The environment used to run the ETL pipeline and write the initial analysis code.

## Credits 
### Content 
The project does not include any external media files, as all images were generated directly from the analysis scripts.

The retail sales dataset was sourced from a Kaggle competition: Retail Sales Data Analysis.

Instructions on how to structure a project README.md were adapted from the Code Institute template.

### Media
The project does not include any external media files, as all images were generated directly from the analysis scripts.

## Acknowledgements (optional)
I would like to thank my peers for their valuable feedback during the development process and my instructors and coaches for guidance on best practices in data analysis.