# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:51:45 2018

@author: Rama krishna
"""

from csv import reader
from random import randrange
from math import sqrt
from math import exp
from math import pi

import pandas as pd
import numpy as np
from sklearn.enable import RandomForestClassifier

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


np.random.seed(0)

filename = 'data.csv'
input_df = pd.read_csv(filename, ',')
y = pd.factorize(input_df['label'])[0]

input_data_columns=['guid','other']
input_df['label'] = pd.Categorical.from_codes(y,input_data_columns)

input_df['is_train'] = np.random.uniform(0, 1, len(input_df)) <= .60
# Create two new dataframes, one with the training rows, one with the test rows
train, test = input_df[input_df['is_train']==True], input_df[input_df['is_train']==False]

def random_forest_classifier(features, target):
    clf = RandomForestClassifier(n_jobs=3,criterion='entropy',random_state=0)
    clf.fit(features, target)
    return clf

def Logistic_regression(features, target):
    return 0

def Decission_tree(features, target):
    return 0

def support_vector_machine(features, target):
    return 0

def boosting_algo(features, target):
    return 0    



            
        

