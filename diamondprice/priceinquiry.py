# from pricequiry.dinquiry import inventory_search_no_craft, price_search_no_craft
from dataframes import run_once
import streamlit as st
import pandas as pd
import os

from dinquiry import price_search,inventory_search,inventory_search_no_craft, price_search_no_craft


st.title("培育钻查价系统V0.1")
st.subheader('本系统为公司内部员工询价使用')

# print(os.getcwd())

#定义获取数据列表 
diamond_color = ['白钻','黄钻']
shape_lst = ['Round 圆钻明亮型','Pear 水滴型','Oval 椭圆形','Heart 心形','MQ 马眼型','Cushion 垫型(枕型)','Radiant 雷迪恩','Emerald 祖母类型','Assher 阿斯切','Princess 公主方']   #形状
carat_lst = ['0.5','0.7','0.9','1','1.2','1.5','2.0','3.0','4.0','5.0']    #分数：克拉
color_lst = ['D','E','F','G','H','I']    #颜色
cert_lst = ['GIA','IGI']      #证书
craft_lst = ['GD','VG','EX']       #工艺： 切工，抛光，对称
purity_lst = ['IF','VVS1','VVS2','VS1','VS2','SI1','SI2']    #净度
shape_r = shape_lst[1:]

#用户输入字典,每一项都是列表存储
user_inputs = {
            "diamond":[],
            "shape":[],
            "carat":[],
            "color":[],
            "cert": [],
            "craft":['','',''],
            "purity":[]
}

#放置上传文件部件uploader，覆盖原先文件，重新进行数据整理，
#更改上传为一个函数，通过按钮来触发
if st.button('更新报价文件'):
    uploaded_file = st.file_uploader('报价如有更新，请重新上传文件:')
    if uploaded_file is not None:
        with open('uploaded_excel.xlsx','wb') as f:
            f.write(uploaded_file.getbuffer())
        os.remove('dprice.xlsx')
        os.rename('uploaded_excel.xlsx','dprice.xlsx')
        with st.spinner('正在重新生成搜索数据......'):
            run_once()
        st.success('数据整理完成！')

#形状，证书，分数选择
col1,col2,col3 = st.beta_columns(3)
user_inputs['diamond'].append(col1.selectbox('1. 钻石颜色', diamond_color))

#钻石颜色是黄色的。不支持选择圆形
if ('黄钻' in user_inputs['diamond']):
    shape_lst.pop(0)

#去除形状里中文部分的描述
shape_lst_en = [x.split(' ')[0] for x in shape_lst]
user_inputs['shape'].append(col2.selectbox('2. 形状',shape_lst)) 
user_inputs['cert'].append(col3.selectbox('3. 证书',cert_lst))

#取消这个判断，工艺会进行第二次搜索
# #如果选择是Round,工艺选择至于两项
# if ('Round' in user_inputs['shape']):
#     craft_lst.pop(0)
#净度，颜色选择

col4,col5,col6 = st.beta_columns(3)

user_inputs['carat'].append(col4.selectbox('4. 分数(克拉)',carat_lst))
user_inputs['purity'].append(col5.selectbox('5. 净度',purity_lst))
user_inputs['color'].append(col6.selectbox('6. 颜色',color_lst))

# if(("Round" in user_inputs['shape']) & (user_inputs['craft'].count('EX') == 2)):
#     st.error("圆形不支持选择等于两个EX的工艺！请重新选择工艺！")
#不是圆形的询价工艺只支持两种模式，即2EX和1个VG+，其他模式都不支持

# if user_inputs['shape'][0] in shape_r:
#     if (user_inputs['craft'].count('EX') !=2) and (user_inputs['craft'].count('VG')!=1):
#         #  | elif user_inputs['craft'].count('VG')!=1:
#         st.warning("非圆形钻只支持2EX或者1VG工艺组合查询！")
#         print(user_inputs['craft'])


#按钮时间绑定函数
#price_search(diamond_in,shape_in, cert_in, crafts_in_lst,carat_in,color_in,purity_in)
diamond_in = user_inputs['diamond'][0]
# shape_in = user_inputs['shape'][0]
#更改shape_in的值为保留英文部分
shape_in = user_inputs['shape'][0].split(' ')[0]
cert_in = user_inputs['cert'][0]
carat_in = user_inputs['carat'][0]
color_in = user_inputs['color'][0]
purity_in = user_inputs['purity'][0]

df_no_craft = price_search_no_craft(diamond_in,shape_in, cert_in, carat_in,color_in,purity_in)
if st.button('无指定工艺查询价格'):
    #输出查询结果df
    st.table(df_no_craft)

if st.button('无指定工艺查询货品'):
    result_data = inventory_search_no_craft(df_no_craft)
    st.table(result_data)
st.markdown('###### FIXED=EX+VG+VG')


col7,col8,col9 = st.beta_columns(3)

user_inputs['craft'][0] = col7.radio('7. 切工',craft_lst)
user_inputs['craft'][1] = col8.radio('8. 抛光',craft_lst) 
user_inputs['craft'][2] = col9.radio('9. 对称',craft_lst)  
crafts_in_lst = user_inputs['craft']

df = price_search(diamond_in,shape_in, cert_in, crafts_in_lst,carat_in,color_in,purity_in)
if st.button('指定工艺查询价格'):
    #输出查询结果df
    st.table(df)

if st.button('指定工艺查询货品'):
    result_data = inventory_search(df)
    st.table(result_data)

