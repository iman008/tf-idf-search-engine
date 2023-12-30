from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
import pickle
import gzip
from mpl_toolkits.mplot3d import Axes3D

with gzip.open("tfidf_per_doc.pkl.gz", "rb") as file:
    X = pickle.load(file)

n_clusters = 10
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

X_clustered = kmeans.fit_predict(X)

svd = TruncatedSVD(n_components=3)
pipeline = make_pipeline(svd)
X_reduced = pipeline.fit_transform(X)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=X_clustered,
    cmap="viridis",
    marker=".",
)

ax.set_title("Document Clustering in 3D")
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_zlabel("Principal Component 3")

colorbar = fig.colorbar(scatter, ax=ax, pad=0.1)
colorbar.set_label("Cluster")

plt.show()
