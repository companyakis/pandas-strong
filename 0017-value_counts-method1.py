import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

print(df["Year"].value_counts())

# Year
# 2016    29398
# 2014    29398
# 2015    24443
# 2013    24443
# 2012     2677
# 2011     2677

# Date                1884
# Day                   31
# Month                 12
# Year                   6
# Customer_Age          70
# Age_Group              4
# Customer_Gender        2
# Country                6
# State                 53
# Product_Category       3
# Sub_Category          17
# Product              130
# Order_Quantity        32
# Unit_Cost             34
# Unit_Price            36
# Profit              1256
# Cost                 360
# Revenue             1876
# dtype: int64


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
