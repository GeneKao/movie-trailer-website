import webbrowser


class Video():
    """Class for the video, this is the parent class of Movie and TvShow.

    Attributes:
        video_title (str): video title.
        rating (str): video rating score.
        storyline (str): video description.
        poster_image (str): video image.
        trailer_youtube (str): video trailer link from youtube.
    """

    # A variable to determine if this movie or tv show.
    video_type = "video"

    def __init__(self, video_title, rating, storyline,
                 poster_image, trailer_youtube):
        """Initial function."""
        self.title = video_title
        self.rating = rating
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open web browser."""
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """Movie is a child class of Video, and having extra attributes.

    Attributes:
        video_title (str): movie title.
        rating (str): movie rating score.
        storyline (str): movie description.
        poster_image (str): movie image.
        trailer_youtube (str): movie trailer link from youtube.
        publish_year (str): movie release year.
        duration (str): movie duration.
    """

    video_type = "movie"

    def __init__(self, movie_title, rating, movie_storyline, poster_image,
                 trailer_youtube, publish_year, duration):
        """Initial function."""
        Video.__init__(self, movie_title, rating, movie_storyline,
                       poster_image, trailer_youtube)
        self.year = publish_year
        self.duration = duration


class TvShow(Video):
	"""TvShow is a child class of Video, and having extra attributes.

    Attributes:
        video_title (str): tv show title.
        rating (str): tv show rating score.
        storyline (str): tv show description.
        poster_image (str): tv show image.
        trailer_youtube (str): tv show trailer link from youtube.
        season (str): tv show season.
        tv_station (str): ttv showv station.
    """

    video_type = "tvShow"
    tv_episodes = []

    def __init__(self, tv_title, rating, tv_storyline, poster_image,
                 trailer_youtube, season, tv_station):
        """Initial function."""
        Video.__init__(self, tv_title, rating, tv_storyline,
                       poster_image, trailer_youtube)
        self.season = season
        self.tv_station = tv_station

    def get_episodes(self):
        """str: return episode text together with labels."""
        episodes_text = ""
        for count, episode in enumerate(self.tv_episodes):
            text = str(count) + " " + episode + ", "
            episodes_text += text

        return episodes_text
