import http.client
import json
import sys

city = input("City to obtain weather information from: ")

HOSTNAME = "www.metaweather.com"
ENDPOINT = " /api/location/search/?query="+city
METHOD = "GET"
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

r1 = conn.getresponse()

raw_response = r1.read().decode("utf-8")
conn.close()

metainfo = json.loads(raw_response)

if len(metainfo) == 0:
    print("- ERROR - Sorry, the requested city does not exist.")
    sys.exit()

# We obtain the id for the city
woeid = metainfo[0]["woeid"]

woeid = str(woeid)

HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"

METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + woeid + '/', None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)

time = weather['time']

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']
sun_set = weather["sun_set"]


print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
print("Sun set time: {}".format(sun_set))
