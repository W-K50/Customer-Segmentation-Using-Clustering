# Customer-Segmentation-Using-Clustering Report

**1. Introduction**
Customer segmentation is a crucial process for businesses to understand different groups of customers based on their behavior, demographics, and spending patterns. In this study, we apply clustering techniques to segment customers using the Mall Customer Segmentation Dataset, which includes features such as Age, Annual Income, and Spending Score.

**2. Methodology**
**2.1 Exploratory Data Analysis (EDA)**
We performed EDA to analyze customer demographics and spending habits. This included:
Descriptive statistics of Age, Income, and Spending Score.
Visualizations such as histograms and scatter plots to identify patterns.

**2.2 Clustering Techniques**
We applied K-Means clustering to segment customers. The optimal number of clusters was determined using:
Elbow Method (finding the best k based on within-cluster variance).
Silhouette Score (measuring cluster separation).
The dataset was then divided into 6 distinct customer segments based on spending behavior and demographics.

**3. Results and Customer Segments**
The six identified segments are:

Cluster	Segment Name	Key Characteristics
0	Premium Shoppers 🏆	Young, high income, high spending. Loyal customers.
1	Wealthy Cautious Buyers 💰	High income, low spending. Potential for upselling.
2	Budget-Conscious Shoppers 🛍️	Low income but high spending. Focused on discounts and deals.
3	Average Consumers 👨‍👩‍👧‍👦	Medium income, moderate spending. General consumers.
4	Low-Income Minimal Spenders 🚶‍♂️	Elderly, low income, low spending. Needs basic services.
5	Wealthy Retired Spenders 🎩	Older, high income, high spending. Interested in premium services.

**4. Visualization and Insights**
To enhance business decision-making, we developed a Streamlit dashboard that includes:
Scatter plots for spending vs. income analysis.
3D cluster visualization (Age, Income, Spending Score).
Pie charts to show segment distribution.

**5. Business Implications**
This segmentation helps businesses personalize marketing strategies:
Premium Shoppers → Offer exclusive memberships & luxury deals.
Budget-Conscious Shoppers → Provide discount-based promotions.
Wealthy Cautious Buyers → Incentivize them with premium loyalty programs.
