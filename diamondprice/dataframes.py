import pandas as pd 
from config import DATA_DICT


src_file = DATA_DICT['SRC_FILE']
columns_name= DATA_DICT['COLUMNS_NAME']
carat_lst = DATA_DICT['CARAT_LST']

#后续block_df()函数用到
def range_cell(header,cols,rows):
    data = pd.read_excel(src_file,header=header,usecols=cols,nrows=rows,names=['Carat'] + DATA_DICT['COLORS_NAME'] )
    #读取时直接更改列名    
    return data

#创建表格转换函数，把excel中价格显示转变成df形式
def df_transfer(carat,df,rows):
    unit_df = pd.DataFrame(index= range(1,(rows*6+1)),columns=columns_name)
    #重新组合数据
    unit_df['分数'] = carat
    counter = 0
    for row in range(rows):
        for col in DATA_DICT['COLORS_NAME']:
            counter += 1
            unit_df.loc[counter]['净度']=df.iloc[row,0]
            unit_df.loc[counter]['颜色']=col
            #价格*3
            unit_df.loc[counter]['单价']=int((df.loc[row][col] *3).round())
    return unit_df

#把原先EXCEL文件分区块，按横向从上到下逐个进行转换，得到一个区块列表，每个列表元素保存有df的pickle文件路径
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

#构建df转换到pickle函数,把上面的函数block_df对每个横向区块运行(13),然后保存为pickle格式，用以提升性能
def block_df_pickle():
    block_df_lst = []
    prefix_c = 'block_df'
    for i in range(21):
        if i > 12:
            prefix_c = 'yblock_df'
        pickle_name = prefix_c + str(i) + '.pk' + str(i)
        print(pickle_name)
        block_df(i).to_pickle(pickle_name)
        block_df_lst.append(pickle_name)
    # for k in range(13,21):
    #     pickle_name = 'yblock_df' + str(k) +'.pk' + str(k)
    #     print(pickle_name)
    #     block_df(k).to_pickle(pickle_name)
    #     block_df_lst.append(pickle_name)
    return block_df_lst



def run_once():
    block_df_pickle()

if __name__ == '__main__':
    run_once()