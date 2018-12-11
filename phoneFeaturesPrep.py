
import re
import pandas as pd

#input_file_path = 'D:\python_examples\PII_DATA\input\phone_num\phone_num.csv'
#feature_engg_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\phone_num\\features_phone_num.csv'

input_data_columns=['phone_num','other']
output_field = ['has_plus','has_hyphen','has_bracket','has_no_alpha','is_numeric','field_len','is_num_in_range','label']

def read_csv(input_file_path):
    #input_df = pd.read_csv('D:\python_examples\ML_TEST\src\guid\guid.csv')
    input_df = pd.read_csv(input_file_path)
    print("reading csv")
    print(input_df.head())
    return input_df


def generate_rows():
    input_df = read_csv()

def has_plus(data):
    try:
        return 1 if data[0]=='+' else 0
    except:
        return 0

def has_hyphen(data):
    if ('-' in data):
        return 1
    return 0

def has_brackets(data):
    c = re.compile('^[()]')
    try:
        if (bool(c.match(data))):
            return 1
        else:
            return 0
    except:
        return 0

def has_no_alpha(data):
    if (bool(re.search('[a-zA-Z]+', data))):
        return 0
    return 1

def is_numeric(data):
    try :
        if(data.isdigit()):
            return 1
        else:
            return 0
    except:
        return 0

def get_field_len(data):
    try:
        return len(data)
    except:
        return 0

def is_num_in_range(data):
    nums = getOnlyDigits(data)
    if(len(nums) >=10 and len(nums)<= 15):
        return 1
    return 0

def getOnlyDigits(data):
    nums = re.sub('[^0-9]', '', data)
    return nums;


def generate_feature_list(data,colName):
    plus = has_plus(data)
    hyphen = has_hyphen(data)
    bracket = has_brackets(data)
    no_aplha = has_no_alpha(data)
    numeric = is_numeric(data)
    in_range = is_num_in_range(data)


    field_len = get_field_len(data)
    return (plus, hyphen,bracket,no_aplha,numeric,field_len, in_range, colName)

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