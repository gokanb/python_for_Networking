#!/usr/bin/env python3


#importing libraries
import argparse
import sys
from customHTTP_server import CustomHTTPServer 
from request_handler import RequestHandler

DEFAULT_HOST = '127.0.0.1'          
DEFAULT_PORT = 8000

def run_server(port):      #creating function that run the server.
    try:
        server = CustomHTTPServer(DEFAULT_HOST, port)   #creating var 
        print(f'Custom HTTP server started on port: {port}')
        server.serve_forever() #serves forever until user keyboard interup 

    except Exception as err:
        print (f'Error: {err}')

    except KeyboardInterrupt: #interupting with keyboard cntl + c 
        print("Server interrupted and is shutting down...")
        server.socket.close() #close connection

if __name__ == "__main__": #calling the method we created.
    parser = argparse.ArgumentParser(description="Simple HTTP server")
    parser.add_argument('--port', action="store", dest="port", type=int, default=DEFAULT_PORT)
    given_args = parser.parse_args()
    port = given_args.port
    run_server(port)