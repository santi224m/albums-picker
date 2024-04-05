import json
import random

from album import Album

ALBUMS_JSON_FILE = "albums.json"

def get_rand_album(albums):
	"""
	Return a random album
	"""
	beg = 0
	end = len(albums) - 1
	rand_idx = random.randint(beg, end)
	selected_album = albums[rand_idx]
	title = selected_album['Album']
	artist = selected_album['Artist']
	year = selected_album['Date']
	album = Album(title, artist, year)
	return album

def print_album(album):
	"""Print the choosen album"""	
	print("Album: ", album.title)
	print("Artist: ", album.artist)
	print("Year: ", album.year)

if __name__ == "__main__":
	with open(ALBUMS_JSON_FILE) as f:
		albums = json.load(f)
	
	rand_album = get_rand_album(albums)
	print_album(rand_album)