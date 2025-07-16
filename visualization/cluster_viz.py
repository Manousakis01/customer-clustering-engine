import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage


def visualize(X, labels, config):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette='Set2')
    plt.title("Cluster Visualization")
    plt.show()

    if config.get("method") == "agglomerative":
        plot_dendrogram(X, method='ward')


def plot_dendrogram(X, method='ward', output_path=None):
    Z = linkage(X, method=method)
    plt.figure(figsize=(10, 6))
    dendrogram(Z)
    plt.title("Hierarchical Clustering Dendrogram")
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
