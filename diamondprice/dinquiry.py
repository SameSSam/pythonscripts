import pandas as pd
import os

from config import DATA_DICT
from picklelist import df_blocks
from dataframes import run_once
from inventory import get_inventory_df

#更改目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#如果目录下已经有pickle文件存在，则不运行，否则运行run_once
if not os.path.isfile('block_df0.pk0'):
    run_once()

def price_search(diamond_in,shape_in, cert_in, crafts_in_lst,carat_in,color_in,purity_in):
    blocks = df_blocks()
    #首先输入形状，马上进行列表内字典对形状的检索，形状从用户获取输入shape_in,cert_in
    # #接受用户输入工艺craft,需要计算EX和VG的个数
    crafts = crafts_in_lst
    ex_num = crafts.count('EX')
    vg_num = crafts.count('VG')

    r_blocks = []  
    results = []
    #blocks列表长度为22，包括一个元素重复使用

    if diamond_in == '白钻':
    ################################################################################################# 
    #如果shape_in和证书为Round和GIA的情况，需要考虑三个单独的情况
        if (shape_in == 'Round') & (crafts == ['EX','VG','VG'] ):
            #先比较三个顺序相等，因为只有两个元素，各自比较即可
            if( cert_in == 'GIA'):
                results.append(blocks[1])
            elif (cert_in == 'IGI'):
                results.append(blocks[3])  
    #################################################################################################
    #如果是白钻，搜索前面的14个记录，如果是黄钻，搜搜后面的8个记录即可（记录即保存的pickle文件)
    for block in (lambda:blocks[0:14] if (diamond_in == '白钻') else blocks[14:22])():
        # print(block.get('shape'))
        if (shape_in in block.get('shape')) & (cert_in in block.get('cert')): 
            r_blocks.append(block)
    # print(r_blocks)

    for block in r_blocks:
        if (ex_num == block.get('craft')['EX']) | (vg_num == block.get('craft')['VG']):
            print(block)
            results.append(block)

   #针对上一步找到的记录，找出对应的价格
    df_price = pd.DataFrame(index = [0], columns=DATA_DICT['COLUMNS_NAME'])
    if len(results) != 0:
        for item in results:
            # data_r = item['data']
            pickle_file = item['data']
            data_r = pd.read_pickle(pickle_file)
            # print(data_r['分数'])
            data_r['条件'] = item['condition']
            result = data_r[(data_r['分数'] == carat_in) & (data_r['净度'] == purity_in) & (data_r['颜色'] == color_in)]
           
            
            df_price = df_price.append(result,ignore_index=True)
            # print(df_price)
    if df_price.empty:
        print("无法找到对应的报价信息，请重新输入查询条件！")
    else:
        #打印或者其他处理结果的方法
        df_price.drop(index=0,inplace=True)
        df_price['钻色'] = diamond_in
        df_price['形状'] = shape_in
        df_price['证书'] = cert_in
        df_price['切工'] = crafts_in_lst[0]
        df_price['抛光'] = crafts_in_lst[1]
        df_price['对称'] = crafts_in_lst[2]
         
    return df_price
#以上price_search从报价单上找到满足条件的对应的报价

#以下函数为不定义craft的模糊查询，取消craft参数
#update by Sam 2021.07.31
def price_search_no_craft(diamond_in,shape_in, cert_in, carat_in,color_in,purity_in):
    blocks = df_blocks()
    #首先输入形状，马上进行列表内字典对形状的检索，形状从用户获取输入shape_in,cert_in
    # #接受用户输入工艺craft,需要计算EX和VG的个数

    # r_blocks = []  
    results = []
    #blocks列表长度为22，包括一个元素重复使用

   #注释掉以下代码，不去查询craft
    # if diamond_in == '白钻':
    #     ################################################################################################# 
    # #如果shape_in和证书为Round和GIA的情况，需要考虑三个单独的情况
    #     if (shape_in == 'Round') & (crafts == ['EX','VG','VG'] ):
    #         #先比较三个顺序相等，因为只有两个元素，各自比较即可
    #         if( cert_in == 'GIA'):
    #             results.append(blocks[1])
    #         elif (cert_in == 'IGI'):
    #             results.append(blocks[3])  
    # #################################################################################################

    #如果是白钻，搜索前面的14个记录，如果是黄钻，搜搜后面的8个记录即可（记录即保存的pickle文件)
    for block in (lambda:blocks[0:14] if (diamond_in == '白钻') else blocks[14:22])():
        # print(block.get('shape'))
        if (shape_in in block.get('shape')) & (cert_in in block.get('cert')): 
            # r_blocks.append(block)
            results.append(block)
    # print(results)

