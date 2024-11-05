import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query1 = df["Customer_Age"] < 29

query2 = df["Country"] == "Canada"

query3 = df["Sub_Category"] == "Road Bikes"

query = query1 & query2 & query3

new_data = df[query]

print(new_data.shape) # (262, 18)
