import http.client
import json
from Seq import Seq

# Every web page listens at the port 80
PORT = 80
SERVER = "rest.ensembl.org"

conn = http.client.HTTPConnection(SERVER, PORT)
conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))
data1 = r1.read().decode("utf-8")
answer = json.loads(data1)
id = answer["data"][0]["id"]
print(id)

conn.request("GET", "/sequence/id/"+id+"?content-type=application/json")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
answer = json.loads(data1)
print(answer)
chain = answer["seq"]
print(chain)

my_sequence = Seq(chain)
total = len(chain)
print("Total length: ", total)

print("Number of T bases: ", my_sequence.count("T"))

print("Percentage of A's: ", my_sequence.perc("A"))
print("Percentage of C's: ", my_sequence.perc("C"))
print("Percentage of G's: ", my_sequence.perc("G"))
print("Percentage of T's: ", my_sequence.perc("T"))
