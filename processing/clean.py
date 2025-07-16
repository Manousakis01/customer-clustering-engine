def clean_data(df, config):
    if config.get("exclude_recontact_features", False):
        df = df[[col for col in df.columns if not col.startswith("core_re")]]

    # Drop columns with only NaNs
    df = df.dropna(axis=1, how='all')

    # Drop columns based on a threshold of non-missing values
    drop_thresh = config.get('drop_thresh', 0.8)
    min_non_na = int(drop_thresh * len(df))
    df = df.dropna(axis=1, thresh=min_non_na)

    # Impute missing values
    imputation_method = config.get('imputation_method', 'fill')
    if imputation_method == 'mode':
        # Use the mode (most frequent value) for each column
        df = df.apply(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 0), axis=0)
    else:
        # Default to filling with a static value
        fill_value = config.get('fill_value', 0.0)
        df = df.fillna(fill_value)

    return df
