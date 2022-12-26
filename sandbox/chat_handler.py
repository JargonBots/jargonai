# Property of JargonBots.
# Written by Armaan Kapoor on 12-22-2022.

from http.server import HTTPServer, BaseHTTPRequestHandler

class ChatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><head><title>Chat Server</title></head>')
        self.wfile.write(b'<body><form action="/" method="POST">')
        self.wfile.write(b'<input type="text" name="message">')
        self.wfile.write(b'<input type="submit" value="Send">')
        self.wfile.write(b'</form></body></html>')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = self.handle_message(body.decode('utf-8'))
        self.wfile.write(response.encode('utf-8'))

    def handle_message(self, message):
        # Your code here
        return 'You said: ' + message

httpd = HTTPServer(('localhost', 8080), ChatHandler)
httpd.serve_forever()
