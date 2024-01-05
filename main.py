import json
import random

ALBUMS_JSON_FILE = "albums.json"

with open(ALBUMS_JSON_FILE) as f:
	albums = json.load(f)
	beg = 0
	end = len(albums) - 1
	rand_idx = random.randint(beg, end)
	selected_album = albums[rand_idx]

	title = selected_album['title']
	album = selected_album['album']
	artist = selected_album['artist']
	year = selected_album['year']

	if album and artist:
		print("Album: ", album)
		print("Artist: ", artist)
	else:
		print("Title: ", title)
	if year:
		print("Year: ", year)
