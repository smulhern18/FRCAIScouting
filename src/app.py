from flask import Flask, request
import pandas as pd
import numpy as np
import math

app = Flask(__name__)


@app.route('/compute/team/<string:team_num>/competition/<string:event_key>', methods=["GET"])
def compute(team_num, event_key):

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
        print(element['team_key'], element['rank'])
        for index in range(1, 17):
            if element['rank'] == index:
                if element['rank'] <= 8:
                    top_8[index-1] = element['team_key']
                elif element['rank'] <= 16:
                    just_outside[index-9] = element['team_key']

    optimized_alliances = optimize(top_8, just_outside, comp)

    print(optimized_alliances)

    return app.make_response(optimized_alliances)


def optimize(top_8, just_outside, comp):
    alliances = []
    all_robots = list(comp['Robot'])
    for robot in top_8:
        teams = [robot]
        all_robots.remove(robot)
        best_area = 0
        best_robot = ''
        for robot_add in all_robots:
            teams.append(robot_add)
            area = calc_alliance_area(teams, comp)
            if area > best_area:
                best_area = area
                best_robot = robot_add
            teams.remove(robot_add)
        teams.append(best_robot)
        all_robots.remove(best_robot)
        if best_robot in top_8:
            top_8.remove(best_robot)
            top_8.append(just_outside[0])
            just_outside.remove(just_outside[0])
        if best_robot in just_outside:
            just_outside.remove(best_robot)

        alliances.append(teams)

    alliances_r = alliances[::-1]
    for alliance in alliances_r:
        best_area = 0
        best_robot = ''
        for robot_add in all_robots:
            alliance.append(robot_add)
            area = calc_alliance_area(alliance, comp)
            if area > best_area:
                best_area = area
                best_robot = robot_add
            alliance.remove(robot_add)
        alliance.append(best_robot)
        all_robots.remove(best_robot)

    alliances = alliances_r[::-1]

    alliances = {
        '1': alliances[0],
        '2': alliances[1],
        '3': alliances[2],
        '4': alliances[3],
        '5': alliances[4],
        '6': alliances[5],
        '7': alliances[6],
        '8': alliances[7]
    }

    return alliances


def calc_alliance_area(teams, comp):

    scoring_cols = list(comp.columns)[2:-2]
    robots = comp[comp['Robot'].isin(teams)]
    area = 0
    for i, col in enumerate(scoring_cols):
        a_col = col
        if i == len(scoring_cols) - 1:
            b_col = scoring_cols[0]
        else:
            b_col = scoring_cols[i + 1]
        a = np.mean(robots[a_col].values)
        b = np.mean(robots[b_col].values)
        c = math.radians(360 / 7)
        triangle = 0.5 * a * b * math.sin(c)
        area += triangle
    return area


if __name__ == "__main__":
    compute('frc190', '2019vapor')
    #app.run(host="0.0.0.0", port=80, debug=True)