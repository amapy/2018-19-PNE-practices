from Seq import Seq
import socket

PORT = 8089

IP = "127.0.0.1"

while True:
    message = str(input("Write a sequence: "))

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.connect((IP, PORT))

    # The reverse of the sequence given by the user
    reverse_mssg = Seq(message).reverse()

    # The complement of the reverse
    complement_mssg = Seq(reverse_mssg).complement()

    # Instead of returning the initial message, we send to the server the reverse-complement sequence.
    final = str.encode(complement_mssg)
    soc.send(final)

    msg = soc.recv(2048).decode("utf-8")

    print("Message from server: ")

    print(msg)

    soc.close()
