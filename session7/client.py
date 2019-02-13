"""Programming our first client"""

# Create a socket for communicating with the server
import socket

s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)

print("Socket created.")

port = 8080

IP = "212.128.253.64"

# Connect to the server
s.connect((IP, port))

s.send(str.encode("Hello from the other side"))

msg = s.recv(2048).decode("utf-8")

print("Message from the server: ")

print(msg)

s.close()

print("The end.")

