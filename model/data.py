from pathlib import Path
from os.path import join
import pandas as pd
from utils import clean

def prepare():
    app_dir = Path(__file__).resolve().parents[1]
    dataset = pd.read_csv(join(app_dir, 'data', 'Train_rev1.csv'))[:3000]
    dataset = dataset[['FullDescription', 'SalaryNormalized']]
    dataset['CleanDescription'] = dataset['FullDescription'].apply(lambda d: clean(d))
    
    return dataset

if __name__ == '__main__':
    dataset = prepare()
    print(dataset.head())
