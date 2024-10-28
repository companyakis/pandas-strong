import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query = df.iloc[:3, 2: 5]

print(query)

#       Month  Year  Customer_Age
# 0  November  2013            19
# 1  November  2015            19
# 2     March  2014            49



# print(df.dtypes)

# Date                object
# Day                  int64
# Month               object
# Year                 int64
# Customer_Age         int64
# Age_Group           object
# Customer_Gender     object
# Country             object
# State               object
# Product_Category    object
# Sub_Category        object
# Product             object
# Order_Quantity       int64
# Unit_Cost            int64
# Unit_Price           int64
# Profit               int64
# Cost                 int64
# Revenue              int64
# dtype: object
