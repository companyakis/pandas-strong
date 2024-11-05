import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query1 = df["Customer_Age"] < 29

query2 = df["Country"] == "Canada"

query3 = df["Country"] == "Australia"

query = query1 & (query2 | query3)

new_data = df[query]

print(new_data.shape) # (11390, 18)

print(new_data["Customer_Age"].value_counts())

print(new_data["Country"].value_counts())

# Customer_Age
# 27    1226
# 28    1224
# 26    1174
# 22    1060
# 25    1058
# 24    1048
# 23    1040
# 18     794
# 21     770
# 20     750
# 19     700
# 17     546
# Name: count, dtype: int64

# Country
# Australia    7668        
# Canada       3722        
# Name: count, dtype: int64
