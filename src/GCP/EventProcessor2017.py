from google.cloud import storage
import pandas as pd
import ast
import logging
def process_2017(eventname: str, serviceAccount) -> dict:
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
        except: continue
    
    col_names = ['Robot','Traditional_Scoring_High','Traditional_Scoring_Low','Technical_Scoring','Autonomous_Scoring','Endgame','Fouls','Defense']
    data_2017 = pd.DataFrame(columns = col_names)
    for match in range(0,len(b1s)):
        try:
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
        except: continue
    for stat in data_2017:
        if stat != 'Robot':
            data_2017[stat] = data_2017[stat].astype('float64')

    grouped_2017 = data_2017.groupby(by='Robot').mean()
    for stat in grouped_2017.columns:
        grouped_2017[stat] = grouped_2017[stat]/3
    return grouped_2017