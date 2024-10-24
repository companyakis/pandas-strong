import pandas as pd
import numpy as np

data_path = "./diabetes.csv"

df = pd.read_csv(data_path)

print(df["Age"].mean()) # 33.240885416666664

print(np.round(df["Age"].mean(), 2)) # 33.24


# print(df.dtypes)

# Pregnancies                   int64
# Glucose                       int64
# BloodPressure                 int64
# SkinThickness                 int64
# Insulin                       int64
# BMI                         float64
# DiabetesPedigreeFunction    float64
# Age                           int64
# Outcome                       int64
# dtype: object
