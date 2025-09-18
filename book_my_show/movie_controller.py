from collections import defaultdict
from movie import Movie
from enums.city import City

class MovieController:
    def __init__(self):
        self.city_vs_movies = defaultdict(list)  # Map[City, List[Movie]]
        self.all_movies = []

    def add_movie(self, movie: Movie, city: City):
        self.all_movies.append(movie)
        self.city_vs_movies[city].append(movie)

    def get_movie_by_name(self, movie_name: str):
        for movie in self.all_movies:
            if movie.get_movie_name() == movie_name:
                return movie
        return None

    def get_movies_by_city(self, city: City):
        return self.city_vs_movies.get(city, [])
