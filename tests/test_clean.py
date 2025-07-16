import pandas as pd
from processing import clean

def test_clean_data_basic():
    df = pd.DataFrame({'a': [1, None, 3], 'core_re_x': [None, None, None]})
    config = {'exclude_recontact_features': True, 'drop_thresh': 0.5, 'fill_value': 0}
    cleaned = clean.clean_data(df, config)
    assert 'core_re_x' not in cleaned.columns
    assert cleaned.isna().sum().sum() == 0
