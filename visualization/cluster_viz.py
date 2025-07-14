import matplotlib.pyplot as plt
import seaborn as sns

def visualize(X, labels):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette='Set2')
    plt.title("Cluster Visualization")
    plt.show()
