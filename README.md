# 👥 Customer Segmentation using K-Means Clustering

An end-to-end Machine Learning project that uses **K-Means Clustering** to segment customers based on their demographic and purchasing behavior, with an interactive **Streamlit dashboard** for exploring customer segments and insights.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://customer-segmentation-codkvraszx8vnukjupw5zq.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/aribamuskan/customer-segmentation)

---

## 🚀 Live Demo

🔗 **Streamlit Dashboard:**  
https://customer-segmentation-codkvraszx8vnukjupw5zq.streamlit.app/

🔗 **GitHub Repository:**  
https://github.com/aribamuskan/customer-segmentation

---

## 📌 Project Overview

Customer segmentation is an important business analytics task that helps organizations understand different groups of customers based on their behavior and characteristics.

In this project, **K-Means Clustering**, an unsupervised Machine Learning algorithm, is used to divide customers into meaningful groups using:

- Age
- Annual Income
- Spending Score
- Purchase Frequency
- Average Purchase Value

The resulting customer segments are visualized through an interactive Streamlit dashboard.

> **Note:** The dataset used in this project is synthetically generated for learning and portfolio purposes.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Understand customer behavior using unsupervised learning
- Apply K-Means clustering
- Identify meaningful customer segments
- Use feature scaling before clustering
- Determine a suitable number of clusters using the Elbow Method
- Analyze and interpret customer segments
- Build an interactive Streamlit dashboard
- Provide customer-level lookup and segment insights
- Allow filtered customer data to be downloaded

---

## 🤖 Machine Learning Approach

The project follows these main steps:

1. Generate the customer dataset
2. Load and inspect the data
3. Perform basic data understanding
4. Select relevant clustering features
5. Scale the features using `StandardScaler`
6. Apply the Elbow Method
7. Select `K = 4`
8. Train the K-Means clustering model
9. Assign customers to clusters
10. Interpret and name the customer segments
11. Build an interactive Streamlit dashboard

---

## 📊 Dataset

The dataset contains **500 synthetic customers** with the following columns:

| Feature | Description |
|---|---|
| `customer_id` | Unique customer identifier |
| `age` | Customer age |
| `annual_income` | Customer annual income |
| `spending_score` | Customer spending score |
| `purchase_frequency` | Customer purchase frequency |
| `average_purchase_value` | Average value of customer purchases |

### Dataset Characteristics

- Total customers: **500**
- Missing values: **0**
- Clustering features: **5**
- Customer identifier: `customer_id`

The `customer_id` column was excluded from clustering because it is only an identifier and does not represent customer behavior.

---

## ⚙️ Feature Scaling

The selected numerical features have different ranges.

For example, annual income contains much larger numerical values than spending score.

To prevent features with larger numerical ranges from dominating the clustering process, `StandardScaler` was used.

After scaling, the features have a comparable scale for K-Means clustering.

---

## 📐 Elbow Method

The Elbow Method was used to evaluate different values of `K`.

The tested values were **K = 2 to 10**.

| K | Inertia |
|---:|---:|
| 2 | 1685.46 |
| 3 | 1038.38 |
| 4 | 883.24 |
| 5 | 789.10 |
| 6 | 735.47 |
| 7 | 682.46 |
| 8 | 637.95 |
| 9 | 607.59 |
| 10 | 576.10 |

Based on the Elbow Method and the structure of the synthetic dataset, **K = 4** was selected for the final clustering model.

---

## 🧠 K-Means Clustering

The final K-Means model used:

- Number of clusters: **4**
- `random_state`: **42**
- `n_init`: **10**

K-Means assigns each customer to one of the four clusters based on similarity across the selected features.

---

## 👥 Customer Segments

The final clustering produced four customer segments.

### 1. 🛍️ Young Frequent Shoppers

Average characteristics:

- Age: **27.64**
- Annual Income: **$36,256.68**
- Spending Score: **69.58**
- Purchase Frequency: **10.48**
- Average Purchase Value: **$66.55**
- Customers: **128**

This group contains relatively younger customers with lower average income but frequent purchasing behavior and a relatively high spending score.

---

### 2. 💼 High-Income Low-Spending

Average characteristics:

- Age: **45.76**
- Annual Income: **$93,718.27**
- Spending Score: **30.77**
- Purchase Frequency: **4.18**
- Average Purchase Value: **$102.09**
- Customers: **119**

This group has the highest average income among the segments but comparatively lower spending activity and purchase frequency.

---

### 3. ⭐ High-Value Customers

Average characteristics:

- Age: **35.73**
- Annual Income: **$88,343.30**
- Spending Score: **80.64**
- Purchase Frequency: **12.30**
- Average Purchase Value: **$180.15**
- Customers: **128**

This segment combines high income with high spending activity, high purchase frequency, and the highest average purchase value among the four groups.

---

### 4. 📊 Moderate Customers

Average characteristics:

