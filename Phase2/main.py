from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
import pickle
import gzip

with gzip.open("tfidf_per_doc.pkl.gz", "rb") as file:
    X = pickle.load(file)

n_clusters = 6  
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

# Assuming X is your input data
X_clustered = kmeans.fit_predict(X)

svd = TruncatedSVD(n_components=2)
pipeline = make_pipeline(svd)
X_reduced = pipeline.fit_transform(X)

plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=X_clustered, cmap="viridis", marker=".")
plt.title("Document Clustering")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
