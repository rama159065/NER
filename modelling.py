# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 07:51:45 2018

@author: Rama krishna
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pickle

input_data_columns = ['guid', 'other']
np.random.seed(0)
rf_pkl_filepath = 'D:\\python_examples\\GUID_DATA\\pickle\\'
rf_pkl_filename = "rf_guid_20181205.pkl"

def read_csv(intput_file_path):
    input_df = pd.read_csv(intput_file_path, ',')
    return input_df

def process(intput_file_path):
    input_df = read_csv(intput_file_path)
    Y = pd.factorize(input_df['label'])[0]
    input_df['label'] = pd.Categorical.from_codes(Y, input_data_columns)

    input_df['is_train'] = np.random.uniform(0, 1, len(input_df)) <= .60
    train, test = input_df[input_df['is_train'] == True], input_df[input_df['is_train'] == False]

    print(pd.value_counts(train['label']))
    print(pd.value_counts(test['label']))
    features = train.columns[0:11]
    print(features)
    y = pd.factorize(train['label'])[0]
    trained_model = train_model(train[features],y)
    test_y = pd.factorize(test['label'])[0]
    model_prediction(test[features], test_y, trained_model)
    dumpModel(trained_model)

def train_model(features, target):
    clf = RandomForestClassifier(n_jobs=3, criterion='entropy', random_state=0)
    clf.fit(features, target)
    return clf

def model_prediction(test, test_y, trained_model):
    predictions = trained_model.predict(test)
    predictions_proba = trained_model.predict_proba(test)
    test_accuracy(predictions, predictions_proba, test_y)
    return (predictions,predictions_proba)

def test_accuracy(predictions, predictions_proba, test_y):
    print("Model Accuracy is ",accuracy_score(test_y, predictions))
    print("confusion matrix is", confusion_matrix(test_y,predictions))

#method to serialize the model to disk.
def dumpModel(rf_tree_model):

    rf_model_pkl = open(rf_pkl_filepath+rf_pkl_filename, 'wb')
    pickle.dump(rf_tree_model, rf_model_pkl)
    rf_model_pkl.close()

#Loading the saved model pickle
def loadmodel():
    rf_model_pkl = open(rf_pkl_filepath+rf_pkl_filename, 'rb')
    rf_model = pickle.load(rf_model_pkl)
    print("Loaded RF model :: ", rf_model);
    return rf_model

#This method is used to test the data using new test data.
def test_model(test_file_path):
    rf_model_pkl = loadmodel()
    test_df = read_csv(test_file_path)
    print(test_df.head())
    test_df['label'].replace(to_replace=['guid', 'other'], value=[0, 1], inplace=True)
    test_y = test_df['label']
    features_test = test_df.columns[0:11]
    predictions, predict_proba = model_prediction(test_df[features_test], test_y, rf_model_pkl)
    predictions = pd.Categorical.from_codes(predictions, input_data_columns)
    print("predictions are ", predictions)
    print("prediction probs", predict_proba)


def main():
    process()

if __name__ == '__main__':
    main()