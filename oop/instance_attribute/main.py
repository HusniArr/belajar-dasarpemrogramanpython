class Song:
    note = "A class type to represent a song"
    version = 1.0

    def __init__(self, name = "", artist = "", album = "", released_year = 2000):
        self.name = name
        self.artist = artist
        self.album = album
        self.released_year = released_year 

    def info(self):
        print(f"Song: {self.name} by {self.artist}") 
        print(f"Album: {self.album}")
        print(f"Released year: {self.released_year}")


songs = [
    Song(
        name="The Ytse Jam",
        artist="Dream Theater",
        album="When dream and day unite",
        released_year=2004
    ),
    Song(
        name="Always with me, Always with you",
        artist="Joe Satriani",
        album="Surfing with alien",
        released_year=1987
    )
]

print(f"Class: Song, version: {Song.version}, note: {Song.note}")

for s in songs:
    s.info()