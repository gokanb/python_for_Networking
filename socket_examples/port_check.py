import socket
#from termcolor import colored
'''
This script will create list of ports and tests if the ports are open or closed. 

'''

ip = '127.0.0.1' 
ports = [20, 21, 22, 23, 24, 80, 81, 82, 83, 84]

for port in ports:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # This tests if the ports are either open or closed to be unsed in certain network protocols
    # such as ssh, ftp, telnet and http.s
    results = sock.connect_ex((ip, port))
    print(f'The host with address {ip} has {port} open for business : {results}')
    sock.close()
    
               





