from typing import List, Callable, Dict

from seat import Seat


class MovieHall:
    def __init__(self, number: int, seats: List[List[Seat]]):
        self.movie_hall_schema = seats
        self.number = number

    @classmethod
    def create_movie_hall(cls, movie_halls_schema):
        seats = []
        for row in movie_halls_schema['rows']:
            seats.append([Seat(index) for index in row])
        return MovieHall(int(movie_halls_schema['number']), seats)
