#!/usr/bin/env python3
from http.server import HTTPServer,SimpleHTTPRequestHandler
import ssl
from datetime import datetime
import pytz

PORT = 1443

class MyHandler(SimpleHTTPRequestHandler):
	def do_GET(s):
		s.send_response(200)
		s.end_headers()
		s.wfile.write (b'Hello, world! Time is ')
		s.wfile.write (bytes(TIME,'ascii'))

tz_MSK = pytz.timezone('Europe/Moscow')
time_MSK = datetime.now(tz_MSK)
TIME=time_MSK.strftime("%H:%M:%S")

httpd = HTTPServer(('', PORT), MyHandler)
sslctx = ssl.SSLContext()
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='cert.pem', keyfile="key.pem", password="QWE123asd")
httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)


httpd.serve_forever()#
