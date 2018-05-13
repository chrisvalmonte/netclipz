import webbrowser

class Movie():
    def __init__(self, title, summary, image, trailer_url):
        self.title = title
        self.summary = summary
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url);
