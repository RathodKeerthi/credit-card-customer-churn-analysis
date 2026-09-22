import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------
st.set_page_config(
    page_title="Credit Card Customer Churn Analysis",
    page_icon="💳",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("credit_card_customer_churn_cleaned.csv")


df = load_data()

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("💳 Credit Card Customer Churn Analysis")
st.markdown(
    "### Customer behavior, attrition patterns and retention insights"
)

st.divider()

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
total_customers = len(df)

existing_customers = (
    df["Attrition_Flag"] == "Existing Customer"
).sum()

attrited_customers = (
    df["Attrition_Flag"] == "Attrited Customer"
).sum()

attrition_rate = (attrited_customers / total_customers) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Existing Customers", f"{existing_customers:,}")
col3.metric("Attrited Customers", f"{attrited_customers:,}")
col4.metric("Attrition Rate", f"{attrition_rate:.2f}%")

st.divider()

# ---------------------------------------------------
# CUSTOMER STATUS
# ---------------------------------------------------
st.subheader("1. Customer Status")

status_data = (
    df["Attrition_Flag"]
    .value_counts()
    .reset_index()
)

status_data.columns = ["Customer Status", "Customers"]

fig_status = px.bar(
    status_data,
    x="Customer Status",
    y="Customers",
    text="Customers",
    title="Existing vs Attrited Customers"
)

fig_status.update_traces(textposition="outside")

fig_status.update_layout(
    xaxis_title="Customer Status",
    yaxis_title="Number of Customers",
    showlegend=False
)

st.plotly_chart(fig_status, use_container_width=True)

# ---------------------------------------------------
# TRANSACTION BEHAVIOR
# ---------------------------------------------------
st.subheader("2. Customer Transaction Behavior")

col1, col2 = st.columns(2)

# Average transaction count
transaction_count = (
    df.groupby("Attrition_Flag")["Total_Trans_Ct"]
    .mean()
    .reset_index()
)

transaction_count.columns = [
    "Customer Status",
    "Average Transaction Count"
]

fig_count = px.bar(
    transaction_count,
    x="Customer Status",
    y="Average Transaction Count",
    text="Average Transaction Count",
    title="Average Transaction Count"
)

fig_count.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_count.update_layout(
    xaxis_title="Customer Status",
    yaxis_title="Average Transactions",
    showlegend=False
)

col1.plotly_chart(fig_count, use_container_width=True)


# Average transaction amount
transaction_amount = (
    df.groupby("Attrition_Flag")["Total_Trans_Amt"]
    .mean()
    .reset_index()
)

transaction_amount.columns = [
    "Customer Status",
    "Average Transaction Amount"
]

fig_amount = px.bar(
    transaction_amount,
    x="Customer Status",
    y="Average Transaction Amount",
    text="Average Transaction Amount",
    title="Average Transaction Amount"
)

fig_amount.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_amount.update_layout(
    xaxis_title="Customer Status",
    yaxis_title="Average Transaction Amount",
    showlegend=False
)

col2.plotly_chart(fig_amount, use_container_width=True)

# ---------------------------------------------------
# CREDIT UTILIZATION
# ---------------------------------------------------
st.subheader("3. Average Credit Utilization")

utilization = (
    df.groupby("Attrition_Flag")["Avg_Utilization_Ratio"]
    .mean()
    .reset_index()
)

utilization.columns = [
    "Customer Status",
    "Average Credit Utilization"
]

fig_utilization = px.bar(
    utilization,
    x="Customer Status",
    y="Average Credit Utilization",
    text="Average Credit Utilization",
    title="Average Credit Utilization by Customer Status"
)

fig_utilization.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig_utilization.update_layout(
    xaxis_title="Customer Status",
    yaxis_title="Average Utilization Ratio",
    showlegend=False
)

st.plotly_chart(fig_utilization, use_container_width=True)

# ---------------------------------------------------
# MONTHS INACTIVE
# ---------------------------------------------------
st.subheader("4. Inactivity and Customer Attrition")

inactive_data = pd.crosstab(
    df["Months_Inactive_12_mon"],
    df["Attrition_Flag"],
    normalize="index"
).reset_index()

if "Attrited Customer" in inactive_data.columns:
    inactive_data["Attrition Rate (%)"] = (
        inactive_data["Attrited Customer"] * 100
    )

fig_inactive = px.bar(
    inactive_data,
    x="Months_Inactive_12_mon",
    y="Attrition Rate (%)",
    text="Attrition Rate (%)",
    title="Attrition Rate by Months Inactive"
)

fig_inactive.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_inactive.update_layout(
    xaxis_title="Months Inactive",
    yaxis_title="Attrition Rate (%)"
)

st.plotly_chart(fig_inactive, use_container_width=True)

# ---------------------------------------------------
# CONTACTS COUNT
# ---------------------------------------------------
st.subheader("5. Customer Contacts and Attrition")

contact_data = pd.crosstab(
    df["Contacts_Count_12_mon"],
    df["Attrition_Flag"],
    normalize="index"
).reset_index()

if "Attrited Customer" in contact_data.columns:
    contact_data["Attrition Rate (%)"] = (
        contact_data["Attrited Customer"] * 100
    )

fig_contacts = px.bar(
    contact_data,
    x="Contacts_Count_12_mon",
    y="Attrition Rate (%)",
    text="Attrition Rate (%)",
    title="Attrition Rate by Number of Contacts"
)

fig_contacts.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_contacts.update_layout(
    xaxis_title="Contacts in Last 12 Months",
    yaxis_title="Attrition Rate (%)"
)

st.plotly_chart(fig_contacts, use_container_width=True)

# ---------------------------------------------------
# INCOME CATEGORY FILTER
# ---------------------------------------------------
st.subheader("6. Customer Filter by Income Category")

income_options = ["All"] + sorted(
    df["Income_Category"].dropna().unique().tolist()
)

selected_income = st.selectbox(
    "Select Income Category",
    income_options
)

if selected_income == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Income_Category"] == selected_income
    ]

st.write(
    f"**Customers in selected category: {len(filtered_df):,}**"
)

filtered_status = (
    filtered_df["Attrition_Flag"]
    .value_counts()
    .reset_index()
)

filtered_status.columns = [
    "Customer Status",
    "Customers"
]

fig_filtered = px.bar(
    filtered_status,
    x="Customer Status",
    y="Customers",
    text="Customers",
    title=f"Customer Status — {selected_income}"
)

fig_filtered.update_traces(
    textposition="outside"
)

fig_filtered.update_layout(
    xaxis_title="Customer Status",
    yaxis_title="Number of Customers",
    showlegend=False
)

st.plotly_chart(
    fig_filtered,
    use_container_width=True
)

# ---------------------------------------------------
# KEY INSIGHTS
# ---------------------------------------------------
st.subheader("7. Key Insights")

st.markdown("""
- **Overall attrition rate:** 16.07% of customers are classified as attrited.
- **Transaction behavior:** Existing customers have a higher average transaction count than attrited customers.
- **Transaction amount:** Existing customers also show a higher average transaction amount.
- **Credit utilization:** Average credit utilization differs between existing and attrited customers.
- **Inactivity:** Attrition rates vary across different levels of customer inactivity.
- **Customer contacts:** Attrition rates also vary with the number of contacts recorded in the previous 12 months.
""")

st.divider()

st.caption(
    "Credit Card Customer Churn Analysis | Data Analytics Project"
)