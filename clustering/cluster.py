from sklearn.cluster import KMeans, AgglomerativeClustering


def run_clustering(df, config):
    method = config.get("method", "kmeans").lower()
    n_clusters = config.get("n_clusters", 5)
    if method == "kmeans":
        model = KMeans(n_clusters=n_clusters, random_state=42)
    elif method == "agglomerative":
        model = AgglomerativeClustering(n_clusters=n_clusters)
    else:
        raise ValueError(f"Unknown clustering method: {method}")

    return model.fit_predict(df)
