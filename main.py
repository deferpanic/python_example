import http.server
import socketserver

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def http_server():
    Handler = MyRequestHandler
    server = socketserver.TCPServer(('0.0.0.0', 3000), Handler)
    server.serve_forever()

if __name__ == '__main__':
    http_server()
