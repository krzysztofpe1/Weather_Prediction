import pandas as pd
import numpy as np

#Test of uploading data
def get_data():
    df = pd.read_csv('data/k_d_01_2020.csv',encoding = 'unicode_escape')
    #x_data = df["t8"].to_numpy()
    #y_data = df["t9"].to_numpy()
    return df

def split_data(dataset):
    train_dataset = dataset.sample(frac=0.8, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)

    return train_dataset, test_dataset