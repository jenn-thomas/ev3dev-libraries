ledpath = '/sys/class/leds/ev3-{}:{}:ev3dev/'
ledbright = ledpath +'brightness'

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_get(self):
		LED = open(ledbright.format('right0','red'),"w",0)
		LED.write(str(0 + '\n'))
		LED.close
		LED = open(ledbright.format('left0','red'),"w",0)
		LED.write(str(i) + '\n')
		LED.close
		for i in range(0,256):
			LED = open(ledbright.format('right0','red'),"w",0)
			LED.write(str(i) + '\n')
			LED.close
			LED = open(ledbright.format('left0','red'),"w",0)
			LED.write(str(i) + '\n')
			LED.close

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