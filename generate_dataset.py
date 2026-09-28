import numpy as np
import pandas as pd

# Reproducible results
np.random.seed(42)

# Number of customers
n = 500

# Hidden customer behavior groups used only
# to generate realistic synthetic data
customer_types = np.random.choice(
    [0, 1, 2, 3],
    size=n,
    p=[0.25, 0.25, 0.25, 0.25]
)

# Empty arrays
age = np.zeros(n)
annual_income = np.zeros(n)
spending_score = np.zeros(n)
purchase_frequency = np.zeros(n)
average_purchase_value = np.zeros(n)

# Generate different customer behavior patterns
for i, customer_type in enumerate(customer_types):

    if customer_type == 0:
        # High income + high spending
        age[i] = np.random.normal(35, 8)
        annual_income[i] = np.random.normal(90000, 15000)
        spending_score[i] = np.random.normal(80, 10)
        purchase_frequency[i] = np.random.normal(12, 3)
        average_purchase_value[i] = np.random.normal(180, 35)

    elif customer_type == 1:
        # High income + low spending
        age[i] = np.random.normal(45, 10)
        annual_income[i] = np.random.normal(95000, 18000)
        spending_score[i] = np.random.normal(30, 10)
        purchase_frequency[i] = np.random.normal(4, 2)
        average_purchase_value[i] = np.random.normal(100, 25)

    elif customer_type == 2:
        # Low income + frequent purchases
        age[i] = np.random.normal(28, 7)
        annual_income[i] = np.random.normal(35000, 10000)
        spending_score[i] = np.random.normal(70, 12)
        purchase_frequency[i] = np.random.normal(10, 3)
        average_purchase_value[i] = np.random.normal(65, 15)

    else:
        # Moderate income + moderate spending
        age[i] = np.random.normal(40, 9)
        annual_income[i] = np.random.normal(60000, 12000)
        spending_score[i] = np.random.normal(50, 12)
        purchase_frequency[i] = np.random.normal(6, 2)
        average_purchase_value[i] = np.random.normal(110, 25)


# Create the customer dataset
df = pd.DataFrame({
    "customer_id": range(1, n + 1),

    "age": np.clip(
        age,
        18,
        75
    ).round().astype(int),

    "annual_income": np.clip(
        annual_income,
        15000,
        150000
    ).round().astype(int),

    "spending_score": np.clip(
        spending_score,
        1,
        100
    ).round().astype(int),

    "purchase_frequency": np.clip(
        purchase_frequency,
        1,
        25
    ).round().astype(int),

    "average_purchase_value": np.clip(
        average_purchase_value,
        10,
        500
    ).round(2)
})


# Save dataset as CSV
df.to_csv(
    "customer_segmentation.csv",
    index=False
)


# Display information
print("=" * 50)
print("CUSTOMER SEGMENTATION DATASET")
print("=" * 50)

print("\nDataset created successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset saved as:")
print("customer_segmentation.csv")