import unittest
import proj1_w18 as proj1
import json
import requests

#again,opening up our json file to test a local sample of data that is saved
#in our repository

json_sample = open('sample_json.json', 'r')
json_sample_data = json_sample.read()
sample_results_list = json.loads(json_sample_data)
json_sample.close()

class TestClasses(unittest.TestCase):

#init test code essentially checks that each iten in a class has the instance
#variables it's supposed to have and that default parameters are working fine

    def test_init(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince", "1982")

        self.assertEqual(m1.title, "No title")
        self.assertEqual(m1.author, "no author")
        self.assertEqual(m1.release_year, "no release year")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.release_year, "1982")
        self.assertIsInstance(m2.author, str)
        self.assertEqual(hasattr(m2, "rating"), False)
        self.assertEqual(hasattr(m2, "track_length"), False)

        m3 = proj1.Song()
        m4 = proj1.Song("Starboy", "no author", "2016", "Starboy", "R&B/soul",
        230000)

        self.assertEqual(m3.title, "No title")
        self.assertEqual(m3.genre, "no genre")
        self.assertEqual(m4.genre, "R&B/soul")
        self.assertEqual(m4.title, "Starboy")
        self.assertEqual(m4.track_length, 230000)
        self.assertEqual(hasattr(m4, "rating"), False)
        self.assertEqual(hasattr(m4, "movie_length"), False)

        m5 = proj1.Movie()
        m6 = proj1.Movie("A Walk to Remember", "Nicholas Sparks", "2002",
        "PG", 6130000)

        self.assertEqual(m5.title, "No title")
        self.assertEqual(m5.movie_length, "NA")
        self.assertEqual(m6.title, "A Walk to Remember")
        self.assertEqual(m6.rating, "PG")
        self.assertEqual(m6.movie_length, 6130000)
        self.assertEqual(hasattr(m6, "genre"), False)
        self.assertEqual(hasattr(m5, "track_length"), False)


    def test_str(self):
        m1 = proj1.Media("Starboy", "The Weeknd", "2016")
        m2 = proj1.Media()

        self.assertEqual(m1.__str__(), "Starboy by The Weeknd (2016)")
        self.assertEqual(m2.__str__(), "No title by no author (no release year)")

        m3 = proj1.Song("Starboy", "no author", "2016", "Starboy", "R&B/soul",
        230000)

        self.assertEqual(m3.__str__(), "Starboy by no author (2016) [R&B/soul]")

        m4 = proj1.Movie("A Walk to Remember", "Nicholas Sparks", "2002",
        "PG", 6130000)

        self.assertEqual(m4.__str__(), "A Walk to Remember by Nicholas Sparks (2002) [PG]")

    def test_len(self):
        m1 = proj1.Media("Starboy")

        self.assertEqual(m1.__len__(), 0)

        m2 = proj1.Song("Starboy", "no author", "2016", "Starboy", "R&B/soul",
        230000)

        self.assertEqual(m2.__len__(), 230)

        m3 = proj1.Movie("A Walk to Remember", "Nicholas Sparks", "2002",
        "PG", 6130000)

        self.assertEqual(m3.__len__(), 102)

#this code allows us to do the same as above, but instead of working with
#user inputted variables, we are extracting results from a json file
#which in this case is the sample json file

    def test_JSON(self):
        m1 = proj1.Media(json_dict = sample_results_list[2])

        self.assertEqual(len(sample_results_list), 3)
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(hasattr(m1, "rating"), False)
        self.assertEqual(hasattr(m1, "track_length"), False)
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(m1.__len__(), 0)

        m2 = proj1.Song(json_dict = sample_results_list[1])

        self.assertEqual(m2.title, "Hey Jude")
        self.assertEqual(m2.album, "TheBeatles 1967-1970 (The Blue Album)")
        self.assertEqual(m2.author, "The Beatles")
        self.assertEqual(m2.genre, "Rock")
        self.assertEqual(hasattr(m2, "rating"), False)
        self.assertEqual(hasattr(m2, "movie_length"), False)
        self.assertEqual(m2.__str__(), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(m2.__len__(), 431.333)

        m3 = proj1.Movie(json_dict = sample_results_list[0])

        self.assertEqual(m3.title, "Jaws")
        self.assertEqual(m3.rating, "PG")
        self.assertEqual(hasattr(m3, "track_length"), False)
        self.assertEqual(hasattr(m3, "genre"), False)
        self.assertEqual(m3.__str__(), "Jaws by Steven Spielberg (1975) [PG]")
        self.assertEqual(m3.__len__(), 124)

#this allows us to check that the results we're getting are the right length
#the default length of results is 50, so we're making sure theres no results above that
#also checks that queries that should be invalid and not return results are working properly
    def test_getItunesData(self):
        m1 = proj1.get_itunes_data(search_term ="")
        self.assertEqual(len(m1), 0)

        m2 = proj1.get_itunes_data(search_term = "love")
        self.assertEqual(len(m2) <= 50, True)

        m3 = proj1.get_itunes_data(search_term = "baby")
        self.assertEqual(len(m3) <= 50, True)

        m4 = proj1.get_itunes_data(search_term = "")
        self.assertEqual(len(m4) <= 50, True)

        m5 = proj1.get_itunes_data(search_term ="##!!")
        self.assertEqual(len(m5), 0)

        m6 = proj1.get_itunes_data(search_term = "moana")
        self.assertEqual(len(m6) <= 50, True)

        m7 = proj1.get_itunes_data(search_term = "helter skelter")
        self.assertEqual(len(m7) <= 50, True)

        m8 = proj1.get_itunes_data(search_term = "demirjian")
        self.assertEqual(len(m8) <= 50, True)

        m9 = proj1.get_itunes_data(search_term = "palig")
        self.assertEqual(len(m9) <= 50, True)

unittest.main()
