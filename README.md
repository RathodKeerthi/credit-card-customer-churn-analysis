# Credit Card Customer Churn Analysis

## Project Overview

This project analyzes credit card customer data to understand customer attrition and identify patterns related to customer behavior. The analysis compares existing customers with attrited customers using transaction activity, credit utilization, inactivity, customer contacts, demographic information and other account-related details.

The project also includes an interactive Streamlit dashboard to present the main findings in an easy-to-understand way.

## Dataset

The dataset used in this project is the Credit Card Customers dataset available on Kaggle.

Dataset Link:
https://www.kaggle.com/sakshigoyal7/credit-card-customers/activity

The dataset contains 10,127 customer records and 23 original columns. After data preparation, two Naive Bayes classifier-related columns were removed, resulting in a cleaned dataset with 21 columns.

## Project Description

The project follows these main steps:

1. Load and understand the customer dataset.
2. Check the dataset structure, missing values and duplicate records.
3. Remove unnecessary Naive Bayes classifier-related columns.
4. Compare existing and attrited customers.
5. Analyze transaction count and transaction amount.
6. Analyze credit utilization.
7. Study months of inactivity and customer contacts.
8. Explore income and demographic information.
9. Create visualizations to understand the observed patterns.
10. Build an interactive Streamlit dashboard to present the results.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Plotly
- Streamlit
- Google Colab
- Visual Studio Code
- Jupyter Notebook

## Project Files

- `Credit_Card_Customer_Churn_Analysis.ipynb` – Jupyter Notebook containing the data cleaning and analysis.
- `app.py` – Streamlit dashboard application.
- `credit_card_customer_churn_cleaned.csv` – Cleaned dataset used for the project.
- `requirements.txt` – Python libraries required to run the project.

## Setup and Run Instructions

### 1. Install Python

Make sure Python is installed on your system.

### 2. Open the project folder

Open the project folder in Visual Studio Code.

### 3. Install the required libraries

Open the terminal in the project folder and run:

```bash
pip install -r requirements.txt

`````
## **Key Information**

- Total customers analyzed: 10,127
- Existing customers: 8,500
- Attrited customers: 1,627
- Overall observed attrition rate: 16.07%
- Existing customers showed higher average transaction count and transaction amount than attrited customers.
- Average credit utilization differed between existing and attrited customers.
- Attrition rates varied across different inactivity levels and customer contact counts.
- An interactive Streamlit dashboard was created to present the analysis and insights.

## **Conclusion**

This project analyzes credit card customer data to understand customer behavior and attrition patterns.
