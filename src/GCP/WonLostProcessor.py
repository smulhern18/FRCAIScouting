from google.cloud import bigquery, storage
import base64, json, os, ast
import pandas as pd

serviceAccount = {"type": "service_account", "project_id": "theta-byte-342416",
                                                       "private_key_id": "3bb0f4e92c48f894e7bb023330fed3247759f1a8",
                                                       "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDc3JxLdqz4mCbT\nNSRQFMosWaXKLpTxlofe5DI104TcCsZJCpydGJcVuESP+wgq0D3+0jbroh9hQbN1\n9UF1VKiX0e0h5I8qeQ9NgoMHWYmXjutWhl4n+PpSydEQh7UcIYgsX00uJhPTNWil\ne4i+22Z+QXnzb1+5hPjrD0folvFY4f0OtY64ga8qy5qvConUVhRNiU6lerEJXqA4\nzvPU2MsDsqEMdo30U8X0DJFQTUfOU0WoadBP1Q8jEjqkWMx5ixVUbf95YX2XujoE\njYveYeFekR0Z5JE1ysYepWueuUjEef7N+cfAA2ubJSbXGmQ0YwZl6gcFtJR8+HGA\ncVVzJW6zAgMBAAECggEAIxgE17LYQjn+9VF83yKmi0yFXO5w6UBXf5G37riY5FPr\n9OA0SXwGScO5VT14q0DikPJ7Go7suIn1h5k8WPXmQhVvvhJwszmANns18b2G8Oeb\nOmjoXiagM/Zwe1Vs8DbdydssytfvD4Dti1npPRZkn0wtIgLA7ZwU51jKvsj5OXuH\nnuDyPs1p+llcUQq6jkFKe/TWxp5CGmOVHN7o20/pdM+uwoATUzidnBTv+m8fLs4D\nB/rRm2UzMy1bArZK7RL7PDLIaX7vBdTROjk2MIZh+Rheo16GrwyaNiFl03hzIK1O\n2pCOEaa3XD0+Zn7j+u8iN7x3M4lSP1aUEB3+CwxuTQKBgQD0tU8wFhGgFgKMp2Jp\nbyN9wFsG/CeUe8dSZGXft6eOvtXUrM+30oGX1tz/gOv83gMoR3tLb5C0wpT960KO\nlMt55UGGIjHtzGe6PykRz2opbb2VRTuaNjANVfGlxiuepJChX3ukr3GkhVOQBdQ7\nnSRYVQdR2k90Q69CDk3fzuPF7wKBgQDnDZt90yiDnNi5AqckC91zG7t+dYOfH+Uf\neo6sZBJ5kx7dWzfrjKAYcFaYJ+DKwyX4bgz50HoT75ziQRAa1Bhuk8pVg/4yl33v\nyN9fKIheI0mpJdF9SKjQZASXkh1tIUPnt37fBl9hmxIkU4wJpP8adStad/8fP7G0\nU7cRKv/HfQKBgQDrJzhbmzmAvuXgSBGYBAb1Ft3ijnlyhKf8EyKao5/O2rAdWZua\nqB2EziM9HKSqMKaUFGz1Btbl/X6zq1ogLfiCwL4AqeeU/rJHFd7fkJQSD7T5NriZ\n7qyqhAZdKVxNbRLXICxvC3GHid/NLOzQBKgigkMwczubHFfUgG5xPh0/3QKBgQCY\nSgO+vzro5KyD5Re9ToS7pf/Crjn+28rtIJ6BScRTlYC2bbVB8AJlmUW6LC6h9lZE\nlGTBE4QjN7+z8SZoSHuCBq9KBiG5vtgm/8MauWCIi8G1V1Pou8do80ODk68Jiu9y\n/yMEZPLhJpCimN6oTLRIAAp/KrBhLF44eSUkj67fEQKBgQCeuybLN0HHe13fYdzC\n/vkd/OoHhKjVlX2W1bKT9dDsBXw63vKwLKgKuGoqrVXcmlRqaERy13OmotjnAw7w\nW7Kv86wj8OyNSJ9VVwB/VhhWIcrddR4OR0WIwVxSQWYxFB02GvQTz7RSOc5myyVC\n/2l6MesGFtW8ch5fdLI+29VTxw==\n-----END PRIVATE KEY-----\n",
                                                       "client_email": "tbapreprocessing@theta-byte-342416.iam.gserviceaccount.com",
                                                       "client_id": "110866838631585602751",
                                                       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                                       "token_uri": "https://oauth2.googleapis.com/token",
                                                       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                                                       "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tbapreprocessing%40theta-byte-342416.iam.gserviceaccount.com"}

