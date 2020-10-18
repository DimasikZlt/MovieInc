import random
from datetime import timedelta, datetime
from typing import Tuple

from movie import Movie
from movie_hall import MovieHall
from movie_house import MovieHouse


class Timetable:
    def __init__(self, start_time: datetime, movie: Movie, movie_hall: MovieHall):
        self.start_time = start_time
        self.movie = movie
        self.movie_hall = movie_hall

    @classmethod
    def create_movies_timetable(cls, movies: Tuple[Movie], movie_house: MovieHouse):
        start_time = datetime.now()
        start_time = start_time.replace(hour=9, minute=0, second=0)
        end_time = start_time.replace(hour=22, minute=0, second=0)
        movies_timetable = []
        while start_time < end_time:
            movie = random.choice(movies)
            movies_timetable.append(
                cls(start_time, movie, random.choice(movie_house.movie_halls))
            )
            start_time = start_time + movie.duration + timedelta(minutes=15)
        return movies_timetable
