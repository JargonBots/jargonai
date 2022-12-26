from http.server import BaseHTTPRequestHandler, HTTPServer

from conversation import conversation


class MyHandler(BaseHTTPRequestHandler):
    Name = "James Bond"
    cv = conversation("The following is a conversation with {}.\n", "{}: ".format(Name))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Chat Bot</title></head>")
        self.wfile.write(b"<body><p>You: </p>")
        self.wfile.write(b"<form action='/' method='POST'>")
        self.wfile.write(b"<input type='text' name='string'>")
        self.wfile.write(b"<input type='submit' value='Submit'>")
        self.wfile.write(b"</form></body></html>")
        return

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        string = post_data.split("=")[1]
        self.cv.add_to_environment("\nMe: " + str(string))
        self.cv.bot_append()

        out_line_readable = self.cv.toks
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<body><p>Bot: </p>")
        self.wfile.write(out_line_readable.encode("utf-8"))
        self.wfile.write(b"</body></html>")
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Chat Bot</title></head>")
        self.wfile.write(b"<body><p>You: </p>")
        self.wfile.write(b"<form action='/' method='POST'>")
        self.wfile.write(b"<input type='text' name='string'>")
        self.wfile.write(b"<input type='submit' value='Submit'>")
        self.wfile.write(b"</form></body></html>")
        return


httpd = HTTPServer(("localhost", 8080), MyHandler)
httpd.serve_forever()
