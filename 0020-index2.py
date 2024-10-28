import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

new_df = df.copy()

new_df.set_index("Country", inplace=True)

print(new_df.index.to_list()[:10])

# ['Canada', 'Canada', 'Australia', 'Australia', 'Australia', 'Australia', 'Australia', 'Australia', 'Australia', 'Australia']


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
