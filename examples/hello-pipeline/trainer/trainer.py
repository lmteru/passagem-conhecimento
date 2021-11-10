from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

def train_model(x, Y):
    clf = LogisticRegression(random_state=0).fit(x,Y)

    return clf

def pickler(model, path):
    try:
        with open(path, 'wb') as file:
            pickle.dump(model, file)
        return True
    except:
        return False

def get_data(x_path, y_path):
    x = pd.read_csv(x_path)
    y = pd.read_csv(y_path)
    
    return x, y

if __name__ == '__main__':
    x, y = get_data('./assets/x.csv', './assets/y.csv')
    model = train_model(x, y)
    pickler(model, './assets/pickled.pkl')