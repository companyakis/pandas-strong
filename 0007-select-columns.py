import pandas as pd

data_path = "./diabetes.csv"

diabets = pd.read_csv(data_path)

print(diabets.columns)

# Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')

selected_columns = ["BMI", "Age", "Outcome"]

partial_diabets = diabets[selected_columns]

print(partial_diabets.head())

"""
    BMI  Age  Outcome
0  33.6   50        1
1  26.6   31        0
2  23.3   32        1
3  28.1   21        0
4  43.1   33        1

"""
