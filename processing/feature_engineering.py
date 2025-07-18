import re
from collections import defaultdict
import pandas as pd
from sklearn.feature_selection import VarianceThreshold


def group_columns_by_question(df):
    """
    Groups columns based on question prefix (e.g., q1, q3, etc.).
    """
    groups = defaultdict(list)
    for col in df.columns:
        match = re.match(r"(core(?:_re)?_q\d+)_\d+", col)
        if match:
            question = match.group(1)
            groups[question].append(col)
    return groups


def build_features(df, config):
    min_unique = config.get('min_unique', 1)
    grouped = group_columns_by_question(df)

    # Drop full-zero question groups (optional, useful)
    for question, cols in grouped.items():
        if df[cols].sum().sum() == 0:
            df = df.drop(columns=cols)

    if config.get("use_variance_threshold", True):
        # Drop low-variance columns (uninformative)
        selector = VarianceThreshold(threshold=0.0)
        df = pd.DataFrame(selector.fit_transform(df), columns=df.columns[selector.get_support()], index=df.index)

    # Drop low-variance columns (uninformative)
    return df.loc[:, df.nunique() > min_unique]
