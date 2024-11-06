import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

print(df["Country"].unique()) # ['Canada' 'Australia' 'United States' 'Germany' 'France' 'United Kingdom']

countries = (df["Country"] == 'Canada') | (df["Country"] == 'Australia') | (df["Country"] == 'United States')

new_df = df[~countries]

print(new_df["Country"].value_counts())

# Country
# United Kingdom    13620
# Germany           11098
# France            10998
# Name: count, dtype: int64
