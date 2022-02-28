from google.cloud import storage

client = storage.Client.from_service_account_json('theta-byte-342416-3bb0f4e92c48.json')

bucket = client.get_bucket('main-storage-theta-byte')