import pandas as pd

data_path = "./fakedata.csv"

df = pd.read_csv(data_path) 

# print(df.head(3))

#               date  runner_id  speed
# 0  20141013T000000          1    121
# 1  20141209T000000          2     97
# 2  20150225T000000         12     86

date_data = df.date 

data_converted = pd.to_datetime(date_data)

print(data_converted)

# 0   2014-10-13
# 1   2014-12-09
# 2   2015-02-25
# 3   2014-12-09
# 4   2015-02-18
# 5   2015-02-25
# 6   2015-02-25
# 7   2015-02-25
# 8   2015-02-25
# 9   2015-02-25
# Name: date, dtype: datetime64[ns]
