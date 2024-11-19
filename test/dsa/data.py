import http.server
import socketserver
import urllib.request


# Configure the server
class ReverseProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        target_url = (
            f"http://google.com{self.path}"  # Replace with the target server URL
        )

        try:
            # Forward the request to the target server
            with urllib.request.urlopen(target_url) as response:
                self.send_response(response.status)
                self.send_headers_from_response(response)
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, f"Failed to proxy request: {e}")

    def send_headers_from_response(self, response):
        # Copy headers from the response
        for header, value in response.getheaders():
            self.send_header(header, value)
        self.end_headers()


def run(
    server_class=http.server.HTTPServer, handler_class=ReverseProxyHandler, port=8080
):
    with server_class(("", port), handler_class) as httpd:
        print(f"Serving reverse proxy on port {port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run()
