from typing import Callable

from movie_hall import MovieHall


class MovieHouse:
    def __init__(self):
        pass

    @classmethod
    def create_movie_house(cls, loader: Callable, movie_halls_schema_file: str):
        movie_halls_schema = loader(movie_halls_schema_file)
        return MovieHall.create_movie_hall(movie_halls_schema['movie_halls'][0])
