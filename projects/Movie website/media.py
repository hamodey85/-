import webbrowser
class Movie():
    def __init__(self,data):
        self.title = data["title"]
        self.storyline = data["storyline"]
        self.poster_image_url = data["poster_image_url"]
        self.trailer_url = data["trailer_url"]
    
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
