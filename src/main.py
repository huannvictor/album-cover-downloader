import urllib.request
import urllib.parse
import json
import os

from data_entry import data_entry
from fetch_album_api import fetch_album_api

def main():
    try:
        data = data_entry()
        album = data['album']
        artist = data['artist']

        url = fetch_album_api(data)

        img_url = None

        with urllib.request.urlopen(url) as response:
            data = json.load(response)

            for item in data.get('results', []):
                if (
                    item.get('artistName', '').strip().lower() == artist.strip().lower()
                    and item.get("collectionName", "").strip().lower() == album.strip().lower()
                ):
                    
                    img_url = item.get("artworkUrl100")

                    if img_url:
                        img_url = img_url.rsplit('/', 1)[0] + '/1000x1000.jpg'
                        print(f'{img_url}')

                        file_name = f'{album.replace(' ', '_')}.jpg'

                        urllib.request.urlretrieve(img_url, file_name)

                        os.startfile(file_name)

                        break

            if not img_url:
                print('Nenhua capa encontrada correspondente.')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


if __name__ == "__main__":
    main()