from kfp.v2 import dsl
from kfp.v2.dsl import (
    Input,
    Output,
    Artifact,
    Dataset,
)

from google.cloud import storage

client = storage.Client.from_service_account_json('theta-byte-342416-3bb0f4e92c48.json')

kubeflow_storage_bucket = client.get_bucket('theta-byte-342416-kubeflowpipelines-default')


@dsl.pipeline(
    name='The Blue Alliance Preprocessing'
)
def pipeline(years: list):
    print(years)