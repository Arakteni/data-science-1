import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)

y_kmeans = kmeans.fit_predict(X)

df['Cluster'] = y_kmeans

plt.figure(figsize=(10, 6))  
sns.scatterplot(
    x='Annual Income (k$)', 
    y='Spending Score (1-100)',
    hue='Cluster',  
    data=df,        
    palette='viridis',  
    s=80           
)

centers = kmeans.cluster_centers_
plt.scatter(
    centers[:, 0], centers[:, 1],
    marker='X', s=200, c='red',  
    label='Centroids'
)

plt.title('Кластеризация клиентов по доходу и уровню трат', fontsize=14)
plt.xlabel('Годовой доход (k$)', fontsize=12)
plt.ylabel('Оценка трат (1-100)', fontsize=12)
plt.legend()  
plt.grid(True, linestyle='--', alpha=0.7)  

plt.show()
