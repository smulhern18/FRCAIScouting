from joblib import load
import pandas as pd
from statistics import mean
try:
    clf = load('models/WonLostMLPClassifier.joblib')
except FileNotFoundError:
    clf = load('WonLostMLPClassifier.joblib')


def predict_probability(x):
    x = x.drop(columns=['year', 'competition', 'match', 'mtype', 'bscore', 'rscore', 'red_won', 'blue_won'])

    y = clf.predict_proba(x)

    return y


if __name__ == '__main__':    
    print('Running test __main__')
    data_test = pd.read_csv('../../data/v2/test.csv')
    data_test = data_test.loc[data_test['mtype'].str.contains("sf")]
    y_predediction = predict_probability(data_test)
    print(y_predediction)
