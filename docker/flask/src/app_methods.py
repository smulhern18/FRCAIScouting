import numpy as np
import math


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