import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

print(df["Customer_Age"].value_counts().sort_index().head(10))

# normalize data

print(df["Customer_Age"].value_counts(normalize = True).sort_index().head(10))

"""
Customer_Age
17    1306
18    1760
19    2010
20    2020
21    2230
22    2636
23    2826
24    3040
25    3050
26    3352
Name: count, dtype: int64

Customer_Age
17    0.011554
18    0.015570
19    0.017782
20    0.017870
21    0.019728
22    0.023320
23    0.025001
24    0.026894
25    0.026983
26    0.029654
Name: proportion, dtype: float64

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
