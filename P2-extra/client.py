import socket

PORT = 8081

IP = "217.0.0.1"

while True:
    message = input("Please, write a sequence: ")

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.connect((IP, PORT))

    # Instead of returning the initial message, we send to the server the reverse-complement sequence.
    soc.send(str.encode(message))

    msg = soc.recv(2048).decode("utf-8")

    print("Message from server: {}".format(msg))

    print(msg)

    soc.close()
