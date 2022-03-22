from google.cloud import storage
import pandas as pd
import ast

def process_2019(eventname: str, serviceAccount) -> dict:
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

    client = storage.Client.from_service_account_info(serviceAccount)

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

    col_names = ['Robot','Traditional_Scoring_High','Traditional_Scoring_Low','Technical_Scoring','Autonomous_Scoring','Endgame','Fouls','Defense']
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

    return grouped_2019