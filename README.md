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
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.
