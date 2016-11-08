import threading
import thread
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import time
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep,listdir
import os,sys
import json
import ev3

FILE = 'webpage.html'
PORT = 8000

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        otype = self.headers.getheader('content-type')
        data_string = self.rfile.read(length)
        data = json.load(data_string)
        
        self.send_response(200)
        self.end_headers()
        data['success']='Operation Successful'
        data = json.dumps(data)
        print data
        self.wfile.write(data)

def WebServerThread():                  
    try:
    #Create a web server and define the handler to manage the
    #incoming request
        server_address = ("", PORT)
        server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
        print 'Started httpserver on port ' , PORT
    #Wait forever for incoming htto requests
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
            
if __name__ == "__main__":
    WebServerThread()