from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from app_methods import optimize
from models.predict import predict_probability
import json

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/compute/team/<string:team_num>/competition/<string:event_key>', methods=["GET"])
def compute(team_num, event_key):

    if 'frc' not in team_num:
        team_num = 'frc'+team_num

    competitions = pd.read_csv('TestProcessing/competitions.csv')

    comp = competitions[competitions['Competition'] == event_key]

    # Allocate strings
    tba_read_key = 'vSedKwbovtAcDcYzaAl0QjcYwox4xXxC7r5b4zPpNS3X9BC6khgVlGhR3Fox2tYR'
    format_str = f'https://www.thebluealliance.com/api/v3/event/{event_key}/rankings'

    import requests

    event_rankings = requests.get(url=format_str, headers={'X-TBA-Auth-Key': tba_read_key})

    rankings_json = event_rankings.json()['rankings']

    top_8 = ['', '', '', '', '', '', '', '']
    just_outside = ['', '', '', '', '', '', '', '']

    for element in rankings_json:
        for index in range(1, 17):
            if element['rank'] == index:
                if element['rank'] <= 8:
                    top_8[index-1] = element['team_key']
                elif element['rank'] <= 16:
                    just_outside[index-9] = element['team_key']

    optimized_alliances = optimize(top_8, just_outside, comp)

    return app.make_response(optimized_alliances)


