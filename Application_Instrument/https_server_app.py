import http.server
from prometheus_client import start_http_server

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(
            "<html><head><title>First Application</title></head>"
            "<body style='color: #333; margin-top: 30px;'>"
            "<center><h2>Welcome to our first Python App.</h2></center>"
            "</body></html>", 
            "utf-8"
        ))

if __name__ == "__main__":
    start_http_server(5001)
    server_address = ('localhost', 5000)
    httpd = http.server.HTTPServer(server_address, HandleRequests)
    print("Serving on http://localhost:5000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        httpd.server_close()
        print("Server stopped.")
