
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

my_playlist = Playlist(["Song A", "Song B", "Song C"])
print(len(my_playlist)) 

# 3