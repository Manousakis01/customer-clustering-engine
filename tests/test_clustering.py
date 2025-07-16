import numpy as np
from clustering import cluster

def test_run_clustering_kmeans():
    df = np.random.rand(10, 2)
    config = {'method': 'kmeans', 'n_clusters': 2}
    labels = cluster.run_clustering(df, config)
    assert len(labels) == 10

def test_run_clustering_agglomerative():
    df = np.random.rand(10, 2)
    config = {'method': 'agglomerative', 'n_clusters': 2}
    labels = cluster.run_clustering(df, config)
    assert len(labels) == 10
