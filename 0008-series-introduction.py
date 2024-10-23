import pandas as pd

data_path = "./diabetes.csv"

df = pd.read_csv(data_path)

print(type(df))

print(df.columns)

# <class 'pandas.core.frame.DataFrame'>

# Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
#       dtype='object')

partial_data = df.Age

print(type(partial_data)) # <class 'pandas.core.series.Series'>

print(partial_data.head())

# 0    50
# 1    31
# 2    32
# 3    21
# 4    33
