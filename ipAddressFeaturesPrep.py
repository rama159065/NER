
import re
import pandas as pd

#input_file_path = 'D:\python_examples\PII_DATA\input\ip_address\ip_address_data.csv'
#feature_engg_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\ip_address\\features_ip_address.csv'

#input_data_columns=['ip','other']
output_field = ['has_dot','dot_count','is_ip_pattern','has_no_alpha','is_numeric','field_len','is_ip_in_range','label']

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

def dot_count(data):
    if(data.count(".") == 3):
        return 1
    return 0

def is_ip_pattern(data):
    ippattern = '([1-2]?[0-9]?[0-9]\.){1,3}([1-2]?[0-9]?[0-9])?'
    try:
        return  1 if re.match(ippattern, data) else 0
    except:
        return 0

def getTokens(data):
    return data.split('.')

def is_numeric(data):
    tokens = getTokens(data)
    fields = [not token.isdigit() for token in tokens]
    if(any(fields)):
        return 0
    return 1

def is_ip_in_range(data):
    tokens = getTokens(data)
    fields = []
    for token in tokens:
        try:
            if(int(token) > 255):
                fields.append(token)
        except:
            return 0
    if (any(fields)):
        return 0
    return 1

def get_field_length(data):
    try :
        return len(data)
    except:
        return 0

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

def generate_feature_list(data,colName):
    dot = has_dot(data)
    dotCount = dot_count(data)
    ipPattern = is_ip_pattern(data)
    noAlpha = has_no_alpha(data)
    numeric = is_numeric(data)
    field_len = get_field_len(data)
    ip_in_range = is_ip_in_range(data)

    return (dot, dotCount,ipPattern,noAlpha,numeric,field_len, ip_in_range, colName)

def prepareData(input_file_path, feature_engg_data_path):
    df = read_csv(input_file_path)
    cols = df.columns.values
    print(cols)
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