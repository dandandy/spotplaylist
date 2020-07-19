import requests
from lxml import html
import re
import json

def get_songs(url):
    res = requests.get(url)
    if res.status_code != 200:
        status_code=res.status_code
        raise Exception(f"response status code {status_code} for {url}")

    matched_nodes = [node.text for node in html.fromstring(res.text).xpath('//script') if node is not None and node.text is not None and "Spotify.Entity" in node.text]
    if len(matched_nodes) != 1:
        raise Exception(f"could not retrieve songs json from url {url}")
    node = matched_nodes.pop()
    return extract_track(extract_items(json.loads(extract_songs_json(node))))

def extract_songs_json(text):
    return re.search(r'{.+}', text).group(0)

def extract_items(full):
    return full["tracks"]["items"]

def extract_track(tracks):
    return [track["track"] for track in tracks]

def extract_details(song):
    return {"name": song["name"], "artist": [artist["name"] for artist in song["artists"]], "album": song["album"]["name"]}

if "__main__" == __name__:
    print(get_songs("https://open.spotify.com/playlist/3sQa1JxjWR4PmuUDk5Egzf"))