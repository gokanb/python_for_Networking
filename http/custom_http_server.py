#!/usr/bin/env python3

from request_handler import RequestHandler #importing reqest handler lib 
from http.server import HTTPServer         #importing http server

class CustomHTTPServer(HTTPServer):        # creating class that creates custo http server given host - port 
    "A custom HTTP server"
    def __init__(self, host, port):
        server_address = (host, port)
        HTTPServer.__init__(self, server_address, RequestHandler)
