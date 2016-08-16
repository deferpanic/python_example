import http.server
import socketserver

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        prefix = "/python/lib/python3.5/site-packages/"
        if self.path == '/':
            self.path = prefix + 'index.html'
        else:
            self.path = prefix + self.path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def http_server():
    Handler = MyRequestHandler
    server = socketserver.TCPServer(('0.0.0.0', 3000), Handler)
    server.serve_forever()

if __name__ == '__main__':
    http_server()
