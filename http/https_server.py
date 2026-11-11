#!/usr/bin/env python3

# Author:Gokan Bektas
# Description: we created secure server. 

import socket
from OpenSSL import SSL
from socketserver import BaseServer
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

class SecureHTTPServer(HTTPServer):
    def __init__(self, server_address, HandlerClass):
        BaseServer.__init__(self, server_address, HandlerClass)
        ctx = SSL.Context(SSL.SSLv23_METHOD)
        fpem = 'server.pem' #location of the server private key and the server cerificate
        ctx.use_privatekey_file (fpem)
        ctx.use_certificate_file(fpem)
        self.socket = SSL.Connection(ctx, socket.socket(self.address_family,self.socket_type))
        self.server_bind()
        self.server_activate()
        

class SecureHTTPrequestHandler(SimpleHTTPRequestHandler):
    def setup(self):
        self.connection = self.request
        self.rfile = socket._fileobject(self.request, 'rb', self.rbufsize)
        self.wfile = socket._fileobject(self.request, 'wb', self.wbufsize)
        

def run_server(HandlerClass = SecureHTTPrequestHandler, ServerClass = SecureHTTPServer):
    server_address = ('', 4443) #port needs to be accessible by user
    server = ServerClass(server_address, HandlerClass)
    running_address = server.socket.getsockname()
    print (f'Serving HTTPS Server On {running_address[0]} : {running_address[1]}')
    server.serve_forever()
    

if __name__ == '__main__':
    run_server()
    

# generate pem key
# openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
# redirecting > 
# add >>