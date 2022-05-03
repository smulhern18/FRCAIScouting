from joblib import load
import pandas as pd
clf = load('models/WonLostMLPClassifier.joblib') 

def predict(x):
    x = x.drop(columns=['year', 'competition', 'match', 'mtype', 'bscore', 'rscore', 'red_won', 'Unnamed: 0'], errors='ignore')
    y_pred = clf.predict(x)
    return y_pred

if __name__ == '__main__':  
    from sklearn.metrics import accuracy_score  
    print('Running test __main__')
    data_train = pd.read_csv('data/v2/train_qm.csv')
    Y_train = data_train['blue_won'].values
    X_train = data_train.drop(columns=['blue_won'])
    y_pred_train = predict(X_train)
    print('Train', accuracy_score(Y_train, y_pred_train))

    data_test = pd.read_csv('data/v2/test_qm.csv')
    Y_test = data_test['blue_won'].values
    X_test = data_test.drop(columns=['blue_won'])
    y_pred_test = predict(X_test)

    print('Test', accuracy_score(Y_test, y_pred_test))
