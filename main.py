import json
import random

ALBUMS_JSON_FILE = "albums.json"

with open(ALBUMS_JSON_FILE) as f:
	albums = json.load(f)
	beg = 0
	end = len(albums) - 1
	rand_idx = random.randint(beg, end)
	selected_album = albums[rand_idx]

	album = selected_album['Album']
	artist = selected_album['Artist']
	year = selected_album['Date']

	print("Album: ", album)
	print("Artist: ", artist)
	print("Year: ", year)
