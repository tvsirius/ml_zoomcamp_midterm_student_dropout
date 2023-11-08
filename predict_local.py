"""
Test prediction with model read from local file

"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer

import pickle

SEED=42
# dataset='dataset/dataset.csv'
model_bin='model/model.bin'

def predict_single(student, dv, model):
    X = dv.transform([student])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

print(f'Reading from {model_bin} file')

with open(model_bin, 'rb') as f_in:
    model, dv = pickle.load(f_in)

print((dv, model))
print('Readinf done...')

from sample_studs import *

print('stud1 predict is', predict_single(stud1,model,dv), '  reality is', stud1_dropout)
print('stud2 predict is', predict_single(stud2,model,dv), '  reality is', stud2_dropout)
print('stud3 predict is', predict_single(stud3,model,dv), '  reality is', stud3_dropout)
print('stud4 predict is', predict_single(stud4,model,dv), '  reality is', stud4_dropout)
print('stud5 predict is', predict_single(stud5,model,dv), '  reality is', stud5_dropout)
print('stud6 predict is', predict_single(stud6,model,dv), '  reality is', stud6_dropout)




