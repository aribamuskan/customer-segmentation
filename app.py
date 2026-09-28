import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1e1b4b 100%);
        color: white;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        font-size: 17px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    .metric-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.20);
    }

    .metric-title {
        font-size: 14px;
        color: #cbd5e1;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 800;
        color: white;
    }

    .section-title {
        font-size: 27px;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .insight-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .insight-title {
        font-size: 19px;
        font-weight: 700;
        color: #e0e7ff;
        margin-bottom: 8px;
    }

    .insight-text {
        font-size: 15px;
        color: #cbd5e1;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 40px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("customer_segments.csv")


try:
    df = load_data()

except FileNotFoundError:
    st.error(
        "❌ customer_segments.csv file nahi mili. "
        "Pehle customer_segmentation.py run karo."
    )
    st.stop()


# ============================================================
# BASIC DATA PREPARATION
# ============================================================

segment_names = sorted(df["customer_segment"].dropna().unique())

numeric_columns = [
    "age",
    "annual_income",
    "spending_score",
    "purchase_frequency",
    "average_purchase_value"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎯 Dashboard Controls")

st.sidebar.markdown(
    """
    **Customer Segmentation**

    Use the filters below to explore different customer groups.
    """
)

selected_segments = st.sidebar.multiselect(
    "Select Customer Segments",
    options=segment_names,
    default=segment_names
)

income_range = st.sidebar.slider(
    "Annual Income Range",
    min_value=int(df["annual_income"].min()),
    max_value=int(df["annual_income"].max()),
    value=(
        int(df["annual_income"].min()),
        int(df["annual_income"].max())
    ),
    step=1000
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    (df["customer_segment"].isin(selected_segments))
    &
    (df["annual_income"].between(income_range[0], income_range[1]))
].copy()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">👥 Customer Segmentation Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Explore customer behavior, spending patterns, income levels, and market segments.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# KPI CARDS
# ============================================================

total_customers = len(filtered_df)
total_segments = filtered_df["customer_segment"].nunique()

if total_customers > 0:
    average_income = filtered_df["annual_income"].mean()
    average_spending = filtered_df["spending_score"].mean()
else:
    average_income = 0
    average_spending = 0


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">👥 Total Customers</div>
            <div class="metric-value">{total_customers:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">🧩 Total Segments</div>
            <div class="metric-value">{total_segments}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">💰 Average Income</div>
            <div class="metric-value">${average_income:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">🛍️ Avg Spending Score</div>
            <div class="metric-value">{average_spending:.1f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SEGMENT DISTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-title">📊 Customer Segment Distribution</div>',
    unsafe_allow_html=True
)

if len(filtered_df) > 0:

    col1, col2 = st.columns(2)

    segment_counts = (
        filtered_df["customer_segment"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = ["customer_segment", "count"]

    with col1:

        fig_pie = px.pie(
            segment_counts,
            names="customer_segment",
            values="count",
            hole=0.45,
            title="Customers by Segment"
        )

        fig_pie.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            legend_title_text="Segment"
        )

        st.plotly_chart(
            fig_pie,
            use_container_width=True
        )

    with col2:

        fig_bar = px.bar(
            segment_counts,
            x="customer_segment",
            y="count",
            text="count",
            title="Segment Customer Count"
        )

        fig_bar.update_traces(
            textposition="outside"
        )

        fig_bar.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            xaxis_title="Customer Segment",
            yaxis_title="Number of Customers"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

else:
    st.warning("No customers match the selected filters.")


# ============================================================
# CUSTOMER BEHAVIOR VISUALIZATION
# ============================================================

st.markdown(
    '<div class="section-title">📈 Customer Behavior Analysis</div>',
    unsafe_allow_html=True
)

if len(filtered_df) > 0:

    col1, col2 = st.columns(2)

    with col1:

        fig_scatter = px.scatter(
            filtered_df,
            x="annual_income",
            y="spending_score",
            color="customer_segment",
            size="average_purchase_value",
            hover_data=[
                "customer_id",
                "age",
                "purchase_frequency",
                "average_purchase_value"
            ],
            title="Income vs Spending Score"
        )

        fig_scatter.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            xaxis_title="Annual Income",
            yaxis_title="Spending Score"
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

    with col2:

        fig_frequency = px.scatter(
            filtered_df,
            x="purchase_frequency",
            y="average_purchase_value",
            color="customer_segment",
            size="spending_score",
            hover_data=[
                "customer_id",
                "age",
                "annual_income"
            ],
            title="Purchase Frequency vs Average Purchase Value"
        )

        fig_frequency.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            xaxis_title="Purchase Frequency",
            yaxis_title="Average Purchase Value"
        )

        st.plotly_chart(
            fig_frequency,
            use_container_width=True
        )


# ============================================================
# SEGMENT PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">🧩 Segment Profiles</div>',
    unsafe_allow_html=True
)

if len(filtered_df) > 0:

    profile = (
        filtered_df
        .groupby("customer_segment")[numeric_columns]
        .mean()
        .round(2)
    )

    st.dataframe(
        profile,
        use_container_width=True
    )


# ============================================================
# SEGMENT INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">💡 Segment Insights</div>',
    unsafe_allow_html=True
)

if len(filtered_df) > 0:

    segment_profile = (
        filtered_df
        .groupby("customer_segment")[numeric_columns]
        .mean()
    )

    for segment, row in segment_profile.iterrows():

        if segment == "Young Frequent Shoppers":

            insight = (
                f"This segment has an average age of {row['age']:.1f}, "
                f"annual income of ${row['annual_income']:,.0f}, "
                f"and purchase frequency of {row['purchase_frequency']:.1f}. "
                "These customers purchase frequently despite having relatively "
                "lower income levels."
            )

        elif segment == "High-Income Low-Spending":

            insight = (
                f"This segment has an average income of "
                f"${row['annual_income']:,.0f}, but its spending score is "
                f"{row['spending_score']:.1f}. "
                "Customers in this group have strong income levels but comparatively "
                "lower spending activity."
            )

        elif segment == "High-Value Customers":

            insight = (
                f"This segment has an average income of "
                f"${row['annual_income']:,.0f}, spending score of "
                f"{row['spending_score']:.1f}, purchase frequency of "
                f"{row['purchase_frequency']:.1f}, and average purchase value of "
                f"${row['average_purchase_value']:,.2f}. "
                "This group shows strong purchasing activity and high customer value."
            )

        elif segment == "Moderate Customers":

            insight = (
                f"This segment has an average income of "
                f"${row['annual_income']:,.0f} and spending score of "
                f"{row['spending_score']:.1f}. "
                "Their purchasing behavior remains around the middle range "
                "compared with the other segments."
            )

        else:

            insight = (
                f"This segment has an average income of "
                f"${row['annual_income']:,.0f}, spending score of "
                f"{row['spending_score']:.1f}, and purchase frequency of "
                f"{row['purchase_frequency']:.1f}."
            )

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">🔹 {segment}</div>
                <div class="insight-text">{insight}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# INDIVIDUAL CUSTOMER LOOKUP
# ============================================================

st.markdown(
    '<div class="section-title">🔎 Customer Lookup</div>',
    unsafe_allow_html=True
)

customer_ids = df["customer_id"].tolist()

selected_customer = st.selectbox(
    "Select a Customer ID",
    customer_ids
)

customer = df[
    df["customer_id"] == selected_customer
]

if not customer.empty:

    customer_row = customer.iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Customer Age",
            int(customer_row["age"])
        )

        st.metric(
            "Annual Income",
            f"${customer_row['annual_income']:,.0f}"
        )

    with col2:
        st.metric(
            "Spending Score",
            f"{customer_row['spending_score']:.0f}"
        )

        st.metric(
            "Purchase Frequency",
            f"{customer_row['purchase_frequency']:.0f}"
        )

    with col3:
        st.metric(
            "Average Purchase Value",
            f"${customer_row['average_purchase_value']:,.2f}"
        )

        st.metric(
            "Customer Segment",
            customer_row["customer_segment"]
        )


# ============================================================
# FILTERED CUSTOMER DATA
# ============================================================

st.markdown(
    '<div class="section-title">📋 Customer Data</div>',
    unsafe_allow_html=True
)

display_columns = [
    "customer_id",
    "age",
    "annual_income",
    "spending_score",
    "purchase_frequency",
    "average_purchase_value",
    "customer_segment"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DOWNLOAD BUTTON
# ============================================================

download_data = filtered_df[display_columns].to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Customer Data",
    data=download_data,
    file_name="filtered_customer_segments.csv",
    mime="text/csv"
)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🤖 About This Project</div>',
    unsafe_allow_html=True
)

st.info(
    """
    This project uses **K-Means Clustering**, an unsupervised machine learning
    algorithm, to group customers according to their behavioral and demographic
    characteristics.

    The clustering features include:

    • Age  
    • Annual Income  
    • Spending Score  
    • Purchase Frequency  
    • Average Purchase Value  

    Customer ID was excluded from clustering because it is only an identifier.

    The dataset used in this project is **synthetically generated for learning
    and portfolio purposes**.
    """
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Customer Segmentation • K-Means Clustering • Machine Learning • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)