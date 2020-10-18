from movie import Movie
from movie_house import MovieHouse
from timetable import Timetable
from tools.yaml_loader import load_yaml

# movie_hall_schema = load_yaml('../data/cronverk.yml')
movie_house = MovieHouse.create_movie_house(load_yaml, '../data/cronverk.yml')
movies_db = Movie.create_movies_db(load_yaml, '../data/movies.yml')
timetable = Timetable.create_movies_timetable(movies_db, movie_house)
for item in timetable:
    movie_duration = item.movie.duration.seconds
    minutes, hours = movie_duration // 60 % 60, movie_duration // 3600
    print(
        f"{item.movie.movie_title} - {item.movie_hall.number}, start: "
        f"{item.start_time.strftime('%d.%m.%Y, %H:%M:%S')}, "
        f"{hours}:{minutes}"
    )
print()