def computeWinLost(matchName):
    mtype = os.path.basename(matchName).split('_')[-1]
    stclient = storage.Client.from_service_account_info(serviceAccount)
    bqclient = bigquery.Client.from_service_account_info(serviceAccount)
    for blob in stclient.list_blobs('theta-byte-342416-kubeflowpipelines-default', prefix=matchName):
        # Get data for match
        event_info = blob.download_as_string().decode("utf-8") 
        event_info = ast.literal_eval(event_info)
        alliances = event_info['alliances']
        _, year, competition, match = matchName.split('/')
        # Get blue team scores from bigquery
        query_job = bqclient.query(
            f'SELECT Traditional_Scoring_High,Traditional_Scoring_Low,Technical_Scoring,Autonomous_Scoring,Endgame,Fouls,Defense FROM `theta-byte-342416.unified.competitions` WHERE (Competition="{competition}" AND (Robot="{alliances["blue"]["team_keys"][0]}" OR Robot="{alliances["blue"]["team_keys"][1]}" OR Robot="{alliances["blue"]["team_keys"][2]}"))'
        )
        stats = list(query_job.result())
        if (len(stats) != 3):  raise ValueError(f'[{matchName}] Did not find 3 teams, but {len(stats)}: {", ".join(stats)}')
        blue_keys = ['Blue_Traditional_Scoring_High','Blue_Traditional_Scoring_Low','Blue_Technical_Scoring','Blue_Autonomous_Scoring','Blue_Endgame','Blue_Fouls','Blue_Defense']
        blue = [sum(x) for x in zip(stats[0], stats[1])]
        blue = [sum(x) for x in zip(blue, stats[2])]
        blue = [x / 3 for x in blue]
        kvb = dict(zip(blue_keys, blue))
        # Get red team scores from bigquery
        query_job = bqclient.query(
            f'SELECT Traditional_Scoring_High,Traditional_Scoring_Low,Technical_Scoring,Autonomous_Scoring,Endgame,Fouls,Defense FROM `theta-byte-342416.unified.competitions` WHERE (Competition="{competition}" AND (Robot="{alliances["red"]["team_keys"][0]}" OR Robot="{alliances["red"]["team_keys"][1]}" OR Robot="{alliances["red"]["team_keys"][2]}"))'
        )
        stats = list(query_job.result())
        if (len(stats) != 3):  raise ValueError(f'[{matchName}] Did not find 3 teams, but {len(stats)}: {", ".join(stats)}')
        red_keys = ['Red_Traditional_Scoring_High','Red_Traditional_Scoring_Low','Red_Technical_Scoring','Red_Autonomous_Scoring','Red_Endgame','Red_Fouls','Red_Defense']
        red = [sum(x) for x in zip(stats[0], stats[1])]
        red = [sum(x) for x in zip(red, stats[2])]
        red = [x / 3 for x in red]
        kvr = dict(zip(red_keys, red))
        res = {
            'year': year, 'competition': competition, 'match': match, 'mtype': mtype,
            'bscore': alliances['blue']['score'],
            'rscore': alliances['red']['score'],
            'blue_won': int(alliances['blue']['score'] > alliances['red']['score']),
            'red_won': int(alliances['red']['score'] > alliances['blue']['score'])
        }
        res.update(kvb)
        res.update(kvr)
        job = bqclient.load_table_from_dataframe(pd.DataFrame(data=[res]), f'theta-byte-342416.wonlost.{os.path.basename(matchName)}')

def pubsub_entry(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    request_json = json.loads(pubsub_message)
    EVENT_NAME = request_json['MATCH_NAME']
    computeWinLost(EVENT_NAME)
    return 'Computed correctly', 200


# if __name__ == '__main__':
#     computeWinLost('pulled_matches/2018/2018ohmv/2018ohmv_qm7')