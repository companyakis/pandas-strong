import pandas as pd

data_path = "./diabetes.csv"

diabets = pd.read_csv(data_path)

print(diabets.columns)

# Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')

new_diabets = diabets.drop(labels = 'Glucose', axis = 1)

print(new_diabets.columns)

# Index(['Pregnancies', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
#        'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')
