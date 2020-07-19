import argparse
from songs import get_songs, extract_details
from matches import matches 
import json

def get_args():
    parser = argparse.ArgumentParser(description='Use a query string to search a list of spotify playlists')

    parser.add_argument('--playlist', "-p", help="spotify playlist URI", required=True, action="append")
    parser.add_argument('--query', "-q", help="query string", required=True)
    parser.add_argument('--verbose', "-v", help="verbose output", action="store_false", default=False)
    return parser.parse_args()

def build_url(uri):
    return "https://open.spotify.com/playlist/" + uri

def run():
    args = get_args()
    urls = [build_url(uri) for uri in args.playlist]
    songs = [song for url in urls for song in get_songs(url)]

    matched_songs = matches(args.query, songs)
    if args.verbose:
        print(json.dumps(matched_songs))
    else:
        print(json.dumps([extract_details(song) for song in matched_songs]))

if __name__ == "__main__":
    run()