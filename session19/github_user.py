import http.client
import json

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("User to obtain information from: ")
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)


text_json = r1.read().decode("utf-8")
conn.close()


user = json.loads(text_json)

login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: \n{}".format(bio))


# Obtain the name of the repositories

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID + "/repos", None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

repos = json.loads(text_json)

print("Names of the repositories: ")
for i in repos:
    print(repos[0]["name"])


# Obtain the number of commits

HOSTNAME = "api.github.com"
ENDPOINT = "/repos/"+ GITHUB_ID + "/2018-2019-practices/commits"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

commits = json.loads(text_json)

print("Total commits: ", len(commits))