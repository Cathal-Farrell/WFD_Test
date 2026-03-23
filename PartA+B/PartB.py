import unittest
from PartA import *

class TestObjects(unittest.TestCase):
    def test_is_instance(self):
        song1 = Song("The Outside", "Taylor Swift", 2004)
        album1 = Album("Example Album", "Taylor Swift", 2004)
        artist1 = Artist("Taylor Swift", 1990, "USA")
        playlist1 = Playlist("My Playlist")
        self.assertIsInstance(song1, Song)
        self.assertIsInstance(album1, Album)
        self.assertIsInstance(artist1, Artist)
        self.assertIsInstance(playlist1, Playlist)
    
    def test_is_not_instance(self):
        song1 = Song("The Outside", "Taylor Swift", 2004)
        album1 = Album("Example Album", "Taylor Swift", 2004)
        artist1 = Artist("Taylor Swift", 1990, "USA")
        playlist1 = Playlist("My Playlist")

        self.assertNotIsInstance(song1, Album)
        self.assertNotIsInstance(song1, Artist)
        self.assertNotIsInstance(song1, Playlist)

        self.assertNotIsInstance(album1, Song)
        self.assertNotIsInstance(album1, Artist)
        self.assertNotIsInstance(album1, Playlist)

        self.assertNotIsInstance(artist1, Song)
        self.assertNotIsInstance(artist1, Album)
        self.assertNotIsInstance(artist1, Playlist)

        self.assertNotIsInstance(playlist1, Song)
        self.assertNotIsInstance(playlist1, Album)
        self.assertNotIsInstance(playlist1, Artist)

    def test_is_identical(self):
        song1 = Song("The Outside", "Taylor Swift", 2004)
        song2 = song1

        self.assertEqual(song1, song2)
        self.assertEqual(song1, song1)

    def test_is_almost_identical(self):
        song1 = Song("The Outside", "Taylor Swift", 2004)
        song2 = Song("The Outside", "Taylor Swift", 2004)

        self.assertAlmostEqual(song1.display_info(), song2.display_info())

    def test_add_methods(self):
        song1 = Song("The Outside", "Taylor Swift", 2004)
        album1 = Album("Example Album", "Taylor Swift", 2004)
        artist1 = Artist("Taylor Swift", 1990, "USA")
        playlist1 = Playlist("My Playlist")

        album1.add_song("The Outside", 2004)
        self.assertEqual(album1.albumSongs[0].songTitle, "The Outside")

        artist1.add_song(song1)
        self.assertEqual(artist1.songList[0].songTitle, "The Outside")

        artist1.add_album(album1)
        self.assertEqual(artist1.albumList[0].albumTitle, "Example Album")

        playlist1.add_song(song1)
        self.assertEqual(playlist1.plSongs[0].songTitle, "The Outside")

    def test_sort_playlist(self):
        playlist1 = Playlist("My Playlist")
        song1 = Song("The Outside", "Taylor Swift", 2004)
        song2 = Song("Tim McGraw", "Taylor Swift", 2004)
        song3 = Song("Picture To Burn", "Taylor Swift", 2004)
        playlist1.add_song(song1)
        playlist1.add_song(song2)
        playlist1.add_song(song3)

        playlist1.sort_playlist("ASC")
        self.assertEqual(playlist1.plSongs, [song3, song1, song2])

        playlist1.sort_playlist("DES")
        self.assertEqual(playlist1.plSongs, [song2, song1, song3])


unittest.main()