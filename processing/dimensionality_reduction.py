from sklearn.decomposition import PCA
import umap.umap_ as umap

def reduce(df, config):
    method = config.get('method', 'pca')
    n_components = config.get('n_components', 10)
    if method == 'umap':
        reducer = umap.UMAP(n_components=n_components, random_state=42)
    else:
        reducer = PCA(n_components=n_components, random_state=42)
    return reducer.fit_transform(df)
