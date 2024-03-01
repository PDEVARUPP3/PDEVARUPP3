Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import pandas as pd
... import matplotlib.pyplot as plt
... from sklearn.cluster import KMeans
... from sklearn.preprocessing import StandardScaler
... 
... # Generate synthetic customer data
... np.random.seed(42)
... n_customers = 200
... age = np.random.randint(18, 70, size=n_customers)
... income = np.random.randint(20000, 150000, size=n_customers)
... spending_score = np.random.randint(1, 100, size=n_customers)
... 
... # Create DataFrame
... data = pd.DataFrame({
...     'Age': age,
...     'Income': income,
...     'Spending Score': spending_score
... })
... 
... # Standardize the data
... scaler = StandardScaler()
... scaled_data = scaler.fit_transform(data)
... 
... # Perform K-Means clustering
... k = 5  # Number of clusters
... kmeans = KMeans(n_clusters=k, random_state=42)
... clusters = kmeans.fit_predict(scaled_data)
... 
... # Add cluster labels to DataFrame
... data['Cluster'] = clusters
... 
... # Visualize clusters
... plt.figure(figsize=(10, 6))
... plt.scatter(data['Age'], data['Spending Score'], c=data['Cluster'], cmap='viridis', s=50)
... plt.xlabel('Age')
... plt.ylabel('Spending Score')
... plt.title('Customer Segmentation - K-Means Clustering')
... plt.colorbar(label='Cluster')
... plt.show()
... 
... # Analyze cluster characteristics
... cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
... cluster_data = pd.DataFrame(cluster_centers, columns=data.columns[:-1])
... cluster_data['Cluster'] = range(k)
print("Cluster Centers:")
print(cluster_data)
