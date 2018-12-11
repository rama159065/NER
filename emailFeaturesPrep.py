
import re
import pandas as pd


#input_file_path = 'D:\python_examples\PII_DATA\input\email\email_data.csv'
#feature_engg_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\email\\features_email.csv'

input_data_columns=['email_id','other']
output_field = ['has_dot','has_at','domain_sep_count','has_dot_aft_at','is_min_len','is_email_pattern','label']

def read_csv(input_file_path):
    #input_df = pd.read_csv('D:\python_examples\ML_TEST\src\guid\guid.csv')
    input_df = pd.read_csv(input_file_path)
    print("reading csv")
    print(input_df.head())
    return input_df


def generate_rows():
    input_df = read_csv()

def has_dot(data):
    if('.' in data):
        return 1
    return 0

def has_at(data):
    if('@' in data):
        return 1
    return 0


def domain_sep_count(data):
    try:
        return data.count('@')
    except:
        return 0


def has_dot_aft_at(data):
    try:
        if (data.index('@') > 0):
            subset_aft_at = data[data.index('@') + 1:]
            if dot_count(subset_aft_at) > 0:
                return 1
            else:
                return 0
    except:
        return 0



def is_min_len(data):
    if(len(data) > 7):
        return 1
    return 0


def is_email_pattern(data):
    c = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', re.I)
    res = c.match(data)
    if res:
        return 1
    return 0

def dot_count(data):
    try:
        return data.count('.')
    except:
        return 0

def generate_feature_list(data,colName):

    return (has_dot(data), has_at(data),domain_sep_count(data),has_dot_aft_at(data),
            is_min_len(data),is_email_pattern(data), colName)

def prepareData(input_file_path, feature_engg_data_path):
    df = read_csv(input_file_path)
    cols = df.columns.values
    total_row_list = list()
    for eachColName in cols:
        feature_data = df[eachColName]
        for colData in feature_data:
            each_row = generate_feature_list(colData,eachColName)
            total_row_list.append(each_row)
        print(total_row_list)
    writeToFile(total_row_list, feature_engg_data_path)
    return cols


def writeToFile(total_row_list, feature_engg_data_path):
    #file_object = open("D:\\python_examples\\OUTPUT\\guid_output.csv", "w")
    file_object = open(feature_engg_data_path, "w")

    file_object.write(','.join(str(colVal) for colVal in output_field) + '\n')
    for item in total_row_list:
        file_object.write(','.join(str(colVal) for colVal in item)+ '\n')
    file_object.close()


def main():
    print("Main")
    #prepareData(input_file_path,feature_engg_data_path)


if __name__ == '__main__':
    main()