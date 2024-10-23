import pandas as pd

data_path = "./diabetes.csv"

df = pd.read_csv(data_path)

# print(df.dtypes)

"""
Pregnancies                   int64
Glucose                       int64
BloodPressure                 int64
SkinThickness                 int64
Insulin                       int64
BMI                         float64
DiabetesPedigreeFunction    float64
Age                           int64
Outcome                       int64
dtype: object
"""
print(df["Age"].sum()) # 25529

print(df.sum(numeric_only = True))

"""
Pregnancies                  2953.000
Glucose                     92847.000
BloodPressure               53073.000
SkinThickness               15772.000
Insulin                     61286.000
BMI                         24570.300
DiabetesPedigreeFunction      362.401
Age                         25529.000
Outcome                       268.000
dtype: float64   
"""

