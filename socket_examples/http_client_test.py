import socket

'''
This script will be testing the given local host and given port. 

'''

web_host = '127.0.0.1'
web_port = 8008


print(f'Connecting to {web_host} on port {web_port}')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((web_host, web_port))
sock.send(bytes('GET / HTTP/1.1\r\n\nHost: localhost\r\n\r\n'.encode('utf-8')))
reply = sock.recv(4096)
print(f'Response from {web_host}: ')
print(reply.decode())
