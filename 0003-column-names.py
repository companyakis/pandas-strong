import pandas as pd

data_path = "./diabteswithoutnames.csv"

COLUMN_NAMES = [
    "Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age","Outcome"
]

# df_first = pd.read_csv(data_path)

# print(df_first)

"""
Example rows

0     1   85  66  29    0  26.6  0.351  31  0
1     8  183  64   0    0  23.3  0.672  32  1
"""

df = pd.read_csv(data_path, names = COLUMN_NAMES)

print(df)

"""
First two rows
         Pregnancies  Glucose  BloodPressure  ...  DiabetesPedigreeFunction  Age  Outcome
0              6      148             72  ...                     0.627   50        1       
1              1       85             66  ...                     0.351   31        0    
"""
