import numpy as np
import matplotlib.pyplot as plt

np.random.seed(45)  # for reproducibility
X = np.random.rand(100, 2)  # 100 data points in 2D space
X[:5]

class KMeansClusterer:
   
    def __init__(self, k=3, max_iter=100, tol=1e-4):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.centroids = None

    def _get_random_centroids(self, X):
        n = X.shape[0]  # no. of data points
        return X[np.random.choice(n, self.k, replace=False)]

    def _assign_clusters(self, X):
        # Compute distances from each point in X to each centroid
        distances = np.linalg.norm(X[:, None] - self.centroids, axis=2)

        labels = np.argmin(distances, axis=1)
        return labels

    def _update_centroids(self, X, clusters):
        new_centroids = np.array(
            [X[clusters == i].mean(axis=0) for i in range(self.k)])  # mean of points in each cluster
        return new_centroids

    def fit(self, X):
        self.centroids = self._get_random_centroids(X)

        for i in range(self.max_iter):
   
            clusters = self._assign_clusters(X)
            new_centroids = self._update_centroids(X, clusters)

            if np.linalg.norm(new_centroids - self.centroids) < self.tol:
                print(f"Converged after {i} iterations")
                break
            self.centroids = new_centroids

        return clusters
    
kmeans = KMeansClusterer(k=3)
clusters = kmeans.fit(X)
kmeans.centroids
clusters[:5]

plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.centroids[:, 0],
            kmeans.centroids[:, 1], c='red', s=200, marker='x', label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means clustering')
plt.legend()
plt.show()