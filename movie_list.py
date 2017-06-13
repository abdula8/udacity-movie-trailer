import json
from media import Movie


def get_movie_list():
    '''
    Fetch the movie list

    This currently fetches the movie list from a JSON file
    but can be updated later to fetch from a remote endpoint
    '''

    movie_list = []
    with open('movie_list.json', 'r') as json_file:
        movie_list_json = json.load(json_file)
        for movie_json in movie_list_json:
            movie_list.append(Movie(
                title=movie_json['title'],
                storyline=movie_json['storyline'],
                trailer_youtube_url=movie_json['trailer_youtube_url'],
                poster_image_url=movie_json['poster_image_url'],
            ))

    return movie_list
