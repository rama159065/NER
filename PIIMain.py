import guidPrep as guidPrep
import emailFeaturesPrep as emailPrep
import ipAddressFeaturesPrep as ipAddPrep
import phoneFeaturesPrep as phoneFeaturesPrep

import genericModelling as modelling

#Guid testing

input_file_path = 'D:\\python_examples\\PII_DATA\\input\\guid\\guid_data.csv'
#test_file_path = 'D:\\python_examples\\PII_DATA\\test\\guid\\guid_data_test.csv'
feature_engg_train_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\guid\\features_guid.csv'
#feature_engg_test_data_path = 'D:\\python_examples\\PII_DATA\\feature_test\\guid\\features_guid_test.csv'

input_data_cols = guidPrep.prepareData(input_file_path, feature_engg_train_data_path)
print("data preparation completed sucessfully")
print("input data cols to send are ", input_data_cols)

modelling.process(feature_engg_train_data_path, input_data_cols)
print("GIUD Training and serializing the model to pickle file is completed")

#print("Testing the model with new data")
#guidPrep.prepareData(test_file_path, feature_engg_test_data_path)
#modelling.predict(feature_engg_test_data_path,'')


#email Testing
input_file_path = 'D:\\python_examples\\PII_DATA\\input\\email\\email_data.csv'
#test_file_path = 'D:\\python_examples\\PII_DATA\\test\\email\\email_data_test.csv'
feature_engg_train_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\email\\features_email.csv'
#feature_engg_test_data_path = 'D:\\python_examples\\PII_DATA\\feature_test\\email\\features_email_test.csv'

input_data_cols = emailPrep.prepareData(input_file_path, feature_engg_train_data_path)
print("data preparation completed sucessfully")
print("input data cols to send are ", input_data_cols)

modelling.process(feature_engg_train_data_path, input_data_cols)
print("EMAIL Training and serializing the model to pickle file is completed")


#ipAdd Testing

input_file_path = 'D:\\python_examples\\PII_DATA\\input\\ip_address\\ip_address_data.csv'
#test_file_path = 'D:\\python_examples\\PII_DATA\\test\\ip_address\\ip_address_data_test.csv'
feature_engg_train_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\ip_address\\features_ip_address.csv'
#feature_engg_test_data_path = 'D:\\python_examples\\PII_DATA\\feature_test\\ip_address\\features_ip_address_test.csv'

input_data_cols = ipAddPrep.prepareData(input_file_path, feature_engg_train_data_path)
print("data preparation completed sucessfully")
print("input data cols to send are ", input_data_cols)

modelling.process(feature_engg_train_data_path, input_data_cols)
print("IP ADDRESS Training and serializing the model to pickle file is completed")


#phone num Testing

input_file_path = 'D:\\python_examples\\PII_DATA\\input\\phone_num\\phone_num_data.csv'
#test_file_path = 'D:\\python_examples\\PII_DATA\\test\\phone_num\\phone_num_data_test.csv'
feature_engg_train_data_path = 'D:\\python_examples\\PII_DATA\\feature_input\\phone_num\\features_phone_num.csv'
#feature_engg_test_data_path = 'D:\\python_examples\\PII_DATA\\feature_test\\phone_num\\features_phone_num_test.csv'

input_data_cols = phoneFeaturesPrep.prepareData(input_file_path, feature_engg_train_data_path)
print("data preparation completed sucessfully")
print("input data cols to send are ", input_data_cols)

modelling.process(feature_engg_train_data_path, input_data_cols)
print("PHONE NUMBER Training and serializing the model to pickle file is completed")


print("Completed")



