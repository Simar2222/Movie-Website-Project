import webbrowser

"""The class 'Movie' models a movie entry of our movie database.
    Attributes:
        title: Title of the movie
        year = The year the movie was released
        rating = IMDb rating
        poster_url: URL to a poster of the movie
        trailer_youtube_urls: List of youtube urls to trailers of the movie
    """

class Movie():
    def __init__(self, title, year, rating, poster_image, trailer_youtube):
        """Initializes a Movie object"""
        self.title = title
        self.year = year
        self.rating = rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    """make a class method to show a trailer"""

