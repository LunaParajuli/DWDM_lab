
#6.3 Hierarchical Clustering (Agglomerative Clustering)

#Agglomerative Clustering

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchical_cluster.fit_predict(data)
print("Cluster Labels:",labels)

plt.scatter(x, y, c=labels)
plt.show()