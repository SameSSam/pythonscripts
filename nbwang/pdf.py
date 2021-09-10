from reportlab.lib import pagesizes
from reportlab.rl_config import defaultPageSize
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('hei', 'SIMHEI.TTF'))
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, LongTable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A5, landscape
from io import BytesIO
from datetime import datetime
import pandas as pd
from pandas.core import indexing
from pandas.core.indexing import convert_to_index_sliceable


def readexcel(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name = sheet_name)

df1 = readexcel('202105.xlsx','Sheet1')


table_data1 = []
cols = ['发票号码','单位名称','商品名称']


df = df1[cols]
df['发票号码'] = df['发票号码'].astype(str)
# print(df.info())
for row in range(len(df)):
    table_data1.append(df.iloc[row].to_list())

print(table_data1)


stylesheet = getSampleStyleSheet()   # 获取样式集
 
# 获取reportlab自带样式
Normal = stylesheet['Normal']
BodyText = stylesheet['BodyText']
Italic = stylesheet['Italic']
Title = stylesheet['Title']
Heading1 = stylesheet['Heading1']
Heading2 = stylesheet['Heading2']
Heading3 = stylesheet['Heading3']
Heading4 = stylesheet['Heading4']
Heading5 = stylesheet['Heading5']
Heading6 = stylesheet['Heading6']
Bullet = stylesheet['Bullet']
Definition = stylesheet['Definition']
Code = stylesheet['Code']

# 自带样式不支持中文，需要设置中文字体，但有些样式会丢失，如斜体Italic。有待后续发现完全兼容的中文字体
Normal.fontName = 'hei'
# Italic.fontName = 'hei'
BodyText.fontName = 'hei'
Title.fontName = 'hei'
Heading1.fontName = 'hei'
Heading2.fontName = 'hei'
Heading3.fontName = 'hei'
Heading4.fontName = 'hei'
Heading5.fontName = 'hei'
Heading6.fontName = 'hei'
Bullet.fontName = 'hei'
Definition.fontName = 'hei'
Code.fontName = 'hei'
 
 
# 添加自定义样式
stylesheet.add(
    ParagraphStyle(name='body',
                   fontName='hei',
                   fontSize=10,
                   textColor='black',
                   leading=20,                # 行间距
                   spaceBefore=0,             # 段前间距
                   spaceAfter=10,             # 段后间距
                   leftIndent=0,              # 左缩进
                   rightIndent=0,             # 右缩进
                   firstLineIndent=20,        # 首行缩进，每个汉字为10
                   alignment=TA_JUSTIFY,      # 对齐方式
 
                   # bulletFontSize=15,       #bullet为项目符号相关的设置
                   # bulletIndent=-50,
                   # bulletAnchor='start',
                   # bulletFontName='Symbol'
                   )
            )
body = stylesheet['body']

story = []

table_data = [['year我是标题行，\n\n比较特殊，不能上下居中\n', '我的背景色被绿了', '我是标题，我比别人大\n'],
              ['2017\n我是换行符，\n单元格中的字符串只能用我换行', '3', '12'],
              [Paragraph('指定了列宽，可以在单元格中嵌入paragraph进行自动换行，不信你看我', body), '4', '13'],
              ['2017', '5', '我们是表格'],
              ['2017', '我是伪拆分单元格，\n通过合并前hou两个兄弟得到', '15'],
              ['2018', '7', '16'],
              [Paragraph('content1', body), '8', [ Paragraph('这样我可以在一个单元格内同时显示图片和paragraph', body)]],
              ['2018', '我们被合并了，合并的值为右上角单元格的值', '18'],
              ['我被绿了', '10', '19'],
              ]
table_style = [
    ('FONTNAME', (0, 0), (-1, -1), 'hei'),  # 字体
    ('FONTSIZE', (0, 0), (-1, 0), 15),  # 第一行的字体大小
    ('FONTSIZE', (0, 1), (-1, -1), 10),  # 第二行到最后一行的字体大小
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 所有表格左右中间对齐
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # 所有表格上下居中对齐
 
    ('SPAN', (-2, -2), (-1, -1)),  # 合并
    ('SPAN', (0, 4), (0, 5)),  # 合并
    ('SPAN', (2, 4), (2, 5)),  # 合并
    ('BACKGROUND', (0, 0), (-1, 0), colors.green),  # 设置第一行背景颜色
    ('TEXTCOLOR', (0, -1), (0, -1), colors.green),  # 设置表格内文字颜色
    ('GRID', (0, 0), (-1, -1), 0.1, colors.black),  # 设置表格框线为灰色，线宽为0.1
]


table = Table(data=table_data1,style=table_style, colWidths=180)


story.append(table)

doc = SimpleDocTemplate('hello.pdf',pagesize=landscape(A5))

doc.build(story)