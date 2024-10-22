import pandas as pd

data_path = "./diabetes.csv"

diabets = pd.read_csv(data_path)

print(diabets.shape)

print(diabets.columns)

print(diabets.info())

print(diabets.describe())

print(diabets.head(4))

print(diabets.head())

print(diabets.tail(8))

print(diabets.tail())