- Age: **38.24**
- Annual Income: **$59,922.04**
- Spending Score: **51.12**
- Purchase Frequency: **6.51**
- Average Purchase Value: **$111.07**
- Customers: **125**

This group shows relatively moderate income, spending score, purchase frequency, and purchase value compared with the other segments.

---

## 📈 Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring the customer segmentation results.

### Dashboard Features

#### 📊 KPI Cards

- Total Customers
- Total Segments
- Average Annual Income
- Average Spending Score

#### 🥧 Segment Distribution

- Customer distribution by segment
- Number of customers in each segment

#### 📈 Customer Behavior Analysis

- Annual Income vs Spending Score
- Purchase Frequency vs Average Purchase Value

#### 🧩 Segment Profiles

The dashboard provides average numerical characteristics for each customer segment.

#### 🔎 Customer Lookup

Users can select an individual customer ID and view:

- Age
- Annual Income
- Spending Score
- Purchase Frequency
- Average Purchase Value
- Customer Segment

#### 🎯 Filters

Users can filter customers by:

- Customer Segment
- Annual Income Range

#### 📥 Data Download

Filtered customer data can be downloaded as a CSV file directly from the dashboard.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- K-Means Clustering
- StandardScaler

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Plotly

### Dashboard

- Streamlit

### Development Tools

- VS Code
- Git
- GitHub

---

## 📁 Project Structure

```text
customer-segmentation/
│
├── app.py
├── customer_segmentation.py
├── generate_dataset.py
├── customer_segmentation.csv
├── customer_segments.csv
├── requirements.txt
└── README.md
```

### File Descriptions

| File | Purpose |
|---|---|
| `generate_dataset.py` | Generates the synthetic customer dataset |
| `customer_segmentation.py` | Performs data analysis, scaling, Elbow Method, and K-Means clustering |
| `customer_segmentation.csv` | Original synthetic customer dataset |
| `customer_segments.csv` | Dataset containing cluster and segment assignments |
| `app.py` | Interactive Streamlit dashboard |
| `requirements.txt` | Python dependencies required for deployment |
| `README.md` | Project documentation |

---

## ⚙️ Installation

Clone the repository:

    git clone https://github.com/aribamuskan/customer-segmentation.git

Navigate to the project directory:

    cd customer-segmentation

Install the required dependencies:

    python -m pip install -r requirements.txt

---

## ▶️ Run the Machine Learning Project

To generate the synthetic dataset:

    python generate_dataset.py

Then run the clustering analysis:

    python customer_segmentation.py

This will generate the customer segmentation results and visualizations.

---

## 🌐 Run the Streamlit Dashboard

Run:

    python -m streamlit run app.py

The dashboard will open locally in your browser.

The local application will normally be available at:

    http://localhost:8501

---

## 📊 Machine Learning Results

The final K-Means model divided the 500 customers into four segments:

| Customer Segment | Customers |
|---|---:|
| Young Frequent Shoppers | 128 |
| High-Income Low-Spending | 119 |
| High-Value Customers | 128 |
| Moderate Customers | 125 |
| **Total** | **500** |

The cluster labels generated by K-Means are numerical identifiers. The segment names were assigned after analyzing the average characteristics of each cluster.

---

## 💡 Customer Segment Insights

The segmentation demonstrates that customers can have significantly different combinations of:

- Income
- Spending behavior
- Purchase frequency
- Purchase value
- Age

For example, the **High-Income Low-Spending** group has relatively high income but lower spending activity, while the **High-Value Customers** group combines high income with high spending and purchasing activity.

These types of segments can help businesses analyze customer behavior and explore data-driven marketing or customer engagement strategies.

---

## 🚀 Future Improvements

Possible future improvements include:

- Add more customer behavioral features
- Experiment with different clustering algorithms
- Compare K-Means with Hierarchical Clustering and DBSCAN
- Add cluster quality metrics such as Silhouette Score
- Add interactive cluster visualization using PCA
- Add automated segment recommendations
- Connect the dashboard to a real customer database
- Add authentication for dashboard access

---

## ⚠️ Limitations

This project uses a **synthetically generated dataset**, so the results do not represent real-world customer behavior.

The identified segments are specific to the generated dataset and should not be interpreted as universal customer categories.

For production use, the model would need to be trained and validated using relevant real-world customer data.

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

- Unsupervised Machine Learning
- K-Means Clustering
- Feature Selection
- Feature Scaling
- Elbow Method
- Cluster Interpretation
- Pandas Data Analysis
- Data Visualization
- Interactive Dashboard Development
- Streamlit
- Git and GitHub

---

## 👩‍💻 Author

**Ariba Muskan**

Software Engineering Student  
Pakistan

### GitHub

https://github.com/aribamuskan

---

## ⭐ Project

If you find this project useful for learning Machine Learning and customer analytics, consider giving the repository a ⭐ on GitHub.