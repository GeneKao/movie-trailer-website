import fresh_tomatoes
import webbrowser

class Video():
	video_type = "video"

	"""Class for the video, this is the parent class of Movie and TvShow

	Attributes:
        video_title (str): video title.
        rating (str): video rating score.
        storyline (str): video description.
        poster_image (str): video image.
        trailer_youtube (str): video trailer link from youtube.
	"""

	def __init__(self, video_title, rating, storyline, poster_image,
				trailer_youtube):
		self.title = video_title
		self.rating = rating
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
	video_type = "movie"

	""" Movie is a child class of Video, and having extra attributes
		publish_year and duration

	Attributes:
        video_title (str): movie title.
        rating (str): movie rating score.
        storyline (str): movie description.
        poster_image (str): movie image.
        trailer_youtube (str): movie trailer link from youtube.
        publish_year (str): movie release year.
        duration (str): movie duration.

	"""
	def __init__(self, movie_title, rating, movie_storyline, poster_image,
				trailer_youtube, publish_year, duration):
		Video.__init__(self, movie_title, rating, movie_storyline,
						poster_image, trailer_youtube)
		self.year = publish_year
		self.duration = duration



class TvShow(Video):
	video_type = "tvShow"

	tv_episodes = []

	""" TvShow is a child class of Video, and having extra attributes
		season and tv_station

	Attributes:
        video_title (str): tv show title.
        rating (str): tv show rating score.
        storyline (str): tv show description.
        poster_image (str): tv show image.
        trailer_youtube (str): tv show trailer link from youtube.
        season (str): tv show season.
        tv_station (str): ttv showv station.

	"""
	def __init__(self, tv_title, rating, tv_storyline, poster_image,
				trailer_youtube, season, tv_station):
		Video.__init__(self, tv_title, rating, tv_storyline,
						poster_image, trailer_youtube)
		self.season = season
		self.tv_station = tv_station

	def get_episodes(self):
		episodes_text = ""
		for count, episode in enumerate(self.tv_episodes):
			text = str(count) + " " + episode + ", "
			episodes_text += text

		return episodes_text
