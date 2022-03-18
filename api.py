#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

mappings = { '/hello': {'msg': 'Hello World'}, '/health': {'msg': 'Healthy'} }

class myHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		status = 200

		service = mappings.get(self.path)
		if service is None:
			status = 404	
			service = {'msg': 'Not found'}
			

		self.send_response(status)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes(service['msg'], 'ASCII'))
		return

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print ('Started httpserver on port ' , PORT_NUMBER)
	
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()
	
