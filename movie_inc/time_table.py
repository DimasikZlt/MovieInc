from datetime import datetime

from movie_hall import MovieHall


class TimeTable:
    def __init__(
            self,
            start_time: datetime,
            end_time: datetime,
            movie_title: str,
            movie_hall: MovieHall,
            description: str
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.movie_title = movie_title
        self.movie_hall = movie_hall
        self.description = description
