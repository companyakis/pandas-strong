import pandas as pd

data_path = "./fakedata.csv"

df = pd.read_csv(data_path) 

# print(df.columns) # Index(['date', 'runner_id', 'speed'], dtype='object')
 
# speed plus 5

new_speed_data = df["speed"] + 5

df.insert(3, "speed_plus_five", new_speed_data)

print(df)

"""
            date      runner_id  speed  speed_plus_five
0  20141013T000000          1    121              126
1  20141209T000000          2     97              102
2  20150225T000000         12     86               91
3  20141209T000000         45     93               98
4  20150218T000000         54    100              105
5  20150225T000000         17     45               50
6  20150225T000000         99    101              106
7  20150225T000000         50     49               54
8  20150225T000000          7     65               70
9  20150225T000000         87     92               97

"""


