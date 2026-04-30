from sklearn.linear_model import LinearRegression

def train_model(df):
    X = df[['clarte']]
    y = df['note_cours']

    model = LinearRegression()
    model.fit(X, y)

    return model