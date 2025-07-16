import pytest
import pandas as pd
from ingestion import ingest

class DummyMinio:
    def fget_object(self, bucket, object_name, local_path):
        # Simulate CSV creation
        with open(local_path, 'w') as f:
            f.write('a,b\n1,2\n')
        return local_path

def test_load_data_csv(monkeypatch, tmp_path):
    # Patch download_from_minio to use DummyMinio
    def dummy_download_from_minio(bucket, object_name, local_path):
        path = tmp_path / 'dummy.csv'
        with open(path, 'w') as f:
            f.write('a,b\n1,2\n')
        return str(path)
    monkeypatch.setattr(ingest, 'download_from_minio', dummy_download_from_minio)
    cfg = {'bucket': 'b', 'object_name': 'o', 'local_path': str(tmp_path / 'dummy.csv')}
    df = ingest.load_data(cfg)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['a', 'b']
    assert df.iloc[0, 0] == 1

# Error case: unsupported file

def test_load_data_unsupported(monkeypatch, tmp_path):
    def dummy_download_from_minio(bucket, object_name, local_path):
        path = tmp_path / 'dummy.txt'
        with open(path, 'w') as f:
            f.write('some text')
        return str(path)
    monkeypatch.setattr(ingest, 'download_from_minio', dummy_download_from_minio)
    cfg = {'bucket': 'b', 'object_name': 'o', 'local_path': str(tmp_path / 'dummy.txt')}
    with pytest.raises(ValueError):
        ingest.load_data(cfg)
