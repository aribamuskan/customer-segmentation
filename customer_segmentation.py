import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("customer_segmentation.csv")

print("=" * 60)
print("CUSTOMER SEGMENTATION PROJECT")
print("=" * 60)


# ============================================================
# 2. BASIC DATA UNDERSTANDING
# ============================================================

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 3. SELECT FEATURES
# ============================================================

features = [
    "age",
    "annual_income",
    "spending_score",
    "purchase_frequency",
    "average_purchase_value"
]

X = df[features]

print("\n" + "=" * 60)
print("SELECTED FEATURES")
print("=" * 60)

print(features)
print("\nFeature Shape:", X.shape)


# ============================================================
# 4. FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\n" + "=" * 60)
print("FEATURE SCALING")
print("=" * 60)

print("Scaling completed successfully.")


# ============================================================
# 5. ELBOW METHOD
# ============================================================

inertia_values = []

K_range = range(2, 11)

for k in K_range:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    inertia_values.append(kmeans.inertia_)


print("\n" + "=" * 60)
print("ELBOW METHOD RESULTS")
print("=" * 60)

for k, inertia in zip(K_range, inertia_values):

    print(
        f"K = {k}: "
        f"Inertia = {inertia:.2f}"
    )


# ============================================================
# 6. ELBOW CURVE
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    list(K_range),
    inertia_values,
    marker="o"
)

plt.title(
    "Elbow Method for Optimal Number of Clusters"
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")

plt.xticks(list(K_range))

plt.grid(True)

plt.tight_layout()

plt.show()


# ============================================================
# 7. FINAL K-MEANS MODEL
# ============================================================

optimal_k = 4

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

cluster_labels = kmeans.fit_predict(X_scaled)

df["cluster"] = cluster_labels


# ============================================================
# 8. CLUSTER COUNTS
# ============================================================

print("\n" + "=" * 60)
print("K-MEANS CLUSTERING")
print("=" * 60)

print("\nNumber of Clusters:", optimal_k)

print("\nCluster Counts:")

print(
    df["cluster"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 9. CLUSTER SUMMARY
# ============================================================

cluster_summary = df.groupby("cluster")[features].mean()

print("\n" + "=" * 60)
print("CLUSTER SUMMARY")
print("=" * 60)

print(
    cluster_summary.round(2)
)


# ============================================================
# 10. MEANINGFUL CUSTOMER SEGMENT NAMES
# ============================================================

segment_names = {
    0: "Young Frequent Shoppers",
    1: "High-Income Low-Spending",
    2: "High-Value Customers",
    3: "Moderate Customers"
}

df["customer_segment"] = df["cluster"].map(segment_names)


# ============================================================
# 11. DISPLAY SEGMENT DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("CUSTOMER SEGMENT DISTRIBUTION")
print("=" * 60)

segment_counts = (
    df["customer_segment"]
    .value_counts()
)

print("\n")

print(segment_counts)


# ============================================================
# 12. SEGMENT PROFILE
# ============================================================

segment_profile = df.groupby(
    "customer_segment"
)[features].mean().round(2)

print("\n" + "=" * 60)
print("CUSTOMER SEGMENT PROFILE")
print("=" * 60)

print("\n")

print(segment_profile)


# ============================================================
# 13. SAVE FINAL DATASET
# ============================================================

df.to_csv(
    "customer_segments.csv",
    index=False
)

print("\n" + "=" * 60)
print("DATASET SAVED")
print("=" * 60)

print("\nFile:")
print("customer_segments.csv")


# ============================================================
# 14. VISUALIZATION
# ============================================================

plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    df["annual_income"],
    df["spending_score"],
    c=df["cluster"],
    s=70,
    alpha=0.7
)

plt.title(
    "Customer Segments: Annual Income vs Spending Score"
)

plt.xlabel("Annual Income")

plt.ylabel("Spending Score")

plt.grid(True)

plt.colorbar(
    scatter,
    label="Cluster"
)

plt.tight_layout()

plt.show()


# ============================================================
# 15. SEGMENT DISTRIBUTION CHART
# ============================================================

plt.figure(figsize=(10, 6))

segment_counts.plot(
    kind="bar"
)

plt.title(
    "Customer Segment Distribution"
)

plt.xlabel("Customer Segment")

plt.ylabel("Number of Customers")

plt.xticks(
    rotation=25,
    ha="right"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ============================================================
# 16. FINAL PROJECT STATUS
# ============================================================

print("\n" + "=" * 60)
print("PROJECT STATUS")
print("=" * 60)

print("\nCustomer segmentation completed successfully.")

print("\nCustomer Segments:")

for cluster, name in segment_names.items():
    print(f"Cluster {cluster}: {name}")

print("\nGenerated Files:")
print("1. customer_segmentation.csv")
print("2. customer_segments.csv")

print("\nNext step:")
print("Build an interactive Streamlit dashboard.")