import pandas as pd

data_path = "./fakedata.csv"

df = pd.read_csv(data_path) 

print(df.columns) # Index(['date', 'runner_id', 'speed'], dtype='object')
 
date_data = df.date 

data_converted = pd.to_datetime(date_data)

df.insert(0, 'converted_date', data_converted) # 0 is column position

print(df)

#   converted_date             date  runner_id  speed
# 0     2014-10-13  20141013T000000          1    121
# 1     2014-12-09  20141209T000000          2     97
# 2     2015-02-25  20150225T000000         12     86
# 3     2014-12-09  20141209T000000         45     93
# 4     2015-02-18  20150218T000000         54    100
# 5     2015-02-25  20150225T000000         17     45
# 6     2015-02-25  20150225T000000         99    101
# 7     2015-02-25  20150225T000000         50     49
# 8     2015-02-25  20150225T000000          7     65
# 9     2015-02-25  20150225T000000         87     92
