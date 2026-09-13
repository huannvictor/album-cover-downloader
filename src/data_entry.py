from typing import TypedDict

class DataEntyType(TypedDict):
    album: str
    artist: str

def data_entry() -> DataEntyType:
    album = input("Insira o nome do album: ")
    artist = input("De qual artista/banda: ")

    return {
        "album": album,
        "artist": artist
    }