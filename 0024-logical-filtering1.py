import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

age_32 = df["Customer_Age"] == 32

print(df[age_32].shape) # (4092, 18)
