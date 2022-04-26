
def process_2019(eventname: str) -> dict:

    import pandas as pd
    import ast

    src_path = 'pulled_matches/2019/'

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
        d = ast.literal_eval(blob.download_as_string().decode('utf-8'))

        b1s.append(d.get('alliances').get('blue').get('team_keys')[0])
        b2s.append(d.get('alliances').get('blue').get('team_keys')[1])
        b3s.append(d.get('alliances').get('blue').get('team_keys')[2])
        r1s.append(d.get('alliances').get('red').get('team_keys')[0])
        r2s.append(d.get('alliances').get('red').get('team_keys')[1])
        r3s.append(d.get('alliances').get('red').get('team_keys')[2])

        bautoT.append(d.get('score_breakdown').get('blue').get('autoPoints'))
        rautoT.append(d.get('score_breakdown').get('red').get('autoPoints'))

        end_dict = {'HabLevel3': 12,'HabLevel2': 6, 'HabLevel1': 3, 'None': 0}
        bendG.append([end_dict.get(d.get('score_breakdown').get('blue').get('endgameRobot1')),  end_dict.get(d.get('score_breakdown').get('blue').get('endgameRobot2')), end_dict.get(d.get('score_breakdown').get('blue').get('endgameRobot3'))])
        rendG.append([end_dict.get(d.get('score_breakdown').get('red').get('endgameRobot1')),  end_dict.get(d.get('score_breakdown').get('red').get('endgameRobot2')), end_dict.get(d.get('score_breakdown').get('red').get('endgameRobot3'))])

        bfoulsO.append(-d.get('score_breakdown').get('red').get('foulPoints'))
        rfoulsO.append(-d.get('score_breakdown').get('blue').get('foulPoints'))

        bdefO.append(-d.get('score_breakdown').get('red').get('totalPoints'))
        rdefO.append(-d.get('score_breakdown').get('blue').get('totalPoints'))

        panel_dict = {'PanelAndCargo': 2, 'Panel': 2, 'None': 0}
        cargo_dict = {'PanelAndCargo': 3, 'Panel': 0, 'None': 0}

        bTradSH.append(cargo_dict.get(d.get('score_breakdown').get('blue').get('lowLeftRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('lowRightRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('lowLeftRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('lowRightRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('midLeftRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('midLeftRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('midRightRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('midRightRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('topLeftRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('topLeftRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('topRightRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('topRightRocketNear')))
        rTradSH.append(cargo_dict.get(d.get('score_breakdown').get('red').get('lowLeftRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('red').get('lowRightRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('red').get('lowLeftRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('red').get('lowRightRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('red').get('midLeftRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('red').get('midLeftRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('red').get('midRightRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('red').get('midRightRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('red').get('topLeftRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('red').get('topLeftRocketNear')) + cargo_dict.get(d.get('score_breakdown').get('red').get('topRightRocketFar')) + cargo_dict.get(d.get('score_breakdown').get('red').get('topRightRocketNear')))

        bTradSL.append(cargo_dict.get(d.get('score_breakdown').get('blue').get('bay1')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay2')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay3')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay4')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay5')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay6')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay7')) + cargo_dict.get(d.get('score_breakdown').get('blue').get('bay8')))
        rTradSL.append(cargo_dict.get(d.get('score_breakdown').get('red').get('bay1')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay2')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay3')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay4')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay5')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay6')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay7')) + cargo_dict.get(d.get('score_breakdown').get('red').get('bay8')))

        bTechS.append(panel_dict.get(d.get('score_breakdown').get('blue').get('bay1')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay2')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay3')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay4')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay5')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay6')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay7')) + panel_dict.get(d.get('score_breakdown').get('blue').get('bay8')) + panel_dict.get(d.get('score_breakdown').get('blue').get('lowLeftRocketFar')) + panel_dict.get(d.get('score_breakdown').get('blue').get('lowRightRocketFar')) + panel_dict.get(d.get('score_breakdown').get('blue').get('lowLeftRocketNear')) + panel_dict.get(d.get('score_breakdown').get('blue').get('lowRightRocketNear')) + panel_dict.get(d.get('score_breakdown').get('blue').get('midLeftRocketFar')) + panel_dict.get(d.get('score_breakdown').get('blue').get('midLeftRocketNear')) + panel_dict.get(d.get('score_breakdown').get('blue').get('midRightRocketFar')) + panel_dict.get(d.get('score_breakdown').get('blue').get('midRightRocketNear')) + panel_dict.get(d.get('score_breakdown').get('blue').get('topLeftRocketFar')) + panel_dict.get(d.get('score_breakdown').get('blue').get('topLeftRocketNear')) + panel_dict.get(d.get('score_breakdown').get('blue').get('topRightRocketFar')) + panel_dict.get(d.get('score_breakdown').get('blue').get('topRightRocketNear'))  - (int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay1')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay2')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay3')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay4')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay5')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay6')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay7')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('blue').get('preMatchBay8')) or 0)))
        rTechS.append(panel_dict.get(d.get('score_breakdown').get('red').get('bay1')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay2')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay3')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay4')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay5')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay6')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay7')) + panel_dict.get(d.get('score_breakdown').get('red').get('bay8')) + panel_dict.get(d.get('score_breakdown').get('red').get('lowLeftRocketFar')) + panel_dict.get(d.get('score_breakdown').get('red').get('lowRightRocketFar')) + panel_dict.get(d.get('score_breakdown').get('red').get('lowLeftRocketNear')) + panel_dict.get(d.get('score_breakdown').get('red').get('lowRightRocketNear')) + panel_dict.get(d.get('score_breakdown').get('red').get('midLeftRocketFar')) + panel_dict.get(d.get('score_breakdown').get('red').get('midLeftRocketNear')) + panel_dict.get(d.get('score_breakdown').get('red').get('midRightRocketFar')) + panel_dict.get(d.get('score_breakdown').get('red').get('midRightRocketNear')) + panel_dict.get(d.get('score_breakdown').get('red').get('topLeftRocketFar')) + panel_dict.get(d.get('score_breakdown').get('red').get('topLeftRocketNear')) + panel_dict.get(d.get('score_breakdown').get('red').get('topRightRocketFar')) + panel_dict.get(d.get('score_breakdown').get('red').get('topRightRocketNear'))  - (int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay1')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay2')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay3')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay4')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay5')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay6')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay7')) or 0) + int(panel_dict.get(d.get('score_breakdown').get('red').get('preMatchBay8')) or 0)))

    col_names = ['Robot','Traditional Scoring High','Traditional Scoring Low','Technical Scoring','Autonomous Scoring','Endgame','Fouls','Defense']
    data_2019 = pd.DataFrame(columns = col_names)
    for match in range(0,len(b1s)):
        data = [b1s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match][0],bfoulsO[match],bdefO[match]]
        data_2019 = data_2019.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [b2s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match][1],bfoulsO[match],bdefO[match]]
        data_2019 = data_2019.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [b3s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match][2],bfoulsO[match],bdefO[match]]
        data_2019 = data_2019.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [r1s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match][0],rfoulsO[match],rdefO[match]]
        data_2019 = data_2019.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [r2s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match][1],rfoulsO[match],rdefO[match]]
        data_2019 = data_2019.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        data = [r3s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match][2],rfoulsO[match],rdefO[match]]
        data_2019 = data_2019.append(pd.DataFrame([data],columns = col_names), ignore_index = True)

    for stat in data_2019:
        if stat != 'Robot':
            data_2019[stat] = data_2019[stat].astype('float64')

    grouped_2019 = data_2019.groupby(by = 'Robot').mean()
    for stat in grouped_2019.columns:
        if stat != 'Endgame':
            grouped_2019[stat] = grouped_2019[stat]/3

    print(grouped_2019)
    return grouped_2019.to_dict()


if __name__=="__main__":
    print(process_2019('2019abca'))
