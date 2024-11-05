import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query1 = df["Customer_Age"] == 29

query2 = df["Country"] == "Canada"

query = query1 & query2

new_data = df[query]

print(new_data.shape) # (554, 18)

print(new_data.iloc[:, :5].head())

#           Date  Day      Month  Year  Customer_Age
# 14  2013-08-02    2     August  2013            29
# 15  2015-08-02    2     August  2015            29
# 16  2013-09-02    2  September  2013            29
# 17  2015-09-02    2  September  2015            29
# 18  2014-01-22   22    January  2014            29
