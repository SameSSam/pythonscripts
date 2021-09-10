import time
import os
from ftplib import FTP


class FtpDownload(object):
    def __init__(self,ftp_server,ftp_username,ftp_password):
        #初始化ftpconnect
        self.ftp_server = ftp_server
        self.username = ftp_username
        self.password = ftp_password
        self.bufsize = 1024
        self.local_path = 'E:\\database_jdzb_bck\\'
        self.remote_path = "/172_16_0_15/dsd_jdzb/"  # 远端目录
        self.logfile = 'E:\\Shares\\Public\\IT_TOols\\DSD_ERP\\ftpdownload.log' 
        self.ftp = FTP()
        self.ftp.set_debuglevel(0) # 较高的级别方便排查问题
        self.ftp.connect(self.ftp_server, 21)
        self.ftp.login(self.username, self.password)   

    def remote_filename(self):
        self.ftp.cwd(self.remote_path)   #进入ftp目录
        remote_file_names = self.ftp.nlst() # 获取指定目录下文件列表
        # self.ftp.quit()  #ftp会在下载完成后退出
        result = [today_file for today_file in remote_file_names if today_file[9:17] == str(int(today) - 1)] #获取到数组，取第一个值
        return result

    def ftp_download_file(self):
        """用于目标文件下载"""
        if self.remote_filename():
            local_filename = self.local_path + self.remote_filename()[0]
            remote_filename = self.remote_path + self.remote_filename()[0]
            if not os.path.exists(local_filename):
                start_time = time.time()
                fp = open(local_filename, 'wb')
                self.ftp.set_debuglevel(0) # 较高的级别方便排查问题
                self.ftp.retrbinary('RETR ' + remote_filename, fp.write, self.bufsize)
                fp.close()
                self.ftp.quit()
                cost_time = time.time() - start_time
                mesg = " 昨日备份数据库文件已下载！共计下载时间%.2f秒" %cost_time
                self.file_logger(mesg)
            else:
                error = " 备份文件已存在！"
                self.file_logger(error)
        else:
            error = "今日没有需要备份的数据库文件！"
            self.file_logger(error)

    def file_logger(self, mesg):
        with open(self.logfile, 'a') as f:
            f.write('\n' + time.strftime("%Y/%m/%d %H:%M:%S") + mesg)


ftp_server = '106.55.152.6'
ftp_user = 'jdzb'
ftp_password = 'dsd_jdzb'

today = time.strftime("%Y%m%d")

if __name__ == "__main__":
    ftpdownload = FtpDownload(ftp_server, ftp_user, ftp_password)
    ftpdownload.ftp_download_file()
    time.sleep(30)
