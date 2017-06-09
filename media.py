class Movie():
    '''
    The representation of a movie
    '''

    def __init__(self, title, storyline, trailer_youtube_url, poster_image_url):
        '''
        :param title: Movie title.
        :param storyline: Movie plot.
        :param youtube_link: URL of the youtube trailer
        :param poster_image_url: URL of the movie image
        '''
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
