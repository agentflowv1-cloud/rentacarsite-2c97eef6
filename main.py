import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<!DOCTYPE html><html><head><title>Simple Navbar</title><link rel="stylesheet" href="https://cdn.tailwindcss.com"></head><body><nav class="flex justify-between bg-blue-500 text-white py-4"><div class="ml-10"><img src="logo.png" alt="Logo" class="h-10"></div><ul class="flex items-center mr-10 space-x-10"><li><a href="" class="hover:text-gray-200">Home</a></li><li><a href="" class="hover:text-gray-200">About</a></li><li><a href="" class="hover:text-gray-200">Contact</a></li></ul></nav></body></html>')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not found')

    def log_message(self, format, *args):
        return

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run_server(port)
