from sklearn.metrics import silhouette_score

def print_scores(X, labels):
    score = silhouette_score(X, labels)
    print(f"Silhouette Score: {score:.3f}")