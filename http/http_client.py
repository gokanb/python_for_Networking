#!/usr/bin/env python3

import urllib.request

class HTTPClient:
    
    def __init__(self, host):
        self.host = host
        
    def fetch(self):
        response = urllib.request.urlopen(self.host)
        data = response.read()
        text = data.decode('utf-8')
        return text