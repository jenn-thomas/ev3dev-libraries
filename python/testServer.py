#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir,sep,listdir
import os,sys
import cgi
import thread
import threading
import time
from threading import Timer

#This class will handles any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):
        
        #Handler for the GET requests
        def do_GET(self):
			print self.path

        #Handler for the POST requests
        def do_POST(self):
        	print self.info

                        
                                      
# This is a thread that runs the web server 
def WebServerThread():     
        try:
                #Create a web server and define the handler to manage the
                #incoming request
                server = HTTPServer(('', PORT_NUMBER), myHandler)
                print 'Started httpserver on port ' , PORT_NUMBER
                
                #Wait forever for incoming htto requests
                server.serve_forever()

        except KeyboardInterrupt:
                print '^C received, shutting down the web server'
                server.socket.close()


# Runs the web server thread
thread.start_new_thread(WebServerThread,())             
