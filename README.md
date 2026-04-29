# 📊 E-commerce Customer & Revenue Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

---

## 📌 Overview

This project analyzes customer purchasing behavior and revenue trends to identify key business insights. It includes an interactive dashboard built using Streamlit for real-time data exploration.

---

## 🎯 Business Problem

Businesses need to understand:

- Who their top customers are
- Which cities generate the most revenue
- How revenue trends change over time

This project solves these questions using data analysis and visualization.

---

## 🔍 Solution Approach

- Data cleaning and analysis using **Pandas**
- SQL-based aggregation for business queries
- Data merging and transformation
- Visualization using **Matplotlib**
- Interactive dashboard using **Streamlit**

---

## 📊 Business Impact

This analysis helps businesses:

- Identify high-value customers
- Focus on top-performing regions
- Track revenue growth patterns
- Make data-driven decisions for marketing and sales

---

## 🛠️ Tech Stack

- Python (Pandas)
- SQL
- Matplotlib
- Streamlit
- VS Code / Jupyter Notebook

---

## 📂 Dataset

Custom dataset containing:

- **Orders** → order_id, customer_id, order_date, amount
- **Customers** → customer_id, name, city

---

## 📁 Project Structure

- `Data/` → dataset files
- `images/` → dashboard screenshots
- `app.py` → Streamlit dashboard
- `requirements.txt` → dependencies
- `README.md` → project documentation

---

## 📊 Key Analysis Performed

- Total orders, customers, and revenue calculation
- Customer-wise spending analysis
- City-wise revenue distribution (JOIN operations)
- Monthly revenue trend analysis
- KPI metrics and dashboard visualization

---

## 📈 Dashboard Features

- KPI cards (Total Orders, Revenue, Top Customer, Avg Order Value)
- City-based filtering
- Customer-based filtering
- Revenue by City (Bar Chart)
- Monthly Revenue Trend (Line Chart)
- Business insights section

---

## 💡 Key Insights

- Top customer contributes ~32% of total revenue, indicating high dependency on a few users
- Delhi generates the highest revenue, making it a key market for business growth
- Revenue trend shows consistent increase, with peak performance in March
- Revenue distribution suggests uneven customer contribution (potential segmentation opportunity)

---

## 📸 Dashboard Preview

The dashboard enables interactive filtering and real-time analysis of customer and revenue data.

### Full Dashboard

![Dashboard](images/dashboard.png)

### Revenue by City

![City Revenue](images/city_chart.png)

### Monthly Trend

![Monthly Trend](images/trend_chart.png)

---

## 🚀 Live Dashboard

👉 [Click here to view the live dashboard](https://ecommerce-analysis-mudit.streamlit.app/)

---

## 🎯 Outcome

This project demonstrates:

- End-to-end data analysis workflow
- SQL + Python integration
- Business insight generation
- Dashboard development using Streamlit

---

## 📌 Future Improvements

- Add more filters (date range, segments)
- Integrate larger real-world dataset
- Apply advanced analytics (cohort analysis, segmentation)

---

## ▶️ How to Run the Project

1. Clone the repository:
   git clone https://github.com/muditkumar14/ecommerce-analysis

2. Navigate to the project folder:
   cd ecommerce-analysis

3. Install dependencies:
   pip install -r requirements.txt

4. Run the Streamlit app:
   streamlit run app.py

---

## 👨‍💻 Author

**Mudit Kumar Singh**

---

> This project reflects the ability to transform raw data into actionable business insights using modern data tools.
