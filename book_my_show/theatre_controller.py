from collections import defaultdict
from enums.city import City
from theatre import Theatre
from show import Show
from movie import Movie

class TheatreController:
    def __init__(self):
        self.city_vs_theatre = defaultdict(list)  # Map[City, List[Theatre]]
        self.all_theatre = []

    def add_theatre(self, theatre: Theatre, city: City):
        self.all_theatre.append(theatre)
        self.city_vs_theatre[city].append(theatre)

    def get_all_show(self, movie: Movie, city: City):
        """
        Return dictionary of {Theatre: [Show]} where the given movie is running in the given city
        """
        theatre_vs_shows = {}

        theatres = self.city_vs_theatre.get(city, [])

        for theatre in theatres:
            given_movie_shows = []
            for show in theatre.get_shows():
                if show.movie.get_movie_id() == movie.get_movie_id():
                    given_movie_shows.append(show)

            if given_movie_shows:
                theatre_vs_shows[theatre] = given_movie_shows

        return theatre_vs_shows
