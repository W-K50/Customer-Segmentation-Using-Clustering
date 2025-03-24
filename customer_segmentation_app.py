import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv(r"C:\Users\hp\Desktop\Customer Segmentation Using Clustering\Customer_Segments.csv")


# Page Title
st.title("Customer Segmentation Dashboard")
st.markdown("### Explore customer segments based on spending behavior, age, and income")

# Sidebar filters
st.sidebar.header("Filter Customers")
selected_segment = st.sidebar.selectbox("Select Customer Segment", df["Segment"].unique())

# Filtered Data
filtered_df = df[df["Segment"] == selected_segment]
st.write(f"Showing data for **{selected_segment}** segment")
st.dataframe(filtered_df)

# --- 1. Cluster Distribution Pie Chart ---
st.subheader("Customer Segment Distribution (Pie Chart)")
segment_counts = df["Segment"].value_counts()
fig_pie = px.pie(names=segment_counts.index, values=segment_counts.values, title="Customer Segments")
st.plotly_chart(fig_pie)

# --- 2. Scatter Plot (Income vs Spending Score) ---
st.subheader("Annual Income vs Spending Score")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Annual Income (k$)", y="Spending Score (1-100)", hue="Segment", palette="Set2")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segments")
plt.legend(title="Segment", bbox_to_anchor=(1,1))
st.pyplot(plt)

# --- 3. 3D Clustering Visualization ---
st.subheader("3D Cluster Visualization (Age, Income, Spending Score)")
fig_3d = px.scatter_3d(df, x="Age", y="Annual Income (k$)", z="Spending Score (1-100)", 
                       color="Segment", opacity=0.8, title="Customer Segments in 3D")
st.plotly_chart(fig_3d)

# --- 4. Summary Statistics ---
st.subheader("Segment Insights")
st.write(df.groupby("Segment")[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].mean())

# Footer
st.markdown("**Created By WISHAL KHAN using Streamlit**")
