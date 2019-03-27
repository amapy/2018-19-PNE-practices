import http.client
import json



# RANDOM JOKE

HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

chucknorris = json.loads(text_json)

print("Chuk Norris' joke: ", chucknorris["value"]["joke"])



# NUMBER OF JOKES

HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/count"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

chucknorris = json.loads(text_json)

print("Total number of jokes", chucknorris["value"])



# CATEGORIES OF JOKES

ENDPOINT = "/categories"

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

chucknorris = json.loads(text_json)

categories = chucknorris["value"]

print("Number of categories: ", len(categories))

print("Category or categories of the joke: ", categories)
