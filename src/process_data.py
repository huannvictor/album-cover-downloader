import os
import urllib.request
import json

from data_entry import DataEntyType
from open_img import open_img

def process_data(url: str, album_data: DataEntyType):
    img_url = None

    with urllib.request.urlopen(url) as response:
        data = json.load(response)

        for item in data.get('results', []):
            if (
                item.get('artistName', '').strip().lower() == album_data['artist'].strip().lower()
                and item.get('collectionName', '').strip().lower() == album_data['album'].strip().lower()
            ):
                # if the data match, return the image URL
                img_url = item.get('artworkUrl100')
                print(f'{album_data["album"]}')

                if img_url:
                    img_url = img_url.rsplit('/', 1)[0] + '/1000x1000.jpg'

                    print(f'{img_url}')

                    file_name = f'{album_data["album"].replace(' ', '_')}.jpg'

                    urllib.request.urlretrieve(img_url, file_name)

                    open_img(file_name)
                    
                    break

        if not img_url:
            print('Nenhuma capa encontrada')