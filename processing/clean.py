def clean_data(df, config):
    if config.get("exclude_recontact_features", False):
        df = df[[col for col in df.columns if not col.startswith("core_re")]]

    # drop columns with only NaNs
    df = df.dropna(axis=1, how='all')

    drop_thresh = config.get('drop_thresh', 0.8)
    min_non_na = int(drop_thresh * len(df))
    df = df.dropna(axis=1, thresh=min_non_na)

    fill_value = config.get('fill_value', 0.0)
    df = df.fillna(fill_value)
    return df
