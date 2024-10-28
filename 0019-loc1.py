import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

query = df.loc[:, ["Date", "Customer_Age", "Product", "Order_Quantity"]].head()

print(query)

#          Date  Customer_Age              Product  Order_Quantity
# 0  2013-11-26            19  Hitch Rack - 4-Bike               8
# 1  2015-11-26            19  Hitch Rack - 4-Bike               8
# 2  2014-03-23            49  Hitch Rack - 4-Bike              23
# 3  2016-03-23            49  Hitch Rack - 4-Bike              20
# 4  2014-05-15            47  Hitch Rack - 4-Bike               4

