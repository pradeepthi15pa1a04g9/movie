import webbrowser


class Movie():
        VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]

        """This class contain the srtructure of the object movie"""
        # Constructor of the class
        def __init__(self, movie_title, movie_storyline,
                     poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube
        # Method to show the trailer of a movie in the browser

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)

            
