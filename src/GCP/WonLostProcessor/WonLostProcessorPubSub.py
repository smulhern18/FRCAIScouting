# theta-byte-342416-kubeflowpipelines-default/pulled_matches/2017/2017abca

from google.cloud import storage
from concurrent import futures
from google.cloud import pubsub_v1
import os, json
from tqdm import tqdm

key_path = 'disco-catcher-346421-20425fa8f8d7.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

serviceAccount = {  "type": "service_account", "project_id": "theta-byte-342416",
                    "private_key_id": "3bb0f4e92c48f894e7bb023330fed3247759f1a8",
                    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDc3JxLdqz4mCbT\nNSRQFMosWaXKLpTxlofe5DI104TcCsZJCpydGJcVuESP+wgq0D3+0jbroh9hQbN1\n9UF1VKiX0e0h5I8qeQ9NgoMHWYmXjutWhl4n+PpSydEQh7UcIYgsX00uJhPTNWil\ne4i+22Z+QXnzb1+5hPjrD0folvFY4f0OtY64ga8qy5qvConUVhRNiU6lerEJXqA4\nzvPU2MsDsqEMdo30U8X0DJFQTUfOU0WoadBP1Q8jEjqkWMx5ixVUbf95YX2XujoE\njYveYeFekR0Z5JE1ysYepWueuUjEef7N+cfAA2ubJSbXGmQ0YwZl6gcFtJR8+HGA\ncVVzJW6zAgMBAAECggEAIxgE17LYQjn+9VF83yKmi0yFXO5w6UBXf5G37riY5FPr\n9OA0SXwGScO5VT14q0DikPJ7Go7suIn1h5k8WPXmQhVvvhJwszmANns18b2G8Oeb\nOmjoXiagM/Zwe1Vs8DbdydssytfvD4Dti1npPRZkn0wtIgLA7ZwU51jKvsj5OXuH\nnuDyPs1p+llcUQq6jkFKe/TWxp5CGmOVHN7o20/pdM+uwoATUzidnBTv+m8fLs4D\nB/rRm2UzMy1bArZK7RL7PDLIaX7vBdTROjk2MIZh+Rheo16GrwyaNiFl03hzIK1O\n2pCOEaa3XD0+Zn7j+u8iN7x3M4lSP1aUEB3+CwxuTQKBgQD0tU8wFhGgFgKMp2Jp\nbyN9wFsG/CeUe8dSZGXft6eOvtXUrM+30oGX1tz/gOv83gMoR3tLb5C0wpT960KO\nlMt55UGGIjHtzGe6PykRz2opbb2VRTuaNjANVfGlxiuepJChX3ukr3GkhVOQBdQ7\nnSRYVQdR2k90Q69CDk3fzuPF7wKBgQDnDZt90yiDnNi5AqckC91zG7t+dYOfH+Uf\neo6sZBJ5kx7dWzfrjKAYcFaYJ+DKwyX4bgz50HoT75ziQRAa1Bhuk8pVg/4yl33v\nyN9fKIheI0mpJdF9SKjQZASXkh1tIUPnt37fBl9hmxIkU4wJpP8adStad/8fP7G0\nU7cRKv/HfQKBgQDrJzhbmzmAvuXgSBGYBAb1Ft3ijnlyhKf8EyKao5/O2rAdWZua\nqB2EziM9HKSqMKaUFGz1Btbl/X6zq1ogLfiCwL4AqeeU/rJHFd7fkJQSD7T5NriZ\n7qyqhAZdKVxNbRLXICxvC3GHid/NLOzQBKgigkMwczubHFfUgG5xPh0/3QKBgQCY\nSgO+vzro5KyD5Re9ToS7pf/Crjn+28rtIJ6BScRTlYC2bbVB8AJlmUW6LC6h9lZE\nlGTBE4QjN7+z8SZoSHuCBq9KBiG5vtgm/8MauWCIi8G1V1Pou8do80ODk68Jiu9y\n/yMEZPLhJpCimN6oTLRIAAp/KrBhLF44eSUkj67fEQKBgQCeuybLN0HHe13fYdzC\n/vkd/OoHhKjVlX2W1bKT9dDsBXw63vKwLKgKuGoqrVXcmlRqaERy13OmotjnAw7w\nW7Kv86wj8OyNSJ9VVwB/VhhWIcrddR4OR0WIwVxSQWYxFB02GvQTz7RSOc5myyVC\n/2l6MesGFtW8ch5fdLI+29VTxw==\n-----END PRIVATE KEY-----\n",
                    "client_email": "tbapreprocessing@theta-byte-342416.iam.gserviceaccount.com",
                    "client_id": "110866838631585602751",
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tbapreprocessing%40theta-byte-342416.iam.gserviceaccount.com"}


publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('disco-catcher-346421', 'WonLostProcessorTopic')
publish_futures = []

client = storage.Client.from_service_account_info(serviceAccount)
import time
count = 0
for year in tqdm([2017, 2018, 2019]):
    for match in tqdm(client.list_blobs('theta-byte-342416-kubeflowpipelines-default', prefix=f'pulled_matches/{year}/')): 
        if len(match.name.split('/')) != 4: continue
        mtype = os.path.basename(match.name).split('_')[-1]
        if mtype[:2] == 'qf' or mtype[:2] == 'qm' or mtype[:2] == 'sf' or mtype[:1] == 'f':
            payload = json.dumps({
                "MATCH_NAME": match.name
            })
            # When you publish a message, the client returns a future.
            publish_future = publisher.publish(topic_path, payload.encode("utf-8"))
            # Non-blocking. Publish failures are handled in the callback function.
            publish_futures.append(publish_future)
            count += 1
            if (count % 30000 == 0):                    
                # Wait for all the publish futures to resolve before exiting.
                futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)
                # print(f"Published messages with error handler to {topic_path}.")
                print('Publishing')
                time.sleep(9 * 60) # 9 minutes wait

print(count)
print('All done')