import json

from dataclasses import dataclass

@dataclass
class Album:
  title: str
  artist: str
  year: int
  
  def to_json(self):
    """
    Return album in json format
    """
    d = {'title': self.title, 'artist': self.artist, 'year': self.year}
    return json.dumps(d, indent=4)