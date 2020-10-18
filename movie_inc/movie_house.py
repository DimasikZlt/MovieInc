from typing import Callable, List

from movie_hall import MovieHall


class MovieHouse:
    def __init__(self, name: str, address: str, movie_halls: List[MovieHall]):
        self.name = name
        self.address = address
        self.movie_halls = movie_halls

    @classmethod
    def create_movie_house(cls, loader: Callable, movie_halls_schema_file: str):
        movie_halls_schema = loader(movie_halls_schema_file)
        movie_halls = [
            MovieHall.create_movie_hall(number) for number in movie_halls_schema['movie_halls']
        ]
        return cls(movie_halls_schema['name'], movie_halls_schema['address'], movie_halls)
