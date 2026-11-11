#!/usr/bin/env python3

# Author:Gokan Bektas
# Description:

import poplib
import argparse
import getpass

GOOGLE_POP3_SERVER = 'pop.googlemail.com'

def email_download(username):
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, '995')
    mailbox.user(username)
    password = getpass.getpass(prompt="Enter your Google password: ")
    mailbox.pass_(password)
    num_messages = len(mailbox.list()[1])
    print(f'Total emails: {num_messages}')
    print (f'Getting last message')
    for msg in mailbox.retr(num_messages)[1]:
        print(msg)
    mailbox.quit()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Download Example')
    parser.add_argument('--username', action="store", dest="username", default=getpass.getuser())
    given_args = parser.parse_args()
    username = given_args.username
    email_download(username)