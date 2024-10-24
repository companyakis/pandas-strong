import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

print(df["Year"].value_counts().sort_index())

# Year
# 2011     2677
# 2012     2677
# 2013    24443
# 2014    29398
# 2015    24443
# 2016    29398



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
