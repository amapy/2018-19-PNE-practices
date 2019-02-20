import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8089



while True:

    # Before connecting to the server, ask the user for the string
    send = ""
    msg = input("> ")
    while len(msg) > 0:
        send = send + msg + "\n"
        msg = str(input(""))

    # If the mesage is empty, the server is going to ask anyways
    if len(send) == 0:
        send = "\n"

    # Now we can create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(send))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()
