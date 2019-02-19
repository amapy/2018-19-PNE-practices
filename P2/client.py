from Seq import Seq

import socket

PORT = 8088

IP = "212.128.253.118"

while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.connect((IP, PORT))

    message = str(input("Write a sequence: "))

    # The reverse of the sequence given by the user
    reverse_mssg = message.reverse()

    # The complement of the reverse
    complement_mssg = reverse_mssg.complement()

    # Instead of returning the initial message, we send to the server the reverse-complement sequence.
    soc.send(str.encode(complement_mssg))

    msg = soc.recv(2048).decode("utf-8")

    print("Message from server: ")

    print(msg)

    soc.close()
