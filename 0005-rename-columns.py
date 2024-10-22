import pandas as pd

data_path = "./diabetes.csv"

diabets = pd.read_csv(data_path)

# print(diabets.columns)

# Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')

# print(diabets.shape) # (768, 9)

new_diabets = diabets.rename(columns = {'BMI': 'body_mass_index', 'Age': 'patient_age'})

print(new_diabets.columns)

# Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'body_mass_index', 'DiabetesPedigreeFunction', 'patient_age',
#        'Outcome'],
#       dtype='object')
