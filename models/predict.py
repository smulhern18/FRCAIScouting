from joblib import load
import pandas as pd
clf = load('models/WonLostMLPClassifier.joblib') 

def predict(x):
    x = x.drop(columns=['year', 'competition', 'match', 'mtype', 'bscore', 'rscore', 'red_won', 'blue_won'])
    y_pred = clf.predict(x.values)
    return y_pred

if __name__ == '__main__':    
    print('Running test __main__')
    data_test = pd.read_csv('data/v2/test.csv')
    data_test = data_test.loc[data_test['mtype'].str.contains("qm")]
    y_pred = predict(data_test)
    print(y_pred.shape)