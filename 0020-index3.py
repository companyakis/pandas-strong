import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path, index_col = "Year")

print(df.iloc[:3, :4])

#             Date  Day     Month  Customer_Age
# Year
# 2013  2013-11-26   26  November            19
# 2015  2015-11-26   26  November            19
# 2014  2014-03-23   23     March            49

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
