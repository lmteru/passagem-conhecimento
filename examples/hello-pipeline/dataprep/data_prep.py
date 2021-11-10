import pandas as pd

def apply_rules(df):
    df["Species"].replace({"Iris-setosa": 0, "Iris-virginica": 1, "Iris-versicolor": 2}, inplace=True)
    df.drop('Id', axis='columns', inplace=True)
    Y = df['Species']
    X = df.drop('Species', axis='columns', inplace=False)

    return X, Y

if __name__ == '__main__':
    df = pd.read_csv('./assets/Iris.csv')
    x, y = apply_rules(df)
    
    x.to_csv('./assets/x.csv', index = False)
    y.to_csv('./assets/y.csv', index = False)