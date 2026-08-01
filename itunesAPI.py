## This is a programme that calls the iTunes API. 
import json
import requests
import sys

if len(sys.argv) > 3:
    sys.exit("Usage: python itunes.py <artist name>>")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
print(response.json())
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o['results']:
    print(result['trackName'] + " by " + result['artistName'])