#coding: utf-8
import http.server
import socketserver

#port et address
port = 90
address = ("",port)

#server
server= http.server.HTTPServer

#manager
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address,handler)

print(f"Server run succcefuly {port}")

httpd.serve_forever()