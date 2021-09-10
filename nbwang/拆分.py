from datetime import datetime
from os import getgroups
import pandas as pd
from pandas.core import indexing
from pandas.core.indexing import convert_to_index_sliceable
# df = pd.DataFrame()
# print(df)
# file_path = r'./202105.xlsx'
# df = pd.read_excel(file_path, sheet_name = "Sheet1")
# print(df["日期"])
# print(df.describe())
# print(df.info())
# readexcel 

def readexcel(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name = sheet_name)

df1 = readexcel('/Users/wangwenyan/Desktop/python/202105.xlsx','Sheet1')
# print(df1)
# df_rb = df1[df1['单位名称'] == '人保']
# print(df_rb['未税金额'].mean().round(2))
# cols = ['单价','未税金额','税额']
# for each in cols:
#    print(df_rb[each].sum().round(2)) 
df2 = df1.groupby('发票号码')
df1['合计'] = df2['未税金额'].transform('sum')
df1['日期'] = df1['日期'].apply(lambda x: str(pd.to_datetime(x).date()))
# for group in df2:
#     print(name)
#     print(group)
class_list = list(df1['发票号码'].drop_duplicates())
for i in class_list:
    df1_1 = df1[df1['发票号码']==i]
    df1_1.to_excel('./%s.xlsx'%(i))

    
