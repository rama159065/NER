# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:59:07 2018

@author: Rama krishna
"""

import re
import pandas as pd
import string


input_data_columns=['guid','other']
output_field = ['has_hyphen','has_bracket','is_alpha_num','is_hexa_decimal','is_guid_pattern',
                'field_len','token_1_len','token_2_len','token_3_len','token_4_len', 'token_5_len','label']

input_path = 'D:\\python_examples\\GUID_DATA\\input\\guid_data.csv'
feature_engg_path = 'D:\\python_examples\GUID_DATA\\feature_cols_input\\features.csv'

def read_csv():
    #input_df = pd.read_csv('D:\python_examples\ML_TEST\src\guid\guid.csv')
    input_df = pd.read_csv(input_path)
    print("reading csv")
    print(input_df.head())
    print(input_df.columns)
    print(input_data_columns)
    return input_df


def generate_rows():
    input_df = read_csv()


def get_field_len(data):
    try:
        return len(data)
    except:
        return 0


def hyphen_count(data):
    try:
        return data.count('-')
    except:
        return 0


def is_alpha_num(data):
    try:
        if (data.isalnum()):
            return 1
        else:
            return 0
    except:
        return 0


def is_hexa_decimal(data):
    if (all(c in string.hexdigits for c in data)):
        return 1
    return 0


def has_hyphen(data):
    if ('-' in data):
        return 1
    return 0


def has_brackets(data):
    c = re.compile('^[{}]')
    try:
        if (bool(c.match(data))):
            return 1
        else:
            return 0
    except:
        return 0


def tokenize(data):
    splits = data.split('-')
    return splits


def is_guid_pattern(data):
    #c = re.compile('[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', re.I)
    c = re.compile('[0-9a-fA-F]{8}[0-9a-fA-F]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{4}[0-9a-fA-F]{12}', re.I)
    res = c.match(data)
    if res:
        return 1
    return 0


def change_to_lower(data):
    return data.lower()

def removeSpecialChars(data):
    data = re.sub(r'[-|{|}]', r'', data)
    return data


def token_by_fixed_len(data):
    return 0

def generate_feature_list(data,colName):
    hyphen = has_hyphen(data)
    bracket = has_brackets(data)
    tokens = tokenize(data)
    print("tokens are ", tokens)
    print(type(tokens))
    tokensDict = {0:0, 1:0, 2:0, 3:0, 4:0};
    if(bool(hyphen) or bool(bracket)):
        data = removeSpecialChars(data)
    alphanum = is_alpha_num(data)
    hexa_deci = is_hexa_decimal(data)
    guid_pattern = is_guid_pattern(data)
    field_len = get_field_len(data)
    if(len(tokens) == 5):
        for i in range(0, len(tokens)):
        #for token in tokens :
            print("value of i is ", tokens[i])
            tokensDict[i] = get_field_len(tokens[i])
    return (hyphen,bracket,alphanum,hexa_deci,guid_pattern, field_len, tokensDict[0],tokensDict[1],tokensDict[2],tokensDict[3],tokensDict[4],colName)

    return 0

def prepareData():
    df = read_csv()
    total_row_list = list()
    for eachColName in input_data_columns:
        feature_data = df[eachColName]
        for colData in feature_data:
            each_row = generate_feature_list(colData,eachColName)
            total_row_list.append(each_row)
    print(total_row_list)
    writeToFile(total_row_list)


def writeToFile(total_row_list):
    #file_object = open("D:\\python_examples\\OUTPUT\\guid_output.csv", "w")
    file_object = open(feature_engg_path, "w")

    file_object.write(','.join(str(colVal) for colVal in output_field) + '\n')
    for item in total_row_list:
        file_object.write(','.join(str(colVal) for colVal in item)+ '\n')
    file_object.close()


def main():
    print("Main")
    prepareData()


if __name__ == '__main__':
    main()