# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
import pandas as pd
src_file = 'dprice.xlsx'

# %% [markdown]
# ### 读取指定范围单元格数据

# %%
columns_name=['形状','证书','分数','净度','颜色','切工','抛光','对称','价格']


# %%
#后续block_df()函数用到
def range_cell(header,cols,rows):
    data = pd.read_excel(src_file,header=header,usecols=cols,nrows=rows,names=['Carat','D','E','F','G','H','I'])
    #读取时直接更改列名    
    return data


# %%
col_names = ['D','E','F','G','H','I'] 
#cols = [x for x in range(1,8)]
df_cell = range_cell(3,range(1,8),7)
df_cell = df_cell.round()
df_cell


# %%
i=0
df_cell = range_cell(3,range(i*8+1,8+i*8),7)  #range(1+i*8,8+i*8)
df_cell


# %%

carat_lst = ['0.5','0.7','0.9','1','1.2','1.5','2.0','3.0','4.0','5.0']    #分数
col_names = ['D','E','F','G','H','I']    #color颜色
# carat = '0.5'


# %%
def df_transfer(carat,df,rows):
    unit_df = pd.DataFrame(index= range(1,(rows*6+1)),columns=columns_name)
    #重新组合数据
    unit_df['分数'] = carat
    counter = 0
    for row in range(rows):
        for col in col_names:
            counter += 1
            unit_df.loc[counter]['净度']=df.iloc[row,0]
            unit_df.loc[counter]['颜色']=col
            unit_df.loc[counter]['价格']=int(df.loc[row][col].round())
    return unit_df


# %%
df = pd.DataFrame(index = [0],columns=columns_name)
#前面四段有规律
for i in range(4):
    block_data1 = range_cell(3+i*11,"B:H",7)
    # print(block_data1)
    data = df_transfer(carat_lst[i],block_data1,7)
    # print(data)
    df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')
    # df = df.append(data)
#中间carat1.2单独计算
block_data2 = range_cell(47,"B:H",6)
# print(block_data2)
data = df_transfer(carat_lst[4],block_data2,6)
# print(data)
df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')

#第三段数据处理
for i in range(2):
    block_data3 = range_cell(57+i*10,"B:H",7)
    data = df_transfer(carat_lst[5+i],block_data3,7)
    df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')

#第四段数据处理
for i in range(3):
    block_data4= range_cell(78+i*11,"B:H",7)
    data = df_transfer(carat_lst[7+i],block_data4,7)
    df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')    
df.drop(index=0,inplace=True)
print(df.head(10))


# %%
#整理上述算法为一个函数
def block_df(block_counter):
    df = pd.DataFrame(index = [0],columns=columns_name)
    #前面四段有规律
    for i in range(4):
        block_data1 = range_cell(3+i*11,range(1+block_counter*8,8+block_counter*8),7)
        # print(block_data1)
        data = df_transfer(carat_lst[i],block_data1,7)
        # print(data)
        df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')
        # df = df.append(data)
    #中间carat1.2单独计算
    block_data2 = range_cell(47,range(1+block_counter*8,8+block_counter*8),6)
    # print(block_data2)
    data = df_transfer(carat_lst[4],block_data2,6)
    # print(data)
    df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')

    #第三段数据处理
    for i in range(2):
        block_data3 = range_cell(57+i*10,range(1+block_counter*8,8+block_counter*8),7)
        data = df_transfer(carat_lst[5+i],block_data3,7)
        df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')

    #第四段数据处理
    for i in range(3):
        block_data4= range_cell(78+i*11,range(1+block_counter*8,8+block_counter*8),7)
        data = df_transfer(carat_lst[7+i],block_data4,7)
        df = pd.concat([df,data],axis=0,ignore_index=True,join='outer')
    df.drop(index=0,inplace=True)
      
    return df


# %%
#创建block的pickle list, 给每个区域块都另存为Pickle，以提高后续读取性能 date:2021.07.27
#需要前面的函数block_df()
block_df_lst = []
for i in range(13):
    pickle_name = 'block_df' + str(i) + '.pk' + str(i)
    print(pickle_name)
    block_df(i).to_pickle(pickle_name)
    block_df_lst.append(pickle_name)
print(block_df_lst)


# %%
#代码段测试
block = []
#01.第一区域
block.append({
    'shape': ['Round'],
    'cert':  ['GIA'],
    'craft':{'EX':3},
    'data': block_df_lst[12]
})
data_r = pd.read_pickle(block[0]['data'])
data_r


# %%
#全部区域创建成一个数组，每个数组包含形状，证书，工艺，数据(报价包含在data里,data保存有pickle文件指向，需要的时候进行读取)
blocks = []
#01.第一区域
blocks.append( {
    'shape': ['Round'],
    'cert':  ['GIA'],
    'craft':{'EX':3,'VG':None},
    'data': block_df_lst[0]
})
#02.第二区域
blocks.append({
    'shape': ['Round'],
    'cert':  ['GIA'],
    'craft':{'C01':'EX','C02':'VG','C03':'VG','EX':None,'VG':None},
    'data': block_df_lst[1]
})
#03.第三区域excel表中为第三栏 Round GIA 3VG+/IGI 3EX, 拆成两个不同的元素，对应到同一个pickle
blocks.append({
    'shape': ['Round'],
    'cert':  ['GIA'],
    'craft': {'VG':3,'EX':None},
    'data': block_df_lst[2]
})
#04.第四区域
blocks.append({
    'shape': ['Round'],
    'cert':  ['IGI'],
    'craft':{'C01':'EX','C02':'VG','C03':'VG','EX':None,'VG':None},
    'data': block_df_lst[3]
})

#05.第五区域AH ROUND IGI 3VG+
blocks.append({
    'shape': ['Round'],
    'cert':  ['IGI'],
    'craft':{'VG':3,'EX':None},
    'data': block_df_lst[4]
})

#06.第六区域AP Pear/Oval/Heart/MQ GIA 2EX
blocks.append({
    'shape': ['Pear','Oval','Heart','MQ'],
    'cert':  ['GIA'],
    'craft':{'EX':2,'VG':None},
    'data': block_df_lst[5]
})

#07.第七区域AX Pear/Oval/Heart/MQ GIA VG+ 至少一个VG
blocks.append({
    'shape': ['Pear','Oval','Heart','MQ'],
    'cert':  ['GIA'],
    'craft':{'VG':1,'EX':None},
    'data': block_df_lst[6]
})
#08.第八区域BF Pear/Oval/Heart/MQ IGI 2EX
blocks.append({
    'shape': ['Pear','Oval','Heart','MQ'],
    'cert':  ['IGI'],
    'craft':{'EX':2,'VG':None},
    'data': block_df_lst[7]
})

#09.第九区域BN Pear/Oval/Heart/MQ IGI VG+ 至少一个VG
blocks.append({
    'shape': ['Pear','Oval','Heart','MQ'],
    'cert':  ['IGI'],
    'craft':{'VG':1,'EX':None},
    'data': block_df_lst[8]
})

#10.第十区域BV Cushion...  GIA 2EX
blocks.append({
    'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
    'cert':  ['GIA'],
    'craft':{'EX':2,'VG':None},
    'data': block_df_lst[9]
})
#11.第十一区域CD Cushion...  GIA VG+
blocks.append({
    'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
    'cert':  ['GIA'],
    'craft':{'VG':1,'EX':None},
    'data': block_df_lst[10]
})
#12.第十二区域CL Cushion...  IGI 2EX
blocks.append({
    'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
    'cert':  ['IGI'],
    'craft':{'EX':2,'VG':None},
    'data': block_df_lst[11]
})
#13.第十三区域CT Cushion...  IGI VG+
blocks.append({
    'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
    'cert':  ['IGI'],
    'craft':{'VG':1,'EX':None},
    'data': block_df_lst[12]
})
#14.来自于第三个的分拆
blocks.append({
    'shape': ['Round'],
    'cert':  ['IGI'],
    'craft': {'EX':3,'VG':None},
    'data': block_df_lst[2]
})

# %%
#首先输入形状，马上进行列表内字典对形状的检索，形状从用户获取输入shape_in,cert_in
shape_in = 'Cushion'
cert_in = 'IGI'


# #接受用户输入工艺craft,需要计算EX和VG的个数
craft_in1 = 'EX'
craft_in2 = ''
craft_in3 = 'EX'

crafts = [craft_in1,craft_in2,craft_in3]
ex_num = crafts.count('EX')
vg_num = crafts.count('VG')

r_blocks = []  
results = []

#如果shape_in和证书为Round和GIA的情况，需要考虑三个单独的情况
if (shape_in == 'Round') & (crafts == ['EX','VG','VG'] ):
    #先比较三个顺序相等，因为只有两个元素，各自比较即可
    if( cert_in == 'GIA'):
        results.append(blocks[1])
    elif (cert_in == 'IGI'):
        results.append(blocks[3])
    
#################################################################################################
for block in blocks:
    # print(block.get('shape'))
    if (shape_in in block.get('shape')) & (cert_in in block.get('cert')): 
        r_blocks.append(block)
# print(r_blocks)

for block in r_blocks:
    if (ex_num == block.get('craft')['EX']) | (vg_num == block.get('craft')['VG']):
        print(block)
        results.append(block)

################################################################################################# 


# %%
#2021.07.28 处理颜色和分数等以获取报价
#获取用户输入
carat_in = '0.5'
color_in = 'E'
purity_in = 'IF'

#针对上一步找到的记录，找出对应的价格
df_price = pd.DataFrame(index = [0], columns=columns_name)
if len(results) != 0:
    for item in results:
        # data_r = item['data']
        data_r = pd.read_pickle(item['data'])
        # print(data_r['分数'])
        result = data_r[(df['分数'] == carat_in) & (df['净度'] == purity_in) & (df['颜色'] == color_in)]
        # print(result)
        df_price = df_price.append(result,ignore_index=True)
        # print(df_price)
if df_price.empty:
    print("无法找到对应的报价信息，请重新输入查询条件！")
else:
    #打印或者其他处理结果的方法
    df_price.drop(index=0,inplace=True)
    df_price['形状'] = shape_in
    df_price['证书'] = cert_in
    df_price['切工'] = craft_in1
    df_price['抛光'] = craft_in2
    df_price['对称'] = craft_in3

df_price 

# %%
df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)],
                  columns=['dogs', 'cats'])
df.dtypes


