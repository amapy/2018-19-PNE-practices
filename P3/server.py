import socket
import termcolor
import sys
from Seq import Seq


# Configure the Server's IP and PORT
PORT = 8089
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


# This function is for finding mistaken bases in the DNA sequence given
def validbases(s):
    valid = "ACGT"
    for base in s:
        if base not in valid:
            return False
    return True


def treat(my_sequence, command):
    print("Command", command)
    if command == "len":
        return my_sequence.len()
    elif command == "complement":
        return my_sequence.complement()
    elif command == "reverse":
        return my_sequence.reverse()
    elif command == "countA":
        return my_sequence.count_base("A")
    elif command == "countC":
        return my_sequence.count_base("C")
    elif command == "countG":
        return my_sequence.count_base("G")
    elif command == "countT":
        return my_sequence.count_base("T")
    elif command == "percA":
        return my_sequence.perc("A")
    elif command == "percC":
        return my_sequence.perc("C")
    elif command == "percG":
        return my_sequence.perc("C")
    elif command == "percT":
        return my_sequence.perc("T")


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the message in red color in the server
    termcolor.cprint(msg, "red")
    answer = ""
    if msg == "\n":
        answer = "Alive"
    else:
        # Here we split the message so it is divided
        # Now we can differentiate the DNA sequence from the commands requested
        divide = msg.split("\n")
        print("Checking...", divide[0])
        if validbases(divide[0]):
            answer = "Ok\n"
            my_sequence = Seq(divide[0])

            for i in range(1, len(divide) - 1):
                print("Command requested", i, ":", divide[i])
                r = treat(my_sequence, divide[i]) # Be careful!!
                answer = answer + str(r) + "\n"

        else:
            answer = "Error"


    # If the message is "EXIT", the server stops the connection with the client
    if msg == "EXIT":
        sys.exit(0)

    # Send the msg back to the client (echo)
    cs.send(str.encode(answer))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)