import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

print(df["Customer_Age"].iloc[3])

print(df[["Customer_Age", "Country"]].iloc[3])

print(df[["Customer_Age", "Country"]].iloc[[3, 12, 75]])

"""
49
-----------------------------------
Customer_Age           49
Country         Australia
Name: 3, dtype: object
-----------------------------------
    Customer_Age        Country    
3             49      Australia    
12            34      Australia    
75            38  United States   

"""

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
