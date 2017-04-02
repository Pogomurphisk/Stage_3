import webbrowser

class Movie():
	"""A class that contains methods and information on movies"""

	def __init__(self, movie_title, poster_image,
				 trailer_youtube):
		"""Initialize instance of movie class using movie_title, which is a
		string of the movie title, poster_image, a url of the movie poster,
		and trailer_youtube, a link to the movie trailer on youtube."""

		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""Open an instance of this movie's trailer in youtube"""
		
		webbrowseropen(self.trailer_youtube_url)