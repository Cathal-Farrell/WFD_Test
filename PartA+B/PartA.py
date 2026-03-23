import random

class Song:
    
    def __init__(self, title, artist, release):
        self.songTitle = title
        self.artist = artist
        self.releaseYear = release

    def display_info(self):
        print(f"Title: {self.songTitle}   Artist: {self.artist}   YoR: {self.releaseYear}")

    

class Album:

    def __init__(self, title, artist, release):
        self.albumTitle = title
        self.artist = artist
        self.releaseYear = release
        self.albumSongs = []

    def add_song(self, title, release):
        self.albumSongs.append(Song(title, self.artist, release))

    def display_info(self):
        print(f"Title: {self.albumTitle}   Artist: {self.artist}   YoR: {self.releaseYear}\nSongs:")
        for i in self.albumSongs:
            print(i.songTitle)


class Artist:

    def __init__(self, name, DOB, country):
        self.artistName = name
        self.DOB = DOB
        self.country = country
        self.albumList = []
        self.songList = []

    def add_album(self, album):
        self.albumList.append(album)
    
    def add_song(self, song):
        self.songList.append(song)

    def display_info(self):
        print(f"Name: {self.artistName}   DOB: {self.DOB}   Country: {self.country}\nAlbums:")
        for i in self.albumList:
            print(i.albumTitle)
        print("Songs:")
        for i in self.songList:
            print(i.songTitle)


class Playlist:

    def __init__(self, title):
        self.playlistTitle = title
        self.plSongs = []

    def add_song(self, song):
        self.plSongs.append(song)

    def print_all_song(self):
        print("Playlist's songs:")
        for i in self.plSongs:
            print(i.songTitle)

    def sort_playlist(self, order):
        if (order == "ASC"):
            n = len(self.plSongs)
            for i in range(n-1):
                for j in range(n-i-1):
                    if self.plSongs[j].songTitle > self.plSongs[j+1].songTitle:
                        self.plSongs[j], self.plSongs[j+1] = self.plSongs[j+1], self.plSongs[j]
        elif (order == "DES"):
            n = len(self.plSongs)
            for i in range(n-1):
                for j in range(n-i-1):
                    if self.plSongs[j].songTitle < self.plSongs[j+1].songTitle:
                        self.plSongs[j], self.plSongs[j+1] = self.plSongs[j+1], self.plSongs[j]

    def shuffle_playlist(self):
        random.shuffle(self.plSongs)
        



print("Song test")
song1 = Song("The Outside", "Taylor Swift", 2004)
song1.display_info()

print("\nAlbum test")
album1 = Album("Example Album", "Taylor Swift", 2004)
album1.add_song("Tim McGraw", 2004)
album1.add_song("Picture To Burn", 2004)
album1.display_info()

print("\nArtist test")
artist1 = Artist("Taylor Swift", 1990, "USA")
artist1.add_album(album1)
artist1.add_song(song1)
song2 = Song("Tim McGraw", "Taylor Swift", 2004)
artist1.add_song(song2)
song3 = Song("Picture To Burn", "Taylor Swift", 2004)
artist1.add_song(song3)
artist1.display_info()

print("\nPlaylist test")
playlist1 = Playlist("My Playlist")
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)
print(f"Name: {playlist1.playlistTitle}")
playlist1.print_all_song()

print("\nAscending order")
playlist1.sort_playlist("ASC")
playlist1.print_all_song()

print("\nDescending order")
playlist1.sort_playlist("DES")
playlist1.print_all_song()

print("\nShuffle 1")
playlist1.shuffle_playlist()
playlist1.print_all_song()

print("\nShuffle 2")
playlist1.shuffle_playlist()
playlist1.print_all_song()