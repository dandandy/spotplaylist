import re

def extract_id_from_uri(uri):
    if "spotify:playlist:" in uri:
        return re.search(r'(?<=spotify:playlist:).+', uri).group(0)
    else:
        return uri