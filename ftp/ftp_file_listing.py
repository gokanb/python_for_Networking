#!/usr/bin/env python3

# Author:Gokan Bektas
# Description:


import ftplib
from ftplib import FTP

FTP_SERVER_URL = 'ftp.ed.ac.uk' #


def ftp_connection(path, username, email):
    ftp = ftplib.FTP(path, username, email)
    ftp.cwd("/pub")
    print(f'File list at {path}: ')
    files = ftp.dir()
    print(files)
    
    ftp.quit()
    
if __name__ == '__main__':
    ftp_connection(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com',) 