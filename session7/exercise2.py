import socket

# Port of the server
port = 8088

# IP of the teacher computer
IP = "212.128.253.64"

# Loop for constantly ask for a message
while True:
    # Creation of the socket
    s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

    # Creation of the input for the user
    my_message = input("Send... : ")

    # Connect to the server
    s.connect((IP, port))

    # Send the message the user wrote
    s.send(str.encode(my_message))

    msg = s.recv(2048).decode("utf-8")

    print("Message from the server: ")

    print(msg)

    s.close()

# I should close the client everytime I send a  new message

# If we put the input of the message before connecting to the server, we make this connection quicker because we write the message first and, when it is ready, we are able to send it in the moment of the connection