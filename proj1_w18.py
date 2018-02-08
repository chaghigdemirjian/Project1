import requests
import json
import sys
import webbrowser


json_sample = open('sample_json.json', 'r')
json_sample_data = json_sample.read()
sample_results_list = json.loads(json_sample_data)


class Media:

	def __init__(self, title="No title", author="no author",
	release_year = "no release year", json_dict = None, url = 'NA'):

		if json_dict is not None:
			if json_dict["wrapperType"] == "track":
				self.title = json_dict["trackName"]
				self.url = json_dict["trackViewUrl"]

			else:
				self.title = json_dict["collectionName"]
				self.url = json_dict["collectionViewUrl"]

			self.author = json_dict["artistName"]
			mediaYear = json_dict["releaseDate"]
			self.release_year = mediaYear[0:4]


		else:
			self.title = title
			self.author = author
			self.release_year = release_year

	def __str__(self):
		return self.title + " by " + self.author + " (" + self.release_year + ")"

	def __len__(self):
		return 0

class Song(Media):

	def __init__(self, title = "No title", author = "no author", release_year = "no release year",
	album = "no album name", genre = "no genre", track_length = "NA", json_dict = None):

		super().__init__(title, author, release_year, json_dict)
		if json_dict is not None:
			self.album = json_dict["collectionName"]
			self.genre = json_dict["primaryGenreName"]
			self.track_length = json_dict["trackTimeMillis"]

		else:
			self.album = album
			self.genre = genre
			self.track_length = track_length

	def __str__(self):
		return super().__str__() + " [" + self.genre + "]"

	def __len__(self):
		return self.track_length / (1000)

class Movie(Media):

	def __init__(self, title = 'No title', author = "no author",
	release_year = "no release year", rating = "no rating",
	movie_length = "NA", json_dict = None):

		super().__init__(title, author, release_year, json_dict)
		if json_dict is not None:
			self.rating = json_dict["contentAdvisoryRating"]
			self.movie_length = json_dict["trackTimeMillis"]

		else:
			self.rating = rating
			self.movie_length = movie_length

	def __str__(self):
		return super().__str__() + " [" + self.rating + "]"

	def __len__(self):
		return round(self.movie_length / (1000 * 60))

def get_itunes_data(search_term):
	base_url = 'https://itunes.apple.com/search?'
	json_data = requests.get(base_url, {'term': search_term})
	results_list = json.loads(json_data.text)

	return results_list['results']


if __name__ == "__main__":

	search_term = input(" Enter a search term, or exit")
	if search_term == "exit":
		exit()

	elif search_term.isdigit():
		search_term = input("You cannot enter an integer at this point. Please re-run the program")
		exit()

	else:

		while search_term != "exit":

			if search_term.isdigit():
				print("Launching")
				webbrowser.open(urls[int(search_term)])
				print("In web browser...")


			elif len(get_itunes_data(search_term)) == 0:
				print('There were no results under this search. Try another search')

			else:
				results_list = get_itunes_data(search_term)

				Songs = []
				Movies = []
				Other_Media = []
				urls = {}
				count = 1

				for i in results_list:
					if i["wrapperType"] == "track":
						if i["kind"] == "song":
							Songs.append(i)
						elif i["kind"] == "feature-movie":
							Movies.append(i)
					else:
						Other_Media.append(i)

				print("Songs")
				for x in Songs:
					song = Song(json_dict = x)
					urls.update({count:song.url})
					print(count, song.__str__())
					count += 1

				print("")
				print("Movies")
				for y in Movies:
					movie = Movie(json_dict = y)
					urls.update({count:movie.url})
					print(count, movie.__str__())
					count += 1

				print("")
				print("Other media")
				for z in Other_Media:
					media = Media(json_dict = z)
					urls.update({count:media.url})
					print(count, media.__str__())
					count += 1
			search_term = input("Enter a number for more info, or another search term, or exit")

	pass
