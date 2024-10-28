import pandas as pd
import numpy as np

data_path = "./sales_data.csv"

df = pd.read_csv(data_path, index_col = "Country")

df.sort_index(inplace=True, ascending = False)

print(df.iloc[:, :3].head())

print("----------------------------")

print(df.iloc[:, :3].tail())

#                      Date  Day      Month
# Country
# United States  2013-06-12   12       June
# United States  2015-09-17   17  September
# United States  2013-11-09    9   November
# United States  2015-10-25   25    October
# United States  2013-10-25   25    October
# ----------------------------
#                  Date  Day      Month
# Country
# Australia  2013-09-26   26  September
# Australia  2015-09-12   12  September
# Australia  2013-12-29   29   December
# Australia  2015-12-29   29   December
# Australia  2015-12-02    2   December
