from typing import List, Callable, Dict

from seat import Seat


class MovieHall:
    def __init__(self, number: int, seats: List[List[Seat]]):
        self.movie_hall_schema = seats
        self.number = number

    @classmethod
    def create_movie_hall(cls, movie_halls_schema: dict):
        seats = [
            [Seat(index) if index else None for index in row]
            for row in movie_halls_schema['rows']
        ]
        return cls(int(movie_halls_schema['number']), seats)
