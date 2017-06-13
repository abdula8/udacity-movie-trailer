import json
from media import Movie


def get_movie_list():
    '''
    Fetch the movie list

    This currently fetches the movie list from a JSON file
    but can be updated later to fetch from a remote endpoint
    '''

    with open('movie_list.json', 'r') as json_file:
        return [Movie(**i) for i in json.load(json_file)]
