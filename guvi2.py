import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Marketing Campaign Dashboard",
    layout="wide"
)

df = pd.read_csv("marketing_campaign_final.csv")

st.title("📊 Marketing Campaign Analytics Dashboard")
st.markdown(
    "Interactive dashboard for customer segmentation, campaign analysis, and marketing insights."
)
st.markdown("---")



# ==========================
# FILTERS & KPI CARDS
# ==========================

st.sidebar.header("Dashboard Filters")

country = st.sidebar.multiselect(
    "Country",
    df["Country"].unique(),
    default=df["Country"].unique()
)

education = st.sidebar.multiselect(
    "Education",
    df["Education"].unique(),
    default=df["Education"].unique()
)

segment = st.sidebar.multiselect(
    "Customer Segment",
    df["Customer_Segment"].unique(),
    default=df["Customer_Segment"].unique()
)

filtered = df[
    (df["Country"].isin(country)) &
    (df["Education"].isin(education)) &
    (df["Customer_Segment"].isin(segment))
]

st.markdown("## 📈 Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", len(filtered))
c2.metric("Average Income", f"₹{filtered['Income'].mean():,.0f}")
c3.metric("Average Spend", f"₹{filtered['Total_Spend'].mean():,.0f}")
c4.metric("Response Rate", f"{filtered['Response'].mean()*100:.2f}%")
# ==========================
# DASHBOARD VISUALS
# ==========================

tab1, tab2, tab3 = st.tabs(
    ["Products & Channels", "Customers & Campaigns", "Heatmap"]
)

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Product Spending")

        product = filtered[
            [
                "MntWines",
                "MntFruits",
                "MntMeatProducts",
                "MntFishProducts",
                "MntSweetProducts",
                "MntGoldProds"
            ]
        ].sum()

        fig, ax = plt.subplots(figsize=(6,4))
        sns.barplot(x=product.index, y=product.values, ax=ax)
        plt.xticks(rotation=30)
        st.pyplot(fig)

    with col2:

        st.subheader("Purchase Channels")

        channels = filtered[
            [
                "NumDealsPurchases",
                "NumWebPurchases",
                "NumCatalogPurchases",
                "NumStorePurchases"
            ]
        ].sum()

        fig, ax = plt.subplots(figsize=(6,4))
        ax.pie(
            channels,
            labels=channels.index,
            autopct="%1.1f%%"
        )
        st.pyplot(fig)

with tab2:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Customer Segments")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.countplot(
            data=filtered,
            x="Customer_Segment",
            order=filtered["Customer_Segment"].value_counts().index,
            ax=ax
        )

        plt.xticks(rotation=20)
        st.pyplot(fig)

    with col2:

        st.subheader("Campaign Response")

        fig, ax = plt.subplots(figsize=(6,4))

        sns.countplot(
            data=filtered,
            x="Campaign_Responder",
            ax=ax
        )

        st.pyplot(fig)

with tab3:

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(10,7))

    sns.heatmap(
        filtered.select_dtypes(include="number").corr(),
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)
    # ==========================
# DATA & BUSINESS INSIGHTS
# ==========================

st.subheader("Customer Dataset")

st.dataframe(filtered)

st.subheader("Business Insights")

product_name = product.idxmax()
channel_name = channels.idxmax()
best_segment = (
    filtered.groupby("Customer_Segment")["Total_Spend"]
    .mean()
    .idxmax()
)

st.success(f"""
📌 Total Customers: {len(filtered)}

📌 Average Income: ₹{filtered['Income'].mean():,.0f}

📌 Average Spend: ₹{filtered['Total_Spend'].mean():,.0f}

📌 Campaign Response Rate: {filtered['Response'].mean()*100:.2f}%

📌 Highest Spending Product: {product_name}

📌 Most Preferred Purchase Channel: {channel_name}

📌 Best Performing Customer Segment: {best_segment}
""")

csv = filtered.to_csv(index=False)

st.download_button(
    "⬇ Download Filtered Data",
    csv,
    file_name="filtered_customers.csv",
    mime="text/csv"
)