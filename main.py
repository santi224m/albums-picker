import  argparse
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
  # Setup argument parser
	parser = argparse.ArgumentParser(
		prog='1001-albums-picker',
		description='Choose a random album from "1001 Albums You Must Hear Before You Die"',
  )
	parser.add_argument('-j', '--json', action='store_true')
	args = parser.parse_args()
  
  # Open albums list
	with open(ALBUMS_JSON_FILE) as f:
		albums = json.load(f)
	
	# Choose random album
	rand_album = get_rand_album(albums)

	# Return in json format if '-j' or '--json' flag is set
	if args.json:
		print(rand_album.to_json())
	else:
		print_album(rand_album)