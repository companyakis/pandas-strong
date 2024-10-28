import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

df.drop(labels = 2, inplace = True)

# print(df.iloc[:, :5].head())

#          Date  Day     Month  Year  Customer_Age
# 0  2013-11-26   26  November  2013            19
# 1  2015-11-26   26  November  2015            19
# 3  2016-03-23   23     March  2016            49
# 4  2014-05-15   15       May  2014            47
# 5  2016-05-15   15       May  2016            47
