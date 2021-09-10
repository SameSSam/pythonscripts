import pandas as pd 
from config import DATA_DICT

#需要合并两个inventory file:
def get_inventory_df():
    cols = []
    df_igi = pd.read_excel(DATA_DICT['INVENTORY_FILE_IGI'],header=1)
    # df_gia = pd.read_excel(DATA_DICT['INVENTORY_FILE_GIA'],header=1)

    return df_igi

#数据如下
'''
        货号    分数   形状    证书    证书号    重量   颜色  净度  切工 抛光 对称 荧光 台宽比 全深比  尺寸                培育 处理
0       C3470  1.0  Radiant  IGI  LG459109533  1.15  FVY  SI1   VG  VG  VG  N  63.0  65.7    5.95 - 5.80 X 3.81  HPHT  N
1       C3478  1.0  Radiant  IGI  LG459109541  1.19  FVY  VS1   VG  VG  VG  N  63.5  67.5    6.57 - 5.63 X 3.80  HPHT  N
2       C3485  1.0  Radiant  IGI  LG459109548  1.07  FIY  VS2   VG  VG  VG  N  64.0  66.6    5.93 - 5.45 X 3.63  HPHT  N
3       C3486  1.0  Cushion  IGI  LG459109549  1.00   FY  VS2   GD  EX  VG  N  61.0  67.0    5.89 - 5.76 X 3.86  HPHT  N
4       C4363  1.0  Emerald  IGI  LG470153083  1.04  FIY  SI1   VG  VG  VG  N  59.5  61.8    6.83 - 5.05 X 3.12  HPHT  N
'''

#dp_price如下
'''
 钻色	条件	形状	证书	分数	净度	颜色	切工	抛光	对称	价格
1	白钻	3VG+	Round	GIA	0.5	IF	D	VG	VG	VG	23155

'''
if __name__ == '__main__':
    df = get_inventory_df()
    print(df)