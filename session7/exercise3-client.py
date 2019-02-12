"""Client for communicatioing with Dafne's computer"""

import socket

soc = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

PORT = 8081

IP = "212.128.253.78"

soc.connect((IP, PORT))

message = str(input("Write a message you want to send: "))

soc.send(str.encode(message))

msg = soc.recv(2048).decode("utf-8")

print("Message from server: ")

print(msg)

soc.close()