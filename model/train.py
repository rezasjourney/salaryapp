import data

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import linear_model
from sklearn.metrics import r2_score

import joblib
from pathlib import Path
from os.path import join, exists

def build(save=True):
    dataset = data.prepare()
    descriptions = dataset['CleanDescription'].tolist()
    salaries = dataset['SalaryNormalized'].tolist()

    vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 3), max_features=24000000)
    features = vectorizer.fit_transform(descriptions)

    Xtrain, Xval, ytrain, yval = train_test_split(features, salaries, test_size=0.3)

    rr = linear_model.Ridge(alpha=0.035)
    rr.fit(Xtrain, ytrain)

    r2 = r2_score(yval, rr.predict(Xval))
    print(f'Ridge Regression R2 = {r2}')

    if save:
        app_dir = Path(__file__).resolve().parents[1]
        joblib.dump([rr, vectorizer], join(app_dir, 'naive_model.joblib'))

    return rr, vectorizer

def load(filename=None):
    if filename is None:
        app_dir = Path(__file__).resolve().parents[1]
        filename = join(app_dir, 'naive_model.joblib')

    if not exists(filename):
        return None, None
    
    model, vectorizer = joblib.load(filename)

    return model, vectorizer

if __name__ == '__main__':
    print('No saved model')
    rr, vectorizer = load()
    print(rr)
    print(vectorizer)

    print('Building model')
    rr, vectorizer = build()
    print(rr)
    print(vectorizer)

    print('Loading saved model')
    rr, vectorizer = load()
    print(rr)
    print(vectorizer)
