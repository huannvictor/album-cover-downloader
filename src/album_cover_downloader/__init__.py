import urllib.request
import json
import os

album = input("Insira o nome do album: ")

url = f"https://itunes.apple.com/search?term={album.replace(' ', '+')}&media=music&limit=1"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

img_url = data ["results"][0]["artworkUrl100"]
img_url = img_url.replace("100x100", "1000x1000")

urllib.request.urlretrieve(img_url, "album-cover.jpg")

os.startfile("album-cover.jpg")