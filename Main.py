import guidPrep as guidPrep

import modelling as modelling

input_file_path = 'D:\\python_examples\\GUID_DATA\\input\\guid_data.csv'
test_file_path = 'D:\\python_examples\\GUID_DATA\\test\\guid_data_test.csv'
#test_file_path = 'D:\\python_examples\\GUID_DATA\\test\\guid_data_other.csv'
feature_engg_train_data_path = 'D:\\python_examples\GUID_DATA\\feature_input\\features.csv'
feature_engg_test_data_path = 'D:\\python_examples\GUID_DATA\\feature_test\\features_test.csv'

guidPrep.prepareData(input_file_path, feature_engg_train_data_path)
print("data preparation completed sucessfully")

modelling.process(feature_engg_train_data_path)
print("Training and serializing the model to pickle file is completed")

print("Testing the model with new data")
guidPrep.prepareData(test_file_path, feature_engg_test_data_path)
modelling.test_model(feature_engg_test_data_path)
print("Completed")



