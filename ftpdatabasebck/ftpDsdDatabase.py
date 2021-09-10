#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
@Time  : 2021-01-12 16:30
@Author : SamShan
@FileName: ftpDsdDatabase.py
@Description: 在Windows Server部署计划任务，在每天某个时刻定时运行此脚本
'''

import time
from ftplib import FTP
import os

local_path = 'E:\\database_jdzb_bck\\'
remote_path = "/172_16_0_15/dsd_jdzb/" # 远端目录
log_file = 'E:\\Shares\\Public\\IT_TOols\\DSD_ERP\\ftpdownload.log'

today = time.strftime("%Y%m%d") # 当天日期

ftp_server = '106.55.152.6'
ftp_user = 'jdzb'
ftp_password = 'dsd_jdzb'

def ftp_connect(ftp_server,username,password):
    """用于FTP连接"""
    ftp = FTP()
    ftp.set_debuglevel(0) # 较高的级别方便排查问题
    ftp.connect(ftp_server, 21)
    ftp.login(username, password)    
    return ftp

def remote_filename():
    """用于FTP站点目标文件存在检测"""
    ftp = ftp_connect(ftp_server,ftp_user,ftp_password)
    ftp.cwd(remote_path) # 进入目标目录
    remote_file_names = ftp.nlst() # 获取文件列表
    ftp.quit()
    result = [today_file for today_file in remote_file_names if today_file[9:17] == str(int(today) - 1)] #获取到数组，取第一个值
    return result

def ftp_download_file(local_filename,remote_filename):
    """用于目标文件下载"""
    ftp = ftp_connect(ftp_server,ftp_user,ftp_password)
    bufsize = 1024
    fp = open(local_filename, 'wb')
    ftp.set_debuglevel(0) # 较高的级别方便排查问题
    ftp.retrbinary('RETR ' + remote_filename, fp.write, bufsize)
    fp.close()
    ftp.quit()


if __name__ == "__main__":
    if remote_filename():
        filename = remote_filename()[0]
        if not os.path.exists(local_path + filename):   #本地文件不存在，才执行下载
            # print("本地不存在最新的备份文件%s,开始从FTP服务器下载，请等待下载完成....." %(local_path + filename))
            start_time = time.time()
            ftp_download_file((local_path + filename),(remote_path + filename))
            cost_time = time.time() - start_time
            with open(log_file, 'a') as f:
                f.write('\n' + time.strftime("%Y/%m/%d %H:%M:%S") + " 昨日备份数据库文件已下载！共计下载时间%.2f秒" %cost_time)
            time.sleep(30) # 下载完毕静默
        else:
            with open(log_file, 'a') as f:
                f.write('\n' + time.strftime("%Y/%m/%d %H:%M:%S") + " 目标文件已下载！")
            time.sleep(30) # 下载完毕静默30秒
    else:
        with open(log_file, 'a') as f:
            f.write('\n' + time.strftime("%Y/%m/%d %H:%M:%S") + " 目标文件不存在！")
        time.sleep(30) # 下载完毕静默30秒        
