import http.server
import socketserver

PORT = 8000
class TestMe():
	def take_five(self):
		returm 4
	def port(self):
		return PORT

if __name__== '__main__' :
	Handler = http.server.SimpleHTTPRequestHandler

	with socketserver.TCPServer(("",Port), Handler) as http:
		print("serving at port", PORT)
		http.serve_forever()
