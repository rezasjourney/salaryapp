## Salary Prediction App

The saved model is trained using only the a subset of the entire training data for simplicity and keeping the saved model size manageable on Github.

Run `pip install -r requirements.txt` to install all relevent packages.

To train a model using the entire dataset download the dataset at https://www.kaggle.com/c/job-salary-prediction/data, unzip `Train_rev1.zip`, and place `Train_rev1.csv` in `data/` and run `python model/train.py`. Otherwise use the included pretrained model `naive_model.joblib` for predictions.

Run the flask app locally using `flask run`, then head to `http://127.0.0.1:5000//predict/salary/<company_name>/<posting_id>` to run predictions.