import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query = df["Customer_Age"].between(80, 82)

print(df[query].shape) # (22, 18)
