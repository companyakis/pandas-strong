import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query = df["Country"].isin(["Canada", "Germany"])

print(df[query].shape[0]) # 25276 => 14178 + 11098

# print(df["Country"].value_counts())

# Country
# United States     39206
# Australia         23936
# Canada            14178
# United Kingdom    13620
# Germany           11098
# France            10998
