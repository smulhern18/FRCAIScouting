from google.cloud import storage
import pandas as pd
import ast, logging

def process_2018(eventname: str, serviceAccount) -> dict:
    src_path = 'pulled_matches/2018/'

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
        try:
            d = ast.literal_eval(blob.download_as_string().decode('utf-8'))
            if ('alliances' not in d or 'score_breakdown' not in d):
                logging.error(f'Incomplete match')
                continue

            b1s.append(d.get('alliances').get('blue').get('team_keys')[0])
            b2s.append(d.get('alliances').get('blue').get('team_keys')[1])
            b3s.append(d.get('alliances').get('blue').get('team_keys')[2])
            r1s.append(d.get('alliances').get('red').get('team_keys')[0])
            r2s.append(d.get('alliances').get('red').get('team_keys')[1])
            r3s.append(d.get('alliances').get('red').get('team_keys')[2])

            bautoT.append(d.get('score_breakdown').get('blue').get('autoPoints'))
            rautoT.append(d.get('score_breakdown').get('red').get('autoPoints'))

            end_dict = {'Parking': 5,'Climbing': 30, 'Levitate': 5, 'None': 0}
            bendG.append([end_dict.get(d.get('score_breakdown').get('blue').get('endgameRobot1')),  end_dict.get(d.get('score_breakdown').get('blue').get('endgameRobot2')), end_dict.get(d.get('score_breakdown').get('blue').get('endgameRobot3'))])
            rendG.append([end_dict.get(d.get('score_breakdown').get('red').get('endgameRobot1')),  end_dict.get(d.get('score_breakdown').get('red').get('endgameRobot2')), end_dict.get(d.get('score_breakdown').get('red').get('endgameRobot3'))])

            bfoulsO.append(-d.get('score_breakdown').get('red').get('foulPoints'))
            rfoulsO.append(-d.get('score_breakdown').get('blue').get('foulPoints'))

            bdefO.append(-d.get('score_breakdown').get('red').get('totalPoints'))
            rdefO.append(-d.get('score_breakdown').get('blue').get('totalPoints'))

            bTradSH.append(d.get('score_breakdown').get('blue').get('teleopScaleOwnershipSec') - d.get('score_breakdown').get('blue').get('teleopScaleForceSec'))
            rTradSH.append(d.get('score_breakdown').get('red').get('teleopScaleOwnershipSec') - d.get('score_breakdown').get('red').get('teleopScaleForceSec'))

            bTradSL.append(d.get('score_breakdown').get('blue').get('teleopSwitchOwnershipSec') - d.get('score_breakdown').get('blue').get('teleopSwitchForceSec'))
            rTradSL.append(d.get('score_breakdown').get('red').get('teleopSwitchOwnershipSec') - d.get('score_breakdown').get('red').get('teleopSwitchForceSec'))

            bTechS.append(d.get('score_breakdown').get('blue').get('teleopScaleBoostSec') + d.get('score_breakdown').get('blue').get('teleopSwitchBoostSec') + d.get('score_breakdown').get('blue').get('teleopScaleForceSec') + d.get('score_breakdown').get('blue').get('teleopSwitchForceSec') + d.get('score_breakdown').get('blue').get('vaultPoints') + d.get('score_breakdown').get('blue').get('vaultLevitatePlayed')*30)
            rTechS.append(d.get('score_breakdown').get('red').get('teleopScaleBoostSec') + d.get('score_breakdown').get('red').get('teleopSwitchBoostSec') + d.get('score_breakdown').get('red').get('teleopScaleForceSec') + d.get('score_breakdown').get('red').get('teleopSwitchForceSec') + d.get('score_breakdown').get('red').get('vaultPoints') + d.get('score_breakdown').get('red').get('vaultLevitatePlayed')*30)
        except: continue
    col_names = ['Robot','Traditional_Scoring_High','Traditional_Scoring_Low','Technical_Scoring','Autonomous_Scoring','Endgame','Fouls','Defense']
    data_2018 = pd.DataFrame(columns = col_names)
    for match in range(0,len(b1s)):
        try:
            data = [b1s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match][0],bfoulsO[match],bdefO[match]]
            data_2018 = data_2018.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
            data = [b2s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match][1],bfoulsO[match],bdefO[match]]
            data_2018 = data_2018.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
            data = [b3s[match],bTradSH[match],bTradSL[match],bTechS[match],bautoT[match],bendG[match][2],bfoulsO[match],bdefO[match]]
            data_2018 = data_2018.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
            data = [r1s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match][0],rfoulsO[match],rdefO[match]]
            data_2018 = data_2018.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
            data = [r2s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match][1],rfoulsO[match],rdefO[match]]
            data_2018 = data_2018.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
            data = [r3s[match],rTradSH[match],rTradSL[match],rTechS[match],rautoT[match],rendG[match][2],rfoulsO[match],rdefO[match]]
            data_2018 = data_2018.append(pd.DataFrame([data],columns = col_names), ignore_index = True)
        except: continue
    
    for stat in data_2018:
        if stat != 'Robot':
            data_2018[stat] = data_2018[stat].astype('float64')

    grouped_2018 = data_2018.groupby(by = 'Robot').mean()
    for stat in grouped_2018.columns:
        if stat != 'Endgame':
            grouped_2018[stat] = grouped_2018[stat]/3

    return grouped_2018
