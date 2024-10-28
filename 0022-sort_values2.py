import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

df.sort_values("Year", inplace = True, ascending = False)

# print(df.iloc[:, : 4].tail())

#              Date  Day      Month  Year
# 71549  2011-02-06    6   February  2011
# 71521  2011-06-23   23       June  2011
# 71523  2011-07-03    3       July  2011
# 71525  2011-08-01    1     August  2011
