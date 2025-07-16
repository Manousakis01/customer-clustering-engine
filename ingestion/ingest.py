import pandas as pd
from storage.minio_client import download_from_minio


def load_data(storage_config):
    filepath = download_from_minio(
        bucket=storage_config['bucket'],
        object_name=storage_config['object_name'],
        local_path=storage_config['local_path']
    )
    print(filepath)
    if filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    elif filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    else:
        raise ValueError("Unsupported file format")
