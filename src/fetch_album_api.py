from typing import TypedDict

import urllib.parse
from data_entry import DataEntyType, data_entry


def fetch_album_api(data: DataEntyType) -> str:

    searchTerm = urllib.parse.quote(f'{data["album"]} {data["artist"]}')

    url = f'https://itunes.apple.com/search?term={searchTerm}&media=music&entity=song'

    return url