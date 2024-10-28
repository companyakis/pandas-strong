import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query = df.iloc[[0, 2, 3], [0, 3, 4, 7]]

print(query)

#          Date  Year  Customer_Age    Country
# 0  2013-11-26  2013            19     Canada
# 2  2014-03-23  2014            49  Australia
# 3  2016-03-23  2016            49  Australia



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
