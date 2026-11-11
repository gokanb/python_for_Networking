#!/usr/bin/env python3

# Author:Gokan Bektas
# Description:

import os
import argparse
import ftplib
import getpass

LOCAL_FTP_SERVER ='localhost'
LOCAL_FILE = 'readme.text'

def ftp_upload(ftp_server, username, password, file_name):
    print(f'Connecting to FTP server: {ftp_server}')
    ftp = ftplib.FTP(ftp_server)
    print(f'Login to FTP server: user = {username}')
    ftp.login(username, password)
    ext = os.path.splitext(file_name)[1]
    if ext in ('.txt', '.htm', '.html'):
        ftp.storlines("STOR " + file_name, open(file_name))
        
    else:
        ftp.storbinary('STOR '+ file_name, open(file_name, 'rb'), 1024)
    print (f'Uploaded file: {file_name}')
    
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='FTP Server Upload Example')
        parser.add_argument('--ftp-server', action='store', dest='ftp_server', default = LOCAL_FTP_SERVER)
        parser.add_argument('--ftp-name', action='store', dest='ftp_name', default = LOCAL_FILE)
        parser.add_argument('--username', action='store', dest='username', default =getpass.getuser())
        given_args = parser.parse_args()
        ftp_server, file_name, username, = given_args.ftp_server, given_args.file_name, given_args.username
        password = getpass.getpass(prompt= 'Enter your FTP password: ')
        ftp_upload(ftp_server, username,password, file_name)
        