# Author: illyum

# Instructions:
#	Create 2 text file in the same folder as this script:
# 		key.txt
#		uuid.txt
#	Enter YOUR uuid and YOUR api key in their respective text files
# 	Run the script using `python typer.py`

import os
import time
import json
import pandas
import sqlite3
import requests

# # # Enter YOUR uuid and YOUR api key in their respective text files
with open('key.txt', r) as key_file:
	key = key_file.readlines().strip()
with open('uuid.txt', 'r') as uuid_file:
	uuid = uuid_file.readlines().strip().replace('-', '')
url = "https://api.hypixel.net/player?key={}&uuid=".format(key)


# # # Get local friends file
local_friends_list = []
with open('shadows.json', 'r') as friends_file:
	local_friends_list = json.load(friends_file).get('friends', [])

# # # Get hypixel friends list
hypixel_friends_request = requests.get("https://api.hypixel.net/friends?key={}&uuid={}".format(key, uuid)).json()
hypixel_friends = {uuid,}
for record in hypixel_friends_request.get('records', {}):
	hypixel_friends.add(record['uuidSender'])
	hypixel_friends.add(record['uuidReceiver'])

# # # Update local shadows file
shadows = set.union(set(local_friends_list), hypixel_friends)
with open('shadows.json', 'w') as friends_file:
	json.dump({"shadows": [val for val in shadows]}, friends_file, indent=2)

# # # Get local database
con = sqlite3.connect('players.db')
cur = con.cursor()

# # # Get stats for all players
all_players = list(set(hypixel_friends))
all_players.insert(0, uuid)
for player in all_players:
	data = requests.get(url + player).json()
	player_uuid = data['player']['uuid']
	player_name = data['player']['displayname']
	bedwars_stars = data['player']['achievements']['bedwars_level']
	timestamp = time.time()
	bedwars_data = {'timestamp': timestamp, 'stars': bedwars_stars}
	for k, v in data['player']['stats']['Bedwars'].items():
			if type(v) == int:
				bedwars_data[k] = v

# # # Log stats for all players
	bedwars_df = pandas.DataFrame([bedwars_data])
	bedwars_df.to_sql(f'{player_uuid}_bedwars', con, if_exists='append' )

# # # Show finished
print('Done!')
