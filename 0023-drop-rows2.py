import pandas as pd

data_path = "./sales_data.csv"

df = pd.read_csv(data_path)

df.drop(labels = [2 * i + 1 for i in range(5)], inplace = True) # 1, 3, 5, 7, 9

print(df.iloc[:, :5].head(20))

#           Date  Day      Month  Year  Customer_Age
# 0   2013-11-26   26   November  2013            19
# 2   2014-03-23   23      March  2014            49
# 4   2014-05-15   15        May  2014            47
# 6   2014-05-22   22        May  2014            47
# 8   2014-02-22   22   February  2014            35
# 10  2013-07-30   30       July  2013            32
# 11  2015-07-30   30       July  2015            32
# 12  2013-07-15   15       July  2013            34
# 13  2015-07-15   15       July  2015            34
# 14  2013-08-02    2     August  2013            29
# 15  2015-08-02    2     August  2015            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 17  2015-09-02    2  September  2015            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 16  2013-09-02    2  September  2013            29
# 17  2015-09-02    2  September  2015            29
# 18  2014-01-22   22    January  2014            29
# 19  2016-01-22   22    January  2016            29
# 20  2014-05-17   17        May  2014            29
# 21  2016-05-17   17        May  2016            29
# 22  2014-03-27   27      March  2014            51
# 23  2016-03-27   27      March  2016            51
# 24  2013-08-25   25     August  2013            49