#注释掉以下代码，不去查询craft
    # for block in r_blocks:
    #     if (ex_num == block.get('craft')['EX']) | (vg_num == block.get('craft')['VG']):
    #         print(block)
    #         results.append(block)

   #针对上一步找到的记录，找出对应的价格
    df_price = pd.DataFrame(index = [0], columns=DATA_DICT['COLUMNS_NAME'])
    if len(results) != 0:
        for item in results:
            # data_r = item['data']
            pickle_file = item['data']
            data_r = pd.read_pickle(pickle_file)
            # print(data_r['分数'])
            data_r['条件'] = item['condition']
            result = data_r[(data_r['分数'] == carat_in) & (data_r['净度'] == purity_in) & (data_r['颜色'] == color_in)]

            
            df_price = df_price.append(result,ignore_index=True)
            # print(df_price)
    if df_price.empty:
        print("无法找到对应的报价信息，请重新输入查询条件！")
    else:
        #打印或者其他处理结果的方法
        df_price.drop(index=0,inplace=True)
        df_price['钻色'] = diamond_in
        df_price['形状'] = shape_in
        df_price['证书'] = cert_in
        # df_price['切工'] = crafts_in_lst[0]
        # df_price['抛光'] = crafts_in_lst[1]
        # df_price['对称'] = crafts_in_lst[2]
         
    return df_price
#以上price_search从报价单上找到满足条件的对应的报价


#以下函数继续根据找到的报价去搜索对应的库存货品
   
def inventory_search(df_price):
    df_inventory = get_inventory_df()
    #增加两列各为工艺EX和VG的计数
    #对得到的df进行一些初步的整理
    df_c = df_inventory[['切工','抛光','对称']]
    
    ex_num = df_c[df_c == 'EX'].count(axis = 1).to_list()
    vg_num = df_c[df_c == 'VG'].count(axis = 1).to_list()
    df_inventory['EX计数'] = ex_num
    df_inventory['VG计数'] = vg_num
    df_inventory['条件'] = ''

    fixed = df_c[(df_c['切工'] == 'EX') & (df_c['抛光'] == 'VG') & (df_c['对称'] == 'VG')] 
    for index in fixed.index.tolist():
        df_inventory.loc[index,'条件'] = 'FIXED'
    
    df_fixed = df_inventory[df_inventory['条件'] == 'FIXED']

    results = pd.DataFrame(index=[0],columns=df_inventory.columns)
    #根据price_search函数找到的报价结果，来搜索对应的商品记录

    if not df_price.empty:
        #直接对df_price进行循环,为防止索引出现错误，使用iloc定位
        for row in range(len(df_price)):
            if df_price.iloc[row]['条件'] == 'FIXED':
                data_r = df_fixed[(df_fixed['分数'] == float(df_price.iloc[row]['分数'])) & (df_fixed['颜色'] == df_price.iloc[row]['颜色']) & (df_fixed['证书'] == df_price.iloc[row]['证书']) &(df_fixed['净度'] == df_price.iloc[row]['净度'])]
            else:
                data_r = df_inventory[(df_inventory['分数'] == float(df_price.iloc[row]['分数'])) & (df_inventory['颜色'] == df_price.iloc[row]['颜色']) & (df_inventory['证书'] == df_price.iloc[row]['证书']) &(df_inventory['净度'] == df_price.iloc[row]['净度'])]   
                data_r = data_r[((data_r['EX计数'] == int(df_price.iloc[row]['条件'][0:1])) & (df_price.iloc[row]['条件'][1:] == 'EX')) | ((data_r['VG计数'] == int(df_price.iloc[row]['条件'][0:1])) & (df_price.iloc[row]['条件'][1:] == 'VG+'))]
            data_r['条件'] = df_price.iloc[row]['条件']
            data_r['单价'] = int(df_price.iloc[row]['单价'])
            data_r['市场价'] = data_r['单价']*data_r['重量']*1.05
            results = pd.concat([results,data_r],axis=0,ignore_index=True,join='outer')

        if not results.empty:
            results.drop(0,inplace=True)
        
        #确定显示列数
        show_cols = ['货号', '分数', '形状', '证书', '证书号', '尺寸', '台宽比', '全深比',  '净度', '颜色','切工', '抛光', '对称', '重量', '培育', '条件', '单价', '市场价' ]
        # print(show_cols)
        #小数点重新设置
        cols = ['分数','重量','台宽比','全深比','单价','市场价']
        results[cols] = results[cols].applymap(lambda x:('%.2f')%x)
        results['单价'] = results['单价'].astype(float).astype(int)
        results['市场价'] = results['市场价'].astype(float).astype(int)   
        # print(results[show_cols])
        return results[show_cols]
    else:
        "无法找到相应的报价！"
