from app import app

@app.route('/')
def index():
    return 'Welcome to salaryapp'

@app.route('/predict/salary/<company_name>/<posting_id>')
def predict(company_name, posting_id):
    base_url = 'https://jobs.lever.co/'
    url = base_url + company_name + '/' + posting_id
    return url
   