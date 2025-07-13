from sklearn.cluster import KMeans

def run_clustering(df, config):
    k = config.get('n_clusters', 5)
    model = KMeans(n_clusters=k, random_state=42)
    return model.fit_predict(df)
