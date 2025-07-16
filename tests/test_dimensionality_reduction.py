import numpy as np
import pandas as pd
from processing import dimensionality_reduction

def test_reduce_pca():
    df = pd.DataFrame(np.random.rand(10, 4))
    config = {'method': 'pca', 'n_components': 2}
    reduced = dimensionality_reduction.reduce(df, config)
    assert reduced.shape[1] == 2
