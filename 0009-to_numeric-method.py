import pandas as pd

data_path = "./fakedata.csv"

df = pd.read_csv(data_path) # speed data example => string "121"

print(df.columns) # Index(['runner_id', 'speed'], dtype='object')

speed_data = df.speed

numeric_speed_data = pd.to_numeric(speed_data)

print(numeric_speed_data)

# 0    121
# 1     97
# 2     86
# 3     93
# 4    100
# 5     45
# 6    101
# 7     49
# 8     65
# 9     92
# Name: speed, dtype: int64

