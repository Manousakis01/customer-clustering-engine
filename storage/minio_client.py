from minio import Minio
import os


def download_from_minio(bucket, object_name, local_path="/tmp/dataset.csv"):
    client = Minio(
        #str(os.getenv("MINIO_ENDPOINT")),
        endpoint="172.18.0.2:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    return local_path
