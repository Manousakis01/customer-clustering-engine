import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage


def get_cluster_plots(X, labels, config):
    figs = []

    # --- Cluster Scatter Plot ---
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette='Set2', ax=ax1)
    ax1.set_title("Cluster Visualization")
    figs.append(fig1)

    # --- Optional Dendrogram ---
    if config.get("method") == "agglomerative":
        Z = linkage(X, method='ward')
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        dendrogram(Z, ax=ax2)
        ax2.set_title("Hierarchical Clustering Dendrogram")
        figs.append(fig2)

    return figs
