from app import app, utils
from model import train

import joblib
from pathlib import Path
from os.path import join

from flask import jsonify

@app.route('/')
def index():
    return 'Welcome to salaryapp'

@app.route('/predict/salary/<company_name>/<posting_id>')
def predict(company_name, posting_id):
    base_url = 'https://jobs.lever.co/'
    url = base_url + company_name + '/' + posting_id
    description = utils.extract_text(url)
    description = utils.clean_text(description)

    app_dir = Path(__file__).resolve().parents[1]
    model, vectorizer = train.load(join(app_dir, 'naive_model.joblib'))

    prediction = model.predict(vectorizer.transform([description]))[0]

    output = {
        'URL': url,
        'Prediction': '${:,.2f}'.format(round(prediction, 2))
    }
    
    return jsonify(output)
   