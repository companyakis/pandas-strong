import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

#print(df["Country"].unique()) # ['Canada' 'Australia' 'United States' 'Germany' 'France' 'United Kingdom']

new_countries = df["Country"].replace("United States", "USA")

df["Country"] = new_countries

print(df["Country"].unique()) # ['Canada' 'Australia' 'USA' 'Germany' 'France' 'United Kingdom']
