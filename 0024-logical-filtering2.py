import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

age_not_32 = df["Customer_Age"] != 32

print(df[age_not_32].shape) # (108944, 18)

age_over_40 = df["Customer_Age"] > 40

print(df[age_over_40].shape) # (35926, 18)
