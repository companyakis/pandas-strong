import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path, index_col = "Country")

df.sort_index(inplace=True)

print(df.iloc[:, :3].head())

print("----------------------------")

print(df.iloc[:, :3].tail())

#                  Date  Day     Month
# Country
# Australia  2016-04-18   18     April
# Australia  2016-02-06    6  February
# Australia  2016-02-06    6  February
# Australia  2014-02-11   11  February
# Australia  2016-02-11   11  February
# ----------------------------
#                      Date  Day     Month
# Country
# United States  2013-12-02    2  December
# United States  2013-12-02    2  December
# United States  2015-12-02    2  December
# United States  2015-08-03    3    August
# United States  2011-12-23   23  December
