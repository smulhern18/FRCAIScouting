

def grab_matches_for_events(event_ids: str, ) -> str:

    event_ids = event_ids.split(',')

    output_dir_path = 'pulled_matches'

    def grabMatches(event_id: str, bucket):
        year = event_id[0:4]

        # Allocate strings
        tba_read_key = 'vSedKwbovtAcDcYzaAl0QjcYwox4xXxC7r5b4zPpNS3X9BC6khgVlGhR3Fox2tYR'
        format_str = f'https://www.thebluealliance.com/api/v3/event/{event_id}/matches'

        import requests

        matches_in_event = requests.get(url=format_str, headers={'X-TBA-Auth-Key': tba_read_key})

        matches_json = matches_in_event.json()

        for match in matches_json:
            dir = bucket.blob(output_dir_path + '/' + year + '/' + event_id + '/' + match['key'])
            dir.upload_from_string(str(match))

            video_objects = match['videos']
            if len(video_objects) != 0:
                videos_to_grab = ''
                for video in video_objects:
                    if video['type'] == 'youtube':
                        videos_to_grab += (video['key']+',')
                videos_to_grab = videos_to_grab[:len(videos_to_grab)-1]
                dir = bucket.blob('video_keys/'+match['key'])
                dir.upload_from_string(videos_to_grab)

        # Grab the general event data also
        format_str = f'https://www.thebluealliance.com/api/v3/event/{event_id}'

        if len(matches_json) != 0:
            matches_in_event = requests.get(url=format_str, headers={'X-TBA-Auth-Key': tba_read_key})
            dir = bucket.blob(output_dir_path + '/' + year + '/' + event_id + '_event_data')
            dir.upload_from_string(str(matches_in_event.json()))

        print(datetime.datetime.now().date(), datetime.datetime.now().time(), ": Match obtaining done with", event_id)

    from google.cloud import storage
    import datetime

    client = storage.Client.from_service_account_info({"type": "service_account",
                                                       "project_id": "theta-byte-342416",
                                                       "private_key_id": "3bb0f4e92c48f894e7bb023330fed3247759f1a8",
                                                       "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDc3JxLdqz4mCbT\nNSRQFMosWaXKLpTxlofe5DI104TcCsZJCpydGJcVuESP+wgq0D3+0jbroh9hQbN1\n9UF1VKiX0e0h5I8qeQ9NgoMHWYmXjutWhl4n+PpSydEQh7UcIYgsX00uJhPTNWil\ne4i+22Z+QXnzb1+5hPjrD0folvFY4f0OtY64ga8qy5qvConUVhRNiU6lerEJXqA4\nzvPU2MsDsqEMdo30U8X0DJFQTUfOU0WoadBP1Q8jEjqkWMx5ixVUbf95YX2XujoE\njYveYeFekR0Z5JE1ysYepWueuUjEef7N+cfAA2ubJSbXGmQ0YwZl6gcFtJR8+HGA\ncVVzJW6zAgMBAAECggEAIxgE17LYQjn+9VF83yKmi0yFXO5w6UBXf5G37riY5FPr\n9OA0SXwGScO5VT14q0DikPJ7Go7suIn1h5k8WPXmQhVvvhJwszmANns18b2G8Oeb\nOmjoXiagM/Zwe1Vs8DbdydssytfvD4Dti1npPRZkn0wtIgLA7ZwU51jKvsj5OXuH\nnuDyPs1p+llcUQq6jkFKe/TWxp5CGmOVHN7o20/pdM+uwoATUzidnBTv+m8fLs4D\nB/rRm2UzMy1bArZK7RL7PDLIaX7vBdTROjk2MIZh+Rheo16GrwyaNiFl03hzIK1O\n2pCOEaa3XD0+Zn7j+u8iN7x3M4lSP1aUEB3+CwxuTQKBgQD0tU8wFhGgFgKMp2Jp\nbyN9wFsG/CeUe8dSZGXft6eOvtXUrM+30oGX1tz/gOv83gMoR3tLb5C0wpT960KO\nlMt55UGGIjHtzGe6PykRz2opbb2VRTuaNjANVfGlxiuepJChX3ukr3GkhVOQBdQ7\nnSRYVQdR2k90Q69CDk3fzuPF7wKBgQDnDZt90yiDnNi5AqckC91zG7t+dYOfH+Uf\neo6sZBJ5kx7dWzfrjKAYcFaYJ+DKwyX4bgz50HoT75ziQRAa1Bhuk8pVg/4yl33v\nyN9fKIheI0mpJdF9SKjQZASXkh1tIUPnt37fBl9hmxIkU4wJpP8adStad/8fP7G0\nU7cRKv/HfQKBgQDrJzhbmzmAvuXgSBGYBAb1Ft3ijnlyhKf8EyKao5/O2rAdWZua\nqB2EziM9HKSqMKaUFGz1Btbl/X6zq1ogLfiCwL4AqeeU/rJHFd7fkJQSD7T5NriZ\n7qyqhAZdKVxNbRLXICxvC3GHid/NLOzQBKgigkMwczubHFfUgG5xPh0/3QKBgQCY\nSgO+vzro5KyD5Re9ToS7pf/Crjn+28rtIJ6BScRTlYC2bbVB8AJlmUW6LC6h9lZE\nlGTBE4QjN7+z8SZoSHuCBq9KBiG5vtgm/8MauWCIi8G1V1Pou8do80ODk68Jiu9y\n/yMEZPLhJpCimN6oTLRIAAp/KrBhLF44eSUkj67fEQKBgQCeuybLN0HHe13fYdzC\n/vkd/OoHhKjVlX2W1bKT9dDsBXw63vKwLKgKuGoqrVXcmlRqaERy13OmotjnAw7w\nW7Kv86wj8OyNSJ9VVwB/VhhWIcrddR4OR0WIwVxSQWYxFB02GvQTz7RSOc5myyVC\n/2l6MesGFtW8ch5fdLI+29VTxw==\n-----END PRIVATE KEY-----\n",
                                                       "client_email": "tbapreprocessing@theta-byte-342416.iam.gserviceaccount.com",
                                                       "client_id": "110866838631585602751",
                                                       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                                       "token_uri": "https://oauth2.googleapis.com/token",
                                                       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                                                       "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tbapreprocessing%40theta-byte-342416.iam.gserviceaccount.com"})
    kubeflow_storage_bucket = client.get_bucket('theta-byte-342416-kubeflowpipelines-default', timeout=3600)
    import google.api_core.exceptions as gex

    while len(event_ids) > 0:

        events_to_retry = []

        for individual_event_id in event_ids:
            try:
                grabMatches(individual_event_id, kubeflow_storage_bucket)
            except gex.ServiceUnavailable:
                events_to_retry.append(individual_event_id)

        event_ids = events_to_retry

    video_keys_dir = 'video_keys/'

    return video_keys_dir


if __name__ == "__main__":
    grab_matches_for_events('2019zhrcc')
