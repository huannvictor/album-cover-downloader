import urllib.request
import json
import os

from data_entry import data_entry
from fetch_album_api import fetch_album_api
from process_data import process_data

def main():
    try:
        album_data = data_entry()
        url = fetch_album_api(album_data)
        process_data(url, album_data)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


if __name__ == "__main__":
    main()