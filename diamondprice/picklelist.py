#创建区块数组函数
def df_blocks():
    #全部区域创建成一个数组，每个数组包含形状，证书，工艺，数据(报价包含在data里,data保存有pickle文件指向，需要的时候进行读取)
    blocks = []
    #01.第一区域
    blocks.append( {
        'shape': ['Round'],
        'cert':  ['GIA'],
        'craft':{'EX':3,'VG':None},
        'condition':'3EX',
        'data': 'block_df0.pk0'
    })
    #02.第二区域
    blocks.append({
        'shape': ['Round'],
        'cert':  ['GIA'],
        'craft':{'C01':'EX','C02':'VG','C03':'VG','EX':None,'VG':None},
        'condition':'FIXED',
        'data': 'block_df1.pk1'
    })
    #03.第三区域excel表中为第三栏 Round GIA 3VG+/IGI 3EX, 拆成两个不同的元素，对应到同一个pickle
    blocks.append({
        'shape': ['Round'],
        'cert':  ['GIA'],
        'craft': {'VG':3,'EX':None},
        'condition':'3VG+',
        'data': 'block_df2.pk2'
    })
    #04.第四区域
    blocks.append({
        'shape': ['Round'],
        'cert':  ['IGI'],
        'craft':{'C01':'EX','C02':'VG','C03':'VG','EX':None,'VG':None},
        'condition':'FIXED',
        'data': 'block_df3.pk3'
    })

    #05.第五区域AH Round IGI 3VG+
    blocks.append({
        'shape': ['Round'],
        'cert':  ['IGI'],
        'craft':{'VG':3,'EX':None},
        'condition':'3VG+',
        'data': 'block_df4.pk4'
    })

    #06.第六区域AP Pear/Oval/Heart/MQ GIA 2EX
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['GIA'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'block_df5.pk5'
    })

    #07.第七区域AX Pear/Oval/Heart/MQ GIA VG+ 至少一个VG
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['GIA'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'block_df6.pk6'
    })
    #08.第八区域BF Pear/Oval/Heart/MQ IGI 2EX
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['IGI'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'block_df7.pk7'
    })

    #09.第九区域BN Pear/Oval/Heart/MQ IGI VG+ 至少一个VG
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['IGI'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'block_df8.pk8'
    })

    #10.第十区域BV Cushion...  GIA 2EX
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['GIA'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'block_df9.pk9'
    })
    #11.第十一区域CD Cushion...  GIA VG+
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['GIA'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'block_df10.pk10'
    })
    #12.第十二区域CL Cushion...  IGI 2EX
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['IGI'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'block_df11.pk11'
    })
    #13.第十三区域CT Cushion...  IGI VG+
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['IGI'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'block_df12.pk12'
    })
    #14.来自于第三个的分拆
    blocks.append({
        'shape': ['Round'],
        'cert':  ['IGI'],
        'craft': {'EX':3,'VG':None},
        'condition':'3EX',
        'data': 'block_df2.pk2'
    })
#####################################################################################
    #黄钻部分报价EXCEL黄色背景部分
    #15. 第14区域DB Pear/Oval/Heart/MQ GIA 2EX
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['GIA'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'yblock_df13.pk13'
    })

    #16.  第15区域DJ Pear/Oval/Heart/MQ GIA VG+ 至少一个VG
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['GIA'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'yblock_df14.pk14'
    })
    #17.  第16区域DR Pear/Oval/Heart/MQ IGI 2EX
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['IGI'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'yblock_df15.pk15'
    })
    #18. 第17区域DZ Pear/Oval/Heart/MQ IGI VG+ 至少一个VG
    blocks.append({
        'shape': ['Pear','Oval','Heart','MQ'],
        'cert':  ['IGI'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'yblock_df16.pk16'
    })
    #19. 第18区域EH Cushion...  GIA 2EX
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['GIA'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'yblock_df17.pk17'
    })
    #20. 第19区域EP Cushion...  GIA VG+
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['GIA'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'yblock_df18.pk18'
    })
    #21. 第20区域EX Cushion...  IGI 2EX
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['IGI'],
        'craft':{'EX':2,'VG':None},
        'condition':'2EX',
        'data': 'yblock_df19.pk19'
    })
    #22. 第21区域FF Cushion...  IGI VG+
    blocks.append({
        'shape': ['Cushion','Radiant','Emerald','Assher','Princess'],
        'cert':  ['IGI'],
        'craft':{'VG':1,'EX':None},
        'condition':'1VG+',
        'data': 'yblock_df20.pk20'
    })
    return blocks 