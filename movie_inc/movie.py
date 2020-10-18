from collections import namedtuple
from datetime import timedelta
from typing import Callable


class Movie:
    def __init__(self, movie_title: str, duration: int, description: str):
        self.movie_title = movie_title
        self.duration = timedelta(minutes=duration)
        self.description = description

    @classmethod
    def create_movies_db(cls, loader: Callable, movies_db_file: str):
        movies_db = loader(movies_db_file)
        return tuple(
            cls(movie['movie_title'], movie['duration'], movie['description'])
            for movie in movies_db['movies']
        )
