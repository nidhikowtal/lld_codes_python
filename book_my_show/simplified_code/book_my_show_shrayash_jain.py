from enum import Enum
import logging

# ---------------- Enums ----------------
class City(Enum):
    BANGALORE = "Bangalore"
    DELHI = "Delhi"

class SeatCategory(Enum):
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

# ---------------- Entities ----------------
class Movie:
    def __init__(self, movie_id, name, duration):
        self.movie_id = movie_id
        self.name = name
        self.duration = duration

class Seat:
    def __init__(self, seat_id, category: SeatCategory):
        self.seat_id = seat_id
        self.category = category

class Screen:
    def __init__(self, screen_id, seats):
        self.screen_id = screen_id
        self.seats = seats

class Show:
    def __init__(self, show_id, movie: Movie, screen: Screen, start_time: int):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.start_time = start_time
        self.booked_seats = set()

    def book_seat(self, seat_id):
        if seat_id in self.booked_seats:
            return False
        self.booked_seats.add(seat_id)
        return True

class Theatre:
    def __init__(self, theatre_id, city: City, screens, shows):
        self.theatre_id = theatre_id
        self.city = city
        self.screens = screens
        self.shows = shows

class Booking:
    def __init__(self, show: Show, seats):
        self.show = show
        self.seats = seats

# ---------------- Controllers ----------------
class MovieController:
    def __init__(self):
        self.city_movies = {}

    def add_movie(self, movie: Movie, city: City):
        # if city not in dict, initialize with empty list
        if city not in self.city_movies:
            self.city_movies[city] = []

        self.city_movies[city].append(movie)

    def get_movies_by_city(self, city: City):
        if city in self.city_movies:
            return self.city_movies[city]
        else:
            return []   # return empty list if city not found


class TheatreController:
    def __init__(self):
        self.city_theatres = {}

    def add_theatre(self, theatre: Theatre, city: City):
        # if city not in dict, initialize with empty list
        if city not in self.city_theatres:
            self.city_theatres[city] = []

        # now safely append theatre
        self.city_theatres[city].append(theatre)

    def get_shows(self, movie: Movie, city: City):
        shows = []

        # check if city exists
        if city in self.city_theatres:
            theatres = self.city_theatres[city]

            # loop through theatres in that city
            for theatre in theatres:
                for show in theatre.shows:
                    if show.movie.movie_id == movie.movie_id:
                        shows.append(show)

        return shows


# ---------------- Orchestrator ----------------
class BookMyShow:
    def __init__(self):
        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()
        self._initialize()

    def _initialize(self):
        # Movies
        avengers = Movie(1, "AVENGERS", 128)    # {movie_id, name, duration}
        baahubali = Movie(2, "BAAHUBALI", 180)

        self.movie_controller.add_movie(avengers, City.BANGALORE)  # {movie obj, city}
        self.movie_controller.add_movie(baahubali, City.BANGALORE)

        # Seats
        seats = []

        for i in range(1, 101):  # 100 seats
            if i < 40:
                category = SeatCategory.SILVER
            elif i < 70:
                category = SeatCategory.GOLD
            else:
                category = SeatCategory.PLATINUM

            seat = Seat(i, category)
            seats.append(seat)

        screen1 = Screen(1, seats)    # {screeen_id, seats}

        # Shows
        show1 = Show(1, avengers, screen1, 10)    # {show_id, movie, screen, start_time}
        show2 = Show(2, baahubali, screen1, 14)

        # Theatre
        theatre1 = Theatre(1, City.BANGALORE, [screen1], [show1, show2])   # {theatre_id, city, screens, shows}
        self.theatre_controller.add_theatre(theatre1, City.BANGALORE)

    def create_booking(self, city: City, movie_name: str, seat_id: int):
        # Step 1: Find movie
        movies = self.movie_controller.get_movies_by_city(city)
        movie = None
        for m in movies:
            if m.name == movie_name:
                movie = m
                break

        if not movie:
            logging.info("Movie not found")
            return None

        # Step 2: Find shows
        shows = self.theatre_controller.get_shows(movie, city)
        if not shows:
            logging.info("No shows available")
            return None

        # Step 3: Pick first show
        show = shows[0]
        logging.info(f"Found show {show.show_id} for movie {movie.name} at {show.start_time}hrs")

        # Step 4: Try booking
        if show.book_seat(seat_id):
            booking = Booking(show, [seat_id])
            logging.info(f"Booking successful for seat {seat_id}")
            return booking
        else:
            logging.info("Seat already booked")
            return None

# ---------------- Run Example ----------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    app = BookMyShow()
    app.create_booking(City.BANGALORE, "BAAHUBALI", 30)
    app.create_booking(City.BANGALORE, "BAAHUBALI", 30)  # duplicate booking
