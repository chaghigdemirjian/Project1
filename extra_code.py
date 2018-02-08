other CODE
#and json_dict["kind"]
 #== "feature-movie" or "song":


#     def __init__(self, title = 'No title', author = "no author",
# 	release_year = "no release year", rating = "no rating",
# 	movie_length, json_dict = None):
#
# questions
# - is JSON code okay so far
# - line 72 has the code below but why isnt it working - none != 230
# - part 3 - do I just pull in requests and save them in a library?
# - part 4 - do I just search through current dictionaries and if not found
# search the api (what do you mean can search term like love)
#time??

# base url, parameters (seerch term, limitations, media type = all), request get, load, return['results']

#         if self.track_length == int:
# 			return self.track_length / (1000)
# 		else:
# 			print('No track length')


# 		if self.movie_length == int:
# 			return self.track_length / (1000 * 60)
# 		else:
# 			print('no movie length

	# def process_json(self, json_dict):
	# 	for item in json_dict: #move up
	# 		if json_dict["wrapperType"] == "track":
	# 			if json_dict["kind"] == "feature-movie" or json_dict["kind"] == "song":
	# 				self.go_to(json_dict = self.json_dict)
	# 				json_dict.next()

    #
    #
	# def go_to(self, json_dict): #remove
	# 	if json_dict["kind"] == "song":
	# 		self.Song(json_dict = self.json_dict)
	# 	elif json_dict["kind"] == "feature-movie":
	# 		self.Movie(json_dict = self.json_dict)