#以下函数支持没有craft的模糊查询
#update by Sam 2021.07.31
def inventory_search_no_craft(df_price):
    df_inventory = get_inventory_df()

#以下代码注释掉，支持没有craft的模糊查询
    # #增加两列各为工艺EX和VG的计数
    # #对得到的df进行一些初步的整理
    # df_c = df_inventory[['切工','抛光','对称']]
    
    # ex_num = df_c[df_c == 'EX'].count(axis = 1).to_list()
    # vg_num = df_c[df_c == 'VG'].count(axis = 1).to_list()
    # df_inventory['EX计数'] = ex_num
    # df_inventory['VG计数'] = vg_num

    df_inventory['条件'] = ''

#以下代码注释掉
    # fixed = df_c[(df_c['切工'] == 'EX') & (df_c['抛光'] == 'VG') & (df_c['对称'] == 'VG')] 
    # for index in fixed.index.tolist():
    #     df_inventory.loc[index,'条件'] = 'FIXED'
    
    # df_fixed = df_inventory[df_inventory['条件'] == 'FIXED']

    results = pd.DataFrame(index=[0],columns=df_inventory.columns)
    #根据price_search函数找到的报价结果，来搜索对应的商品记录

    if not df_price.empty:
        #直接对df_price进行循环,为防止索引出现错误，使用iloc定位
        # #这里已经可以不用for循环，因为对四个指标的搜索一次性就够了。

        for row in range(len(df_price)):
            # if df_price.iloc[row]['条件'] == 'FIXED':
            #     data_r = df_fixed[(df_fixed['分数'] == float(df_price.iloc[row]['分数'])) & (df_fixed['颜色'] == df_price.iloc[row]['颜色']) & (df_fixed['证书'] == df_price.iloc[row]['证书']) &(df_fixed['净度'] == df_price.iloc[row]['净度'])]
            # else:
            #     data_r = df_inventory[(df_inventory['分数'] == float(df_price.iloc[row]['分数'])) & (df_inventory['颜色'] == df_price.iloc[row]['颜色']) & (df_inventory['证书'] == df_price.iloc[row]['证书']) &(df_inventory['净度'] == df_price.iloc[row]['净度'])]   
            #     data_r = data_r[((data_r['EX计数'] == int(df_price.iloc[row]['条件'][0:1])) & (df_price.iloc[row]['条件'][1:] == 'EX')) | ((data_r['VG计数'] == int(df_price.iloc[row]['条件'][0:1])) & (df_price.iloc[row]['条件'][1:] == 'VG+'))]
            data_r = df_inventory[(df_inventory['分数'] == float(df_price.iloc[row]['分数'])) & (df_inventory['颜色'] == df_price.iloc[row]['颜色']) & (df_inventory['证书'] == df_price.iloc[row]['证书']) &(df_inventory['净度'] == df_price.iloc[row]['净度'])]
            data_r = data_r.copy()
            data_r['条件'] = df_price.iloc[row]['条件']
            data_r['单价'] = int(df_price.iloc[row]['单价'])
            data_r['市场价'] = data_r['单价']*data_r['重量']*1.05
            results = pd.concat([results,data_r],axis=0,ignore_index=True,join='outer')

      
        if not results.empty:
            results.drop(0,inplace=True)
        
        #确定显示列数
        show_cols = ['货号', '分数', '形状', '证书', '尺寸', '净度', '颜色','切工', '抛光', '对称', '重量', '培育', '市场价' ]
        # print(show_cols)
        # print(results[show_cols])
        #小数点重新设置
        cols = ['分数','重量','台宽比','全深比','单价','市场价']
        results[cols] = results[cols].applymap(lambda x:('%.2f')%x)
        results['单价'] = results['单价'].astype(float).astype(int)
        results['市场价'] = results['市场价'].astype(float).astype(int)   
        # print(results.info())
        results.drop_duplicates('货号',keep='first',inplace=True)

        return results[show_cols]
    else:
        return "无法找到相应的报价！"        

# def df_inventory_table():
#     df_tmp = get_inventory_df().head(10)
#     cols = ['分数','重量','台宽比','全深比']
#     df_tmp[cols] = df_tmp[cols].applymap(lambda x:('%.2f')%x)
#     return df_tmp