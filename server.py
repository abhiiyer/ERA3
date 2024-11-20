from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import os

def run_server():
    os.chdir('static')
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server at http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=run_server).start() 