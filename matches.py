from functools import reduce 

def matches(query, songs):
    return [song for song in songs if matches_name(query, song) or matches_artist(query, song)]

def matches_name(query, field):
    return query.lower() == field["name"].lower()

def matches_artist(query, song):
    return len([artist for artist in song["artists"] if matches_name(query, artist)]) > 0