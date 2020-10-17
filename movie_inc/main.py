from movie_house import MovieHouse
from tools.yaml_loader import load_yaml

# movie_hall_schema = load_yaml('../data/cronverk.yml')
movie_hall_schema = MovieHouse.create_movie_house(load_yaml, '../data/cronverk.yml')
print()