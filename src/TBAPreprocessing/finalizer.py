
def finalize():

    from google.cloud import storage

    client = storage.Client.from_service_account_json('theta-byte-342416-3bb0f4e92c48.json')

    main_storage_bucket = client.get_bucket('main-storage-theta-byte')
    kubeflow_storage_bucket = client.get_bucket('theta-byte-342416-kubeflowpipelines-default')


if __name__ == "__main__":
    finalize()