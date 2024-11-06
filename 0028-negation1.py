import pandas as pd

dummy = pd.Series([True, True, True, False, False, True])

print(~dummy)

# 0    False 
# 1    False 
# 2    False 
# 3     True 
# 4     True 
# 5    False 
# dtype: bool
