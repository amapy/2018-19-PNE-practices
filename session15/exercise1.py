import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8012


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open different options depending on request message
        if self.path == "/" or "":
            sending = open("form1.html", "r")
            contents = sending.read()
        elif "/echo" in self.path:
            sending = self.path.split("=")[1]
            contents = """<hmtl>
            <body style="background-color: turquoise;">
            <title>Message sent</title>         
            <h1>Received message:</h1>
            <br>"""+ sending +"""<br><br>
            <a href = "/">Click here to return to the main page :)</a>
            </body>
            </html>"""
        else:
            sending = open("error.html", "r")
            contents = sending.read()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
