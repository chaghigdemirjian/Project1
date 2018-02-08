import requests
import json
import sys
import webbrowser

#opening and reading sample json file to understand the structure of the
#json output and test our preliminary code

json_sample = open('sample_json.json', 'r')
json_sample_data = json_sample.read()
sample_results_list = json.loads(json_sample_data)


class Media:

	def __init__(self, title="No title", author="no author",
	release_year = "no release year", json_dict = None, url = 'NA'):

#The code below checks if a JSON input was provided as a parameter and
#then chooses if it should initialize variables from the provided fictionary or
#assign default or inputted paramters

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

#this allows us to output a string of information that are relevant to
#the media item

	def __str__(self):
		return self.title + " by " + self.author + " (" + self.release_year + ")"

	def __len__(self):
		return 0

class Song(Media):

	def __init__(self, title = "No title", author = "no author", release_year = "no release year",
	album = "no album name", genre = "no genre", track_length = "NA", json_dict = None):

#super allows the song class to inherit variables from the parent(Media) class
#and then either initializes the variables from either the JSON sample or
#the init functions parameters

		super().__init__(title, author, release_year, json_dict)
		if json_dict is not None:
			self.album = json_dict["collectionName"]
			self.genre = json_dict["primaryGenreName"]
			self.track_length = json_dict["trackTimeMillis"]

		else:
			self.album = album
			self.genre = genre
			self.track_length = track_length

#str inherits the previous return from Media and adds a song specific variable
#to it

	def __str__(self):
		return super().__str__() + " [" + self.genre + "]"

#this returns the length that is stores in milliseconds in seconds

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

#str inherits the previous return from Media and adds a movie specific variable
#to it

	def __str__(self):
		return super().__str__() + " [" + self.rating + "]"

#this returns the length that is stores in milliseconds in minutes
	def __len__(self):
		return round(self.movie_length / (1000 * 60))

#this function essentially allows us to connect to and request data from
#itunes search and stores it as a JSON file

def get_itunes_data(search_term):
	base_url = 'https://itunes.apple.com/search?'
	json_data = requests.get(base_url, {'term': search_term})
	results_list = json.loads(json_data.text)
	return results_list['results']

if __name__ == "__main__":

	search_term = input(" Enter a search term, or exit")
	if search_term == "exit":
		print("Peace out. Come again.")
		exit()

#we wont allows users to open a specific url of a media item they are intersted
#in until we have actually made a request for data from itunes

	elif search_term.isdigit():
		search_term = input("You cannot enter an integer at this point. Please re-run the program")
		print("Peace out. Come again.")
		exit()

#the while function below essentially allows us to allow the user to request data as
#long as they don't choose to exit the program by typing exit
	else:

		while search_term.lower() != "exit":

			if search_term.isdigit():
				print("Launching")
				webbrowser.open(urls[int(search_term)])
				print("In web browser...")

#if the user doesnt input anything or inputs a query with no results. Then they
#are prompted to enter another search

			elif len(get_itunes_data(search_term)) == 0:
				print('There were no results under this search. Try another search')

#this block of code allows us to parse through our media restults and create lists
#of songs, movies and other media types because each of those media types are
#processed differently by our previous functions based on classes they belong to

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

				print("SONGS")
				for x in Songs:
					song = Song(json_dict = x)
					urls.update({count:song.url})
					print(count, song.__str__())
					count += 1

				print("")
				print("MOVIES")
				for y in Movies:
					movie = Movie(json_dict = y)
					urls.update({count:movie.url})
					print(count, movie.__str__())
					count += 1

				print("")
				print("OTHER MEDIA")
				for z in Other_Media:
					media = Media(json_dict = z)
					urls.update({count:media.url})
					print(count, media.__str__())
					count += 1
			search_term = input("Enter a number for more info, or another search term, or exit")
	print("Peace out. Come again.")

	pass
