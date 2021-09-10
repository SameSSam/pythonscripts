
import os#导入os
import pandas as pd
path='/Users/wangwenyan/Desktop/python/输出'
files_list=os.listdir(path)#获取目标文件夹内各文件的名称
print(files_list)

file=files_list
li=[]
for i in file:
    li.append(pd.read_excel(i))
writer = pd.ExcelWriter('/Users/wangwenyan/Desktop/python/ouput.xlsx')
pd.concat(li).to_excel(writer,'Sheet1',index=False)
 
writer.save()



