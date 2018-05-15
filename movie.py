import webbrowser

class Movie():
    """
    Description: This class stores movie information

    Attributes:
        title (str): The movie's title
        summary (str): The movie's synopsis
        poster_image_url (str): The movie's poster image
        trailer_youtube_url (str): The movie's trailer
    """

    def __init__(self, title, summary, image, trailer_url):
        self.title = title
        self.summary = summary
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url);
