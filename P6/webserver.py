import http.server
import socketserver
import termcolor
from Seq import Seq

# Define the Server's port
PORT = 8020


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def validSequence(self, s):
        valid = 'ACTG'
        for letter in s:
            if letter not in valid:
                return False
        return True

    def tratar(self, s1, comand):
        print("Haciendo comando", comand)
        if (comand == "len"):
            return s1.len()
        elif (comand == "complement"):
            return s1.complement().get_strbase()
        elif (comand == "reverse"):
            return s1.reverse().get_strbase()
        elif (comand == "countA"):
            return s1.count('A')
        elif (comand == "countT"):
            return s1.count('T')
        elif (comand == "countG"):
            return s1.count("G")
        elif (comand == "countC"):
            return s1.count("C")
        elif (comand == "percA"):
            return s1.perc("A")
        elif (comand == "percT"):
            return s1.perc("T")
        elif (comand == "percG"):
            return s1.perc("G")
        elif (comand == "percC"):
            return s1.perc("C")
        else:
            return "ERROR"

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open different options depending on request message
        if self.path == "/":
            sending = open("form.html", "r")
            contents = sending.read()
        elif "/seq" in self.path:
            contents = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>ServerResponse</title>
            </head>
            <body style="background-color: green">"""

            petition = self.path.split("=")[1]
            divide = petition.split("&")
            dna_seq = divide[0]

            contents = contents + "<p><h3>Cadena: </h3>" + dna_seq + "</p>"

            if self.validSequence(dna_seq):
                print ("Cadena: "+dna_seq)
                s1 = Seq(dna_seq)
                if 'len=on' in self.path:
                    length = s1.len()
                    contents = contents + "<p><h3>Length: </h3>" + str(length) + "</p>"
                operation = self.path.split('operation=')[1].split("&")[0]
                contents = contents + "<p><h3>Operation: </h3>" + operation + "</p>"
                base = self.path.split('base=')[1].split("&")[0]
                contents = contents + "<p><h3>Base: </h3>" + base + "</p>"
                comand = operation + base
                answer = self.tratar(s1, comand)
                contents = contents + "<p><h3>Answer: </h3>" + str(answer) + "</p>"
            else:
                contents = contents + "<p>No Valida</p>"

            contents = contents + """<br> <a href="/"> Click here to go to the main page </a></body></html>"""


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
