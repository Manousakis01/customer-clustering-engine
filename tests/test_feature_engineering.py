import pandas as pd
from processing import feature_engineering

def test_build_features_variance():
    df = pd.DataFrame({'core_q1_1': [1, 1, 1], 'core_q2_1': [0, 1, 2], 'core_q3_1': [0, 0, 0]})
    config = {'min_unique': 0, 'use_variance_threshold': True}
    out = feature_engineering.build_features(df, config)
    assert 'core_q2_1' in out.columns
    assert 'core_q1_1' in out.columns or 'core_q3_1' not in out.columns