@app.route('/won_lost/event/<string:event_key>', methods=["GET", "POST"])
def won_lost(event_key):
    alliances = json.loads(request.headers['Alliances'])

    seed1 = alliances['1']
    seed2 = alliances['2']
    seed3 = alliances['3']
    seed4 = alliances['4']
    seed5 = alliances['5']
    seed6 = alliances['6']
    seed7 = alliances['7']
    seed8 = alliances['8']

    data = pd.read_csv('../data/v1/robots.csv')
    data = data.loc[data["Competition"] == event_key]

    seed1 = data.loc[(data["Robot"] == seed1[0]) | (data["Robot"] == seed1[1]) | (data["Robot"] == seed1[2])]
    seed2 = data.loc[(data["Robot"] == seed2[0]) | (data["Robot"] == seed2[1]) | (data["Robot"] == seed2[2])]
    seed3 = data.loc[(data["Robot"] == seed3[0]) | (data["Robot"] == seed3[1]) | (data["Robot"] == seed3[2])]
    seed4 = data.loc[(data["Robot"] == seed4[0]) | (data["Robot"] == seed4[1]) | (data["Robot"] == seed4[2])]
    seed5 = data.loc[(data["Robot"] == seed5[0]) | (data["Robot"] == seed5[1]) | (data["Robot"] == seed5[2])]
    seed6 = data.loc[(data["Robot"] == seed6[0]) | (data["Robot"] == seed6[1]) | (data["Robot"] == seed6[2])]
    seed7 = data.loc[(data["Robot"] == seed7[0]) | (data["Robot"] == seed7[1]) | (data["Robot"] == seed7[2])]
    seed8 = data.loc[(data["Robot"] == seed8[0]) | (data["Robot"] == seed8[1]) | (data["Robot"] == seed8[2])]

    seed1 = \
        seed1[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed2 = \
        seed2[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed3 = \
        seed3[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed4 = \
        seed4[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed5 = \
        seed5[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed6 = \
        seed6[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed7 = \
        seed7[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()
    seed8 = \
        seed8[['Traditional_Scoring_High', 'Traditional_Scoring_Low', 'Technical_Scoring',
              'Autonomous_Scoring', 'Endgame', 'Fouls', 'Defense']].mean()

    qf1 = pd.DataFrame({
        'Blue_Traditional_Scoring_High': [seed8.Traditional_Scoring_High],
        'Blue_Traditional_Scoring_Low': [seed8.Traditional_Scoring_Low],
        'Blue_Technical_Scoring': [seed8.Technical_Scoring],
        'Blue_Autonomous_Scoring': [seed8.Autonomous_Scoring],
        'Blue_Endgame': [seed8.Endgame],
        'Blue_Fouls': [seed8.Fouls],
        'Blue_Defense': [seed8.Defense],
        'Red_Traditional_Scoring_High': [seed1.Traditional_Scoring_High],
        'Red_Traditional_Scoring_Low': [seed1.Traditional_Scoring_Low],
        'Red_Technical_Scoring': [seed1.Technical_Scoring],
        'Red_Autonomous_Scoring': [seed1.Autonomous_Scoring],
        'Red_Endgame': [seed1.Endgame],
        'Red_Fouls': [seed1.Fouls],
        'Red_Defense': [seed1.Defense],
    })

    qf2 = pd.DataFrame({
        'Blue_Traditional_Scoring_High': [seed5.Traditional_Scoring_High],
        'Blue_Traditional_Scoring_Low': [seed5.Traditional_Scoring_Low],
        'Blue_Technical_Scoring': [seed5.Technical_Scoring],
        'Blue_Autonomous_Scoring': [seed5.Autonomous_Scoring],
        'Blue_Endgame': [seed5.Endgame],
        'Blue_Fouls': [seed5.Fouls],
        'Blue_Defense': [seed5.Defense],
        'Red_Traditional_Scoring_High': [seed4.Traditional_Scoring_High],
        'Red_Traditional_Scoring_Low': [seed4.Traditional_Scoring_Low],
        'Red_Technical_Scoring': [seed4.Technical_Scoring],
        'Red_Autonomous_Scoring': [seed4.Autonomous_Scoring],
        'Red_Endgame': [seed4.Endgame],
        'Red_Fouls': [seed4.Fouls],
        'Red_Defense': [seed4.Defense],
    })

    qf3 = pd.DataFrame({
        'Blue_Traditional_Scoring_High': [seed6.Traditional_Scoring_High],
        'Blue_Traditional_Scoring_Low': [seed6.Traditional_Scoring_Low],
        'Blue_Technical_Scoring': [seed6.Technical_Scoring],
        'Blue_Autonomous_Scoring': [seed6.Autonomous_Scoring],
        'Blue_Endgame': [seed6.Endgame],
        'Blue_Fouls': [seed6.Fouls],
        'Blue_Defense': [seed6.Defense],
        'Red_Traditional_Scoring_High': [seed3.Traditional_Scoring_High],
        'Red_Traditional_Scoring_Low': [seed3.Traditional_Scoring_Low],
        'Red_Technical_Scoring': [seed3.Technical_Scoring],
        'Red_Autonomous_Scoring': [seed3.Autonomous_Scoring],
        'Red_Endgame': [seed3.Endgame],
        'Red_Fouls': [seed3.Fouls],
        'Red_Defense': [seed3.Defense],
    })

    qf4 = pd.DataFrame({
        'Blue_Traditional_Scoring_High': [seed7.Traditional_Scoring_High],
        'Blue_Traditional_Scoring_Low': [seed7.Traditional_Scoring_Low],
        'Blue_Technical_Scoring': [seed7.Technical_Scoring],
        'Blue_Autonomous_Scoring': [seed7.Autonomous_Scoring],
        'Blue_Endgame': [seed7.Endgame],
        'Blue_Fouls': [seed7.Fouls],
        'Blue_Defense': [seed7.Defense],
        'Red_Traditional_Scoring_High': [seed2.Traditional_Scoring_High],
        'Red_Traditional_Scoring_Low': [seed2.Traditional_Scoring_Low],
        'Red_Technical_Scoring': [seed2.Technical_Scoring],
        'Red_Autonomous_Scoring': [seed2.Autonomous_Scoring],
        'Red_Endgame': [seed2.Endgame],
        'Red_Fouls': [seed2.Fouls],
        'Red_Defense': [seed2.Defense],
    })

    sf1 = pd.DataFrame()
    sf2 = pd.DataFrame()
    f = pd.DataFrame()

    wonlost = {'qf': [[], [], [], []],
               'sf': [[], []],
               'f': [[]],
               'qf_probs': [[], [], [], []],
               'sf_probs': [[], []],
               'f_probs': [[]]
    }

    qf1_win = predict_probability(qf1)
    if qf1_win[0] > qf1_win[1]:
        wonlost['qf'][0] = alliances['1']
        sf1['Red_Traditional_Scoring_High'] = [seed1.Traditional_Scoring_High]
        sf1['Red_Traditional_Scoring_Low'] = [seed1.Traditional_Scoring_Low]
        sf1['Red_Technical_Scoring'] = [seed1.Technical_Scoring]
        sf1['Red_Autonomous_Scoring'] = [seed1.Autonomous_Scoring]
        sf1['Red_Endgame'] = [seed1.Endgame]
        sf1['Red_Fouls'] = [seed1.Fouls]
        sf1['Red_Defense'] = [seed1.Defense]
    else:
        wonlost['qf'][0] = alliances['8']
        sf1['Red_Traditional_Scoring_High'] = [seed8.Traditional_Scoring_High]
        sf1['Red_Traditional_Scoring_Low'] = [seed8.Traditional_Scoring_Low]
        sf1['Red_Technical_Scoring'] = [seed8.Technical_Scoring]
        sf1['Red_Autonomous_Scoring'] = [seed8.Autonomous_Scoring]
        sf1['Red_Endgame'] = [seed8.Endgame]
        sf1['Red_Fouls'] = [seed8.Fouls]
        sf1['Red_Defense'] = [seed8.Defense]
    wonlost['qf_probs'][0] = qf1_win

    qf2_win = predict_probability(qf2)
    if qf2_win[0] > qf2_win[1]:
        wonlost['qf'][1] = alliances['4']
        sf1['Blue_Traditional_Scoring_High'] = [seed4.Traditional_Scoring_High]
        sf1['Blue_Traditional_Scoring_Low'] = [seed4.Traditional_Scoring_Low]
        sf1['Blue_Technical_Scoring'] = [seed4.Technical_Scoring]
        sf1['Blue_Autonomous_Scoring'] = [seed4.Autonomous_Scoring]
        sf1['Blue_Endgame'] = [seed4.Endgame]
        sf1['Blue_Fouls'] = [seed4.Fouls]
        sf1['Blue_Defense'] = [seed4.Defense]
    else:
        wonlost['qf'][1] = alliances['5']
        sf1['Blue_Traditional_Scoring_High'] = [seed5.Traditional_Scoring_High]
        sf1['Blue_Traditional_Scoring_Low'] = [seed5.Traditional_Scoring_Low]
        sf1['Blue_Technical_Scoring'] = [seed5.Technical_Scoring]
        sf1['Blue_Autonomous_Scoring'] = [seed5.Autonomous_Scoring]
        sf1['Blue_Endgame'] = [seed5.Endgame]
        sf1['Blue_Fouls'] = [seed5.Fouls]
        sf1['Blue_Defense'] = [seed5.Defense]
    wonlost['qf_probs'][1] = qf2_win

    qf3_win = predict_probability(qf3)
    if qf3_win[0] > qf3_win[1]:
        wonlost['qf'][2] = alliances['3']
        sf2['Blue_Traditional_Scoring_High'] = [seed3.Traditional_Scoring_High]
        sf2['Blue_Traditional_Scoring_Low'] = [seed3.Traditional_Scoring_Low]
        sf2['Blue_Technical_Scoring'] = [seed3.Technical_Scoring]
        sf2['Blue_Autonomous_Scoring'] = [seed3.Autonomous_Scoring]
        sf2['Blue_Endgame'] = [seed3.Endgame]
        sf2['Blue_Fouls'] = [seed3.Fouls]
        sf2['Blue_Defense'] = [seed3.Defense]
    else:
        wonlost['qf'][2] = alliances['6']
        sf2['Blue_Traditional_Scoring_High'] = [seed6.Traditional_Scoring_High]
        sf2['Blue_Traditional_Scoring_Low'] = [seed6.Traditional_Scoring_Low]
        sf2['Blue_Technical_Scoring'] = [seed6.Technical_Scoring]
        sf2['Blue_Autonomous_Scoring'] = [seed6.Autonomous_Scoring]
        sf2['Blue_Endgame'] = [seed6.Endgame]
        sf2['Blue_Fouls'] = [seed6.Fouls]
        sf2['Blue_Defense'] = [seed6.Defense]
    wonlost['qf_probs'][2] = qf3_win

    qf4_win = predict_probability(qf4)
    if qf4_win[0] > qf4_win[1]:
        wonlost['qf'][3] = alliances['2']
        sf2['Red_Traditional_Scoring_High'] = [seed2.Traditional_Scoring_High]
        sf2['Red_Traditional_Scoring_Low'] = [seed2.Traditional_Scoring_Low]
        sf2['Red_Technical_Scoring'] = [seed2.Technical_Scoring]
        sf2['Red_Autonomous_Scoring'] = [seed2.Autonomous_Scoring]
        sf2['Red_Endgame'] = [seed2.Endgame]
        sf2['Red_Fouls'] = [seed2.Fouls]
        sf2['Red_Defense'] = [seed2.Defense]
    else:
        wonlost['qf'][3] = alliances['7']
        sf2['Red_Traditional_Scoring_High'] = [seed7.Traditional_Scoring_High]
        sf2['Red_Traditional_Scoring_Low'] = [seed7.Traditional_Scoring_Low]
        sf2['Red_Technical_Scoring'] = [seed7.Technical_Scoring]
        sf2['Red_Autonomous_Scoring'] = [seed7.Autonomous_Scoring]
        sf2['Red_Endgame'] = [seed7.Endgame]
        sf2['Red_Fouls'] = [seed7.Fouls]
        sf2['Red_Defense'] = [seed7.Defense]
    wonlost['qf_probs'][3] = qf4_win

    sf1_win = predict_probability(sf1)
    sf2_win = predict_probability(sf2)

    winner = None

    if sf1_win[0] > sf1_win[1]:
        wonlost['sf'][0] = wonlost['qf'][0]
        f['Red_Traditional_Scoring_High'] = sf1.Red_Traditional_Scoring_High
        f['Red_Traditional_Scoring_Low'] = sf1.Red_Traditional_Scoring_Low
        f['Red_Technical_Scoring'] = sf1.Red_Technical_Scoring
        f['Red_Autonomous_Scoring'] = sf1.Red_Autonomous_Scoring
        f['Red_Endgame'] = sf1.Red_Endgame
        f['Red_Fouls'] = sf1.Red_Fouls
        f['Red_Defense'] = sf1.Red_Defense
    else:
        wonlost['sf'][0] = wonlost['qf'][1]
        f['Red_Traditional_Scoring_High'] = sf1.Blue_Traditional_Scoring_High
        f['Red_Traditional_Scoring_Low'] = sf1.Blue_Traditional_Scoring_Low
        f['Red_Technical_Scoring'] = sf1.Blue_Technical_Scoring
        f['Red_Autonomous_Scoring'] = sf1.Blue_Autonomous_Scoring
        f['Red_Endgame'] = sf1.Blue_Endgame
        f['Red_Fouls'] = sf1.Blue_Fouls
        f['Red_Defense'] = sf1.Blue_Defense
    wonlost['sf_probs'][0] = sf1_win

    if sf2_win[0] > sf2_win[1]:
        wonlost['sf'][1] = wonlost['qf'][3]
        f['Blue_Traditional_Scoring_High'] = sf2.Red_Traditional_Scoring_High
        f['Blue_Traditional_Scoring_Low'] = sf2.Red_Traditional_Scoring_Low
        f['Blue_Technical_Scoring'] = sf2.Red_Technical_Scoring
        f['Blue_Autonomous_Scoring'] = sf2.Red_Autonomous_Scoring
        f['Blue_Endgame'] = sf2.Red_Endgame
        f['Blue_Fouls'] = sf2.Red_Fouls
        f['Blue_Defense'] = sf2.Red_Defense
    else:
        wonlost['sf'][1] = wonlost['qf'][2]
        f['Blue_Traditional_Scoring_High'] = sf2.Blue_Traditional_Scoring_High
        f['Blue_Traditional_Scoring_Low'] = sf2.Blue_Traditional_Scoring_Low
        f['Blue_Technical_Scoring'] = sf2.Blue_Technical_Scoring
        f['Blue_Autonomous_Scoring'] = sf2.Blue_Autonomous_Scoring
        f['Blue_Endgame'] = sf2.Blue_Endgame
        f['Blue_Fouls'] = sf2.Blue_Fouls
        f['Blue_Defense'] = sf2.Blue_Defense
    wonlost['sf_probs'][1] = sf2_win

    f_win = predict_probability(f)

    if f_win[0] > f_win[1]:
        wonlost['f'] = wonlost['sf'][0]
    else:
        wonlost['f'] = wonlost['sf'][1]
    wonlost['f_probs'] = f_win

    return app.make_response(wonlost)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)