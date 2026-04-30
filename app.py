import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="E-commerce Dashboard", layout="wide")

# ---------------- LOAD DATA ----------------
# Use relative paths (important for GitHub + deployment)
orders = pd.read_csv('Data/orders.csv')
customers = pd.read_csv('Data/customers.csv')

# Merge datasets
merged = pd.merge(orders, customers, on='customer_id')

# Convert date
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['month'] = orders['order_date'].dt.to_period('M')

# ---------------- TITLE ----------------
st.title("📊 E-commerce Analytics Dashboard")
st.markdown("### Insights on Customer Behavior & Revenue Trends")

# ---------------- FILTER ----------------
st.sidebar.header("Filter")

city_filter = st.sidebar.selectbox(
    "Select City",
    ["All"] + sorted(merged['city'].unique())
)

# Apply filter
if city_filter != "All":
    filtered_data = merged[merged['city'] == city_filter]
else:
    filtered_data = merged
customer_filter = st.sidebar.selectbox(
    "Select Customer",
    ["All"] + list(merged['customer_id'].unique())
)

# Apply customer filter
if customer_filter != "All":
    filtered_data = filtered_data[filtered_data['customer_id'] == customer_filter]

# Safety check
if filtered_data.empty:
    st.warning("No data available for selected filter")
    st.stop()

# ---------------- KPI SECTION ----------------
col1, col2, col3, col4 = st.columns(4)

total_orders = filtered_data.shape[0]
total_revenue = filtered_data['amount'].sum()

avg_order = total_revenue / total_orders
st.metric("Avg Order Value", f"₹ {avg_order:.2f}")
customer_spend = filtered_data.groupby('customer_id')['amount'].sum()
top_customer = customer_spend.idxmax()
top_amount = customer_spend.max()

col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹ {total_revenue:,}")
col3.metric("Top Customer", f"{top_customer} (₹ {top_amount:,})")

# ---------------- CHART: REVENUE BY CITY ----------------
st.subheader("Revenue by City")

city_revenue = filtered_data.groupby('city')['amount'].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
city_revenue.plot(kind='bar', ax=ax1)
ax1.set_xlabel("City")
ax1.set_ylabel("Revenue")

# Add values on bars
for i, v in enumerate(city_revenue):
    ax1.text(i, v, f"{v}", ha='center', va='bottom')

st.pyplot(fig1)

# ---------------- CHART: MONTHLY TREND ----------------
st.subheader("Monthly Revenue Trend")

filtered_orders = orders[orders['customer_id'].isin(filtered_data['customer_id'])]

monthly_revenue = (
    filtered_orders.groupby('month')['amount']
    .sum()
    .sort_index()
)

monthly_revenue.index = monthly_revenue.index.astype(str)

fig2, ax2 = plt.subplots()
monthly_revenue.plot(kind='line', marker='o', ax=ax2)
ax2.set_xlabel("Month")
ax2.set_ylabel("Revenue")

st.pyplot(fig2)

# ---------------- INSIGHTS ----------------
st.markdown("### 🔍 Key Insights")

st.write("• Customer 101 contributes the highest revenue.")
st.write("• Delhi is the top-performing city.")
st.write("• Revenue shows growth trend with peak in March.")

if total_revenue > 10000:
    st.success("Revenue is performing strongly 📈")
else:
    st.warning("Revenue needs improvement 📉")
# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("Built using Python, Pandas, SQL & Streamlit")