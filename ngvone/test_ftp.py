import sys
from ftplib import FTP
import os
import struct
import time

# 当前路径
current_path = os.path.dirname(os.path.realpath(__file__))

download_file_pth = os.path.join(current_path, "download")


def ftp_download_file(self, remote_file_name, address, user_name="anonymous", password=""):
    '''
    ftp下载文件
    :param remote_file_name:
    :param address:
    :param user_name:
    :param password:
    :return:True，下载成功，False,下载失败
    '''
    # 创建ftp对象实例
    ftp = FTP()
    local_path = download_file_pth
    if not os.path.exists(download_file_pth):
        os.mkdir(download_file_pth)
    # 为准备下载到本地的文件，创建文件对象（默认为远程下载的文件名，也可自定义）
    local_file_name = os.path.join(local_path, os.path.basename(remote_file_name))
    file = open(local_file_name, 'wb')
    try:
        # 连接接FTP
        ftp.connect(address, '21')
        # 通过账号和密码登录FTP服务器
        ftp.login(user_name, password)
        # 如果参数 pasv 为真，打开被动模式传输 (PASV MODE) ，否则，如果参数 pasv 为假则关闭被动传输模式。
        ftp.set_pasv(1)
        # 从FTP服务器下载文件到前一步创建的文件对象，其中写对象为file.write，1024是缓冲区大小
        ftp.retrbinary('RETR ' + remote_file_name, file.write, 1024)
        # 关闭下载到本地的文件
        # 提醒：虽然Python可以自动关闭文件，但实践证明，如果想下载完后立即读该文件，最好关闭后重新打开一次
        # log.info("文件下载完成")
        return True
    except Exception as e:
        # log.error("文件下载失败...")
        # log.error(e.message)
        return False
    finally:
        file.close()
        ftp.close()


ftp_download_file('ttt', '192.168.71.76', 'root', '111111')
