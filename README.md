# 📊 Marketing Campaign Analytics Dashboard

## 📌 Project Overview

The **Marketing Campaign Analytics Dashboard** is a data analytics project that analyzes customer demographics, purchasing behavior, and marketing campaign performance. The project uses **Python, SQL, and Streamlit** to generate actionable business insights through data preprocessing, feature engineering, exploratory data analysis (EDA), SQL queries, and an interactive dashboard.

The primary objective is to help marketing teams identify high-value customers, understand purchasing patterns, evaluate campaign effectiveness, and support data-driven decision-making.

---

# 🎯 Objectives

- Clean and preprocess the marketing campaign dataset.
- Perform Exploratory Data Analysis (EDA).
- Create meaningful business features.
- Segment customers using rule-based techniques.
- Store cleaned data in a SQL database.
- Analyze customer behavior using SQL queries.
- Build an interactive Streamlit dashboard.
- Generate business insights and recommendations.

---

# 📂 Dataset

The dataset contains customer information, including:

- Customer Demographics
- Income
- Education
- Marital Status
- Country
- Purchase History
- Product Spending
- Campaign Responses
- Website Visits
- Complaints

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- Streamlit
- VS Code
- Jupyter Notebook

---

# 📋 Project Workflow

```
Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Customer Segmentation
     │
     ▼
SQL Analysis
     │
     ▼
Interactive Dashboard
     │
     ▼
Business Insights
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate records
- Converted Dt_Customer to Date format
- Handled missing values
- Checked data types
- Removed inconsistent values
- Verified dataset quality

---

# ⚙ Feature Engineering

The following business features were created:

### Age

```
Age = Current Year - Year_Birth
```

### Customer Tenure

```
Customer_Tenure = Reference Date - Dt_Customer
```

### Children

```
Children = Kidhome + Teenhome
```

### Total Spend

```
Total_Spend =
MntWines +
MntFruits +
MntMeatProducts +
MntFishProducts +
MntSweetProducts +
MntGoldProds
```

### Total Purchases

```
Total_Purchases =
NumDealsPurchases +
NumWebPurchases +
NumCatalogPurchases +
NumStorePurchases
```

Additional Features:

- Income Band
- Age Group
- High Spender
- High Web Engagement
- Campaign Responder
- Customer Segment

---

# 📊 Exploratory Data Analysis

The project includes:

- Customer Age Distribution
- Income Distribution
- Product Spending Analysis
- Purchase Channel Analysis
- Campaign Response Analysis
- Correlation Heatmap
- Customer Segmentation
- Country-wise Analysis
- Education-wise Analysis
- Marital Status Analysis

---

# 👥 Customer Segmentation

Customers were segmented into:

- High Value
- Loyal
- Active
- Potential
- At Risk
- New
- Regular

Segmentation is based on:

- Income
- Total Spending
- Customer Tenure
- Total Purchases
- Campaign Response
- Recency

---

# 🗄 SQL Analysis

SQLite was used to perform business analysis.

SQL operations include:

- Creating Customer Table
- Loading Cleaned Dataset
- KPI Queries
- Customer Segment Analysis
- Country-wise Analysis
- Product Analysis
- Purchase Channel Analysis
- Campaign Performance
- Top Spending Customers

---

# 📈 Dashboard Features

The Streamlit dashboard includes:

✅ Interactive Filters

- Country
- Education
- Marital Status
- Customer Segment

✅ KPI Cards

- Total Customers
- Average Income
- Average Spending
- Campaign Response Rate

✅ Interactive Tabs

- Products & Channels
- Customer & Campaign Analysis
- Correlation Heatmap

✅ Business Insights

- Highest Spending Product
- Best Purchase Channel
- Best Customer Segment

✅ Download Filtered Dataset

---

# 📌 Key Business Insights

- High-income customers spend significantly more.
- Wine and Meat products contribute the highest revenue.
- Store and Web purchases are the most popular purchase channels.
- Customer segmentation enables personalized marketing strategies.
- Campaign responders show higher average spending.
- Targeting loyal and high-value customers can improve campaign ROI.

---

# 📁 Project Structure

```
Marketing-Campaign-Analytics/
│
├── Marketing_Campaign_Analysis.ipynb
├── guvi2.py
├── marketing_campaign_final.csv
├── marketing_campaign.db
├── README.md
├── requirements.txt
│
└── SQL/
    └── analysis_queries.sql
```

---

# ▶️ How to Run

## Clone Repository

```bash
git clone <repository_link>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
streamlit run guvi2.py
```

---

# 📸 Dashboard Preview

The dashboard provides:

- Interactive Filters
- KPI Cards
- Product Analysis
- Campaign Analysis
- Customer Segmentation
- Correlation Heatmap
- Download Feature

---

# 📌 Future Improvements

- Machine Learning-based Customer Segmentation
- Campaign Response Prediction
- Customer Lifetime Value (CLV) Prediction
- Power BI Integration
- Real-time Database Integration

---

# 👨‍💻 Author

**Monish Sai**

Marketing Campaign Analytics Dashboard

Developed using Python, SQL, Streamlit, Pandas, Matplotlib, and Seaborn.
