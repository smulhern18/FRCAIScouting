
def process_2017(eventname: str) -> dict:

    import pandas as pd
    import ast

    src_path = 'pulled_matches/2017/'

    b1s = []
    b2s = []
    b3s = []
    r1s = []
    r2s = []
    r3s = []
    bautoT = []
    rautoT = []
    bendG = []
    rendG = []
    bfoulsO = []
    rfoulsO = []
    bdefO = []
    rdefO = []
    bTradSH = []
    rTradSH = []
    bTradSL = []
    rTradSL = []
    bTechS = []
    rTechS = []

    from google.cloud import storage

    client = storage.Client.from_service_account_info({"type": "service_account", "project_id": "theta-byte-342416",
                                                       "private_key_id": "3bb0f4e92c48f894e7bb023330fed3247759f1a8",
                                                       "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDc3JxLdqz4mCbT\nNSRQFMosWaXKLpTxlofe5DI104TcCsZJCpydGJcVuESP+wgq0D3+0jbroh9hQbN1\n9UF1VKiX0e0h5I8qeQ9NgoMHWYmXjutWhl4n+PpSydEQh7UcIYgsX00uJhPTNWil\ne4i+22Z+QXnzb1+5hPjrD0folvFY4f0OtY64ga8qy5qvConUVhRNiU6lerEJXqA4\nzvPU2MsDsqEMdo30U8X0DJFQTUfOU0WoadBP1Q8jEjqkWMx5ixVUbf95YX2XujoE\njYveYeFekR0Z5JE1ysYepWueuUjEef7N+cfAA2ubJSbXGmQ0YwZl6gcFtJR8+HGA\ncVVzJW6zAgMBAAECggEAIxgE17LYQjn+9VF83yKmi0yFXO5w6UBXf5G37riY5FPr\n9OA0SXwGScO5VT14q0DikPJ7Go7suIn1h5k8WPXmQhVvvhJwszmANns18b2G8Oeb\nOmjoXiagM/Zwe1Vs8DbdydssytfvD4Dti1npPRZkn0wtIgLA7ZwU51jKvsj5OXuH\nnuDyPs1p+llcUQq6jkFKe/TWxp5CGmOVHN7o20/pdM+uwoATUzidnBTv+m8fLs4D\nB/rRm2UzMy1bArZK7RL7PDLIaX7vBdTROjk2MIZh+Rheo16GrwyaNiFl03hzIK1O\n2pCOEaa3XD0+Zn7j+u8iN7x3M4lSP1aUEB3+CwxuTQKBgQD0tU8wFhGgFgKMp2Jp\nbyN9wFsG/CeUe8dSZGXft6eOvtXUrM+30oGX1tz/gOv83gMoR3tLb5C0wpT960KO\nlMt55UGGIjHtzGe6PykRz2opbb2VRTuaNjANVfGlxiuepJChX3ukr3GkhVOQBdQ7\nnSRYVQdR2k90Q69CDk3fzuPF7wKBgQDnDZt90yiDnNi5AqckC91zG7t+dYOfH+Uf\neo6sZBJ5kx7dWzfrjKAYcFaYJ+DKwyX4bgz50HoT75ziQRAa1Bhuk8pVg/4yl33v\nyN9fKIheI0mpJdF9SKjQZASXkh1tIUPnt37fBl9hmxIkU4wJpP8adStad/8fP7G0\nU7cRKv/HfQKBgQDrJzhbmzmAvuXgSBGYBAb1Ft3ijnlyhKf8EyKao5/O2rAdWZua\nqB2EziM9HKSqMKaUFGz1Btbl/X6zq1ogLfiCwL4AqeeU/rJHFd7fkJQSD7T5NriZ\n7qyqhAZdKVxNbRLXICxvC3GHid/NLOzQBKgigkMwczubHFfUgG5xPh0/3QKBgQCY\nSgO+vzro5KyD5Re9ToS7pf/Crjn+28rtIJ6BScRTlYC2bbVB8AJlmUW6LC6h9lZE\nlGTBE4QjN7+z8SZoSHuCBq9KBiG5vtgm/8MauWCIi8G1V1Pou8do80ODk68Jiu9y\n/yMEZPLhJpCimN6oTLRIAAp/KrBhLF44eSUkj67fEQKBgQCeuybLN0HHe13fYdzC\n/vkd/OoHhKjVlX2W1bKT9dDsBXw63vKwLKgKuGoqrVXcmlRqaERy13OmotjnAw7w\nW7Kv86wj8OyNSJ9VVwB/VhhWIcrddR4OR0WIwVxSQWYxFB02GvQTz7RSOc5myyVC\n/2l6MesGFtW8ch5fdLI+29VTxw==\n-----END PRIVATE KEY-----\n",
                                                       "client_email": "tbapreprocessing@theta-byte-342416.iam.gserviceaccount.com",
                                                       "client_id": "110866838631585602751",
                                                       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                                                       "token_uri": "https://oauth2.googleapis.com/token",
                                                       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                                                       "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tbapreprocessing%40theta-byte-342416.iam.gserviceaccount.com"})

    src_path = src_path + eventname + '/'

    for blob in client.list_blobs('theta-byte-342416-kubeflowpipelines-default', prefix=src_path, timeout=3600):
        print(blob.name)
        
        d = ast.literal_eval(blob.download_as_string().decode('utf-8'))

        b1s.append(d.get('alliances').get('blue').get('team_keys')[0])
        b2s.append(d.get('alliances').get('blue').get('team_keys')[1])
        b3s.append(d.get('alliances').get('blue').get('team_keys')[2])
        r1s.append(d.get('alliances').get('red').get('team_keys')[0])
        r2s.append(d.get('alliances').get('red').get('team_keys')[1])
        r3s.append(d.get('alliances').get('red').get('team_keys')[2])
        bautoT.append(d.get('score_breakdown').get('blue').get('autoPoints'))
        rautoT.append(d.get('score_breakdown').get('red').get('autoPoints'))
        bendG.append(d.get('score_breakdown').get('blue').get('teleopTakeoffPoints'))
        rendG.append(d.get('score_breakdown').get('red').get('teleopTakeoffPoints'))
        bfoulsO.append(-d.get('score_breakdown').get('red').get('foulPoints'))
        rfoulsO.append(-d.get('score_breakdown').get('blue').get('foulPoints'))
        bdefO.append(-d.get('score_breakdown').get('red').get('totalPoints'))
        rdefO.append(-d.get('score_breakdown').get('blue').get('totalPoints'))
        bTradSH.append(d.get('score_breakdown').get('blue').get('teleopFuelHigh')/3 + d.get('score_breakdown').get('blue').get('kPaBonusPoints'))
        rTradSH.append(d.get('score_breakdown').get('red').get('teleopFuelHigh')/3 + d.get('score_breakdown').get('red').get('kPaBonusPoints'))
        bTradSL.append(d.get('score_breakdown').get('blue').get('teleopFuelLow')/6 + d.get('score_breakdown').get('blue').get('kPaBonusPoints')/2)
        rTradSL.append(d.get('score_breakdown').get('red').get('teleopFuelLow')/6 + d.get('score_breakdown').get('blue').get('kPaBonusPoints')/2)
        bTechS.append(d.get('score_breakdown').get('blue').get('rotor1Engaged')*40 + d.get('score_breakdown').get('blue').get('rotor2Engaged')*40/2 + d.get('score_breakdown').get('blue').get('rotor1Engaged')*40/4 + d.get('score_breakdown').get('blue').get('rotor1Engaged')*40/5)
        rTechS.append(d.get('score_breakdown').get('red').get('rotor1Engaged')*40 + d.get('score_breakdown').get('red').get('rotor2Engaged')*40/2 + d.get('score_breakdown').get('red').get('rotor1Engaged')*40/4 + d.get('score_breakdown').get('red').get('rotor1Engaged')*40/5)

    col_names = ['Robot','Traditional Scoring High','Traditional Scoring Low','Technical Scoring','Autonomous Scoring','Endgame','Fouls','Defense']
    data_2017 = pd.DataFrame(columns = col_names)
    for match in range(0,len(b1s)):
        data = [b1s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match],bfoulsO[match],bdefO[match]]
        data_2017 = data_2017.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [b2s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match],bfoulsO[match],bdefO[match]]
        data_2017 = data_2017.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [b3s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match],bfoulsO[match],bdefO[match]]
        data_2017 = data_2017.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [r1s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match],rfoulsO[match],rdefO[match]]
        data_2017 = data_2017.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [r2s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match],rfoulsO[match],rdefO[match]]
        data_2017 = data_2017.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [r3s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match],rfoulsO[match],rdefO[match]]
        data_2017 = data_2017.append(pd.DataFrame([data],columns = col_names), ignore_index = True)

    for stat in data_2017:
        if stat != 'Robot':
            data_2017[stat] = data_2017[stat].astype('float64')

    grouped_2017 = data_2017.groupby(by='Robot').mean()
    for stat in grouped_2017.columns:
        grouped_2017[stat] = grouped_2017[stat]/3

    print(grouped_2017)
    return grouped_2017.to_dict()


if __name__=="__main__":
    print(process_2017('2017abca'))
