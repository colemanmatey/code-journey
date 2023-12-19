"""
The Factory Design Pattern
"""
# In serializer_demo.py

import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)
        
def get_serializer(format):
    if format == 'JSON':
        return to_json
    elif format == 'XML':
        return to_xml
    else:
        raise ValueError(format)
    
def to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)

def to_xml(song):
    song_info = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_info, 'title')
    title.text = song.title
    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist
    return et.tostring(song_info, encoding='unicode')


song = Song('1', 'Water of Love', 'Dire Straits')

serializer = SongSerializer()


json_data = serializer.serialize(song, 'JSON')
print(json_data)

xml_data = serializer.serialize(song, 'XML')
print(xml_data)

yaml_data = serializer.serialize(song, 'YAML')
print(yaml_data)