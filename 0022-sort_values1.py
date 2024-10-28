import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

df.sort_values("Year", inplace = True)

# print(df.tail())

#               Date  Day  Month  Year  ...  Unit_Price Profit Cost Revenue
# 19337   2016-04-10   10  April  2016  ...           9     38  196     234
# 19335   2016-06-29   29   June  2016  ...           9     35  133     168
# 19333   2016-05-04    4    May  2016  ...           9     13   49      62
# 113019  2016-07-30   30   July  2016  ...          64    310  240     550
# 113031  2016-04-12   12  April  2016  ...          64    112   72     184
