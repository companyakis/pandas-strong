import pandas as pd

data_path = "./diabetes.csv"

df = pd.read_csv(data_path)

# print(df.columns)

# print(df.shape)

# Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')
# (768, 9)

# count method

print(df["Age"].count()) # 768

