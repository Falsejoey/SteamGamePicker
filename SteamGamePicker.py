import json
import random
import urllib2
import sys

# enter valid api key
API_KEY = raw_input("Enter Steam Web API key: ")
API_CALL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&include_appinfo=1&format=json"

# enter valid steamid
steamid = raw_input("Enter steamid (http://steamcommunity.com/profiles/<steamid>): ")
url = API_CALL % (API_KEY, steamid)

try:
	games = []

	# api call returns data in json
	steamjson = json.loads(urllib2.urlopen(url).read())
	for game in steamjson["response"]["games"]:
		games.append(game["name"].encode("ascii", "ignore"))

	gameindex = random.randint(0, len(games) - 1)
	print games[gameindex]

# if key/steamid invalid
except ValueError:
	print "Error: invalid steamid and/or API key."
