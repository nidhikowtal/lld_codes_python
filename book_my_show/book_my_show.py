import logging

from movie import Movie
from booking import Booking
from movie_controller import MovieController
from theatre_controller import TheatreController
from theatre import Theatre
from screen import Screen
from seat import Seat
from show import Show
from enums.city import City
from enums.seat_category import SeatCategory


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class BookMyShow:
    def __init__(self):
        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()

    def initialize(self):
        logging.info("Initializing BookMyShow system...")
        self.create_movies()
        self.create_theatres()
        logging.info("Initialization complete ✅")

    def create_movies(self):
        logging.info("Creating movies...")

        avengers = Movie(1, "AVENGERS", 128)
        baahubali = Movie(2, "BAAHUBALI", 180)

        self.movie_controller.add_movie(avengers, City.Bangalore)
        self.movie_controller.add_movie(avengers, City.Delhi)
        self.movie_controller.add_movie(baahubali, City.Bangalore)
        self.movie_controller.add_movie(baahubali, City.Delhi)

        logging.info("Movies created and added to cities")

    def create_theatres(self):
        logging.info("Creating theatres and assigning shows...")

        avenger_movie = self.movie_controller.get_movie_by_name("AVENGERS")
        baahubali_movie = self.movie_controller.get_movie_by_name("BAAHUBALI")

        # Theatre 1 - Bangalore
        inox = Theatre(1, "MG Road", City.Bangalore)
        inox_screens = [self.create_screen(1)]
        inox.set_screens(inox_screens)

        inox_shows = [
            self.create_show(1, inox_screens[0], avenger_movie, 8),
            self.create_show(2, inox_screens[0], baahubali_movie, 16)
        ]
        inox.set_shows(inox_shows)
        self.theatre_controller.add_theatre(inox, City.Bangalore)

        # Theatre 2 - Delhi
        pvr = Theatre(2, "CP", City.Delhi)
        pvr_screens = [self.create_screen(2)]
        pvr.set_screens(pvr_screens)

        pvr_shows = [
            self.create_show(3, pvr_screens[0], avenger_movie, 13),
            self.create_show(4, pvr_screens[0], baahubali_movie, 20)
        ]
        pvr.set_shows(pvr_shows)
        self.theatre_controller.add_theatre(pvr, City.Delhi)

        logging.info("Theatres and shows successfully created")

    def create_screen(self, screen_id):
        screen = Screen(screen_id)
        screen.set_seats(self.create_seats())
        return screen

    def create_seats(self):
        seats = []
        for i in range(0, 40):
            seats.append(Seat(i, row=None, seat_category=SeatCategory.SILVER))
        for i in range(40, 70):
            seats.append(Seat(i, row=None, seat_category=SeatCategory.GOLD))
        for i in range(70, 100):
            seats.append(Seat(i, row=None, seat_category=SeatCategory.PLATINUM))
        return seats

    def create_show(self, show_id, screen, movie, show_start_time):
        return Show(show_id, movie, screen, show_start_time)

    def create_booking(self, city, movie_name):
        logging.info(f"Attempting booking for movie '{movie_name}' in {city.name}...")

        # Step 1: Find movies in the city
        movies = self.movie_controller.get_movies_by_city(city)
        if not movies:
            logging.warning(f"No movies available in {city.name}")
            return

        interested_movie = None
        for movie in movies:
            if movie.get_movie_name() == movie_name:
                interested_movie = movie
                break

        if not interested_movie:
            logging.warning(f"Movie '{movie_name}' not found in {city.name}")
            return

        # Step 2: Get all shows for that movie
        shows_theatre_wise = self.theatre_controller.get_all_show(interested_movie, city)

        if not shows_theatre_wise:
            logging.warning(f"No shows found for '{movie_name}' in {city.name}")
            return

        # Step 3: Pick first show for simplicity
        theatre, running_shows = next(iter(shows_theatre_wise.items()))
        interested_show = running_shows[0]

        logging.info(f"Found show {interested_show.get_show_id()} at Theatre {theatre.get_theatre_id()} ({theatre.get_address()})")


        # Step 4: Pick a seat
        seat_number = 30
        if seat_number in interested_show.get_booked_seat_ids():
            logging.error(f"Seat {seat_number} already booked! ❌")
            return
        else:
            interested_show.get_booked_seat_ids().append(seat_number)

        # Step 5: Confirm booking
        booking = Booking()
        my_booked_seats = [seat for seat in interested_show.get_screen().get_seats() if seat.get_seat_id() == seat_number]

        booking.set_booked_seats(my_booked_seats)
        booking.set_show(interested_show)

        logging.info(f"Booking successful 🎉 -> Seat {seat_number} booked for movie '{movie_name}'")


if __name__ == "__main__":
    bms = BookMyShow()
    bms.initialize()

    # User1 booking
    bms.create_booking(City.Bangalore, "BAAHUBALI")

    # User2 booking same seat -> should fail
    bms.create_booking(City.Bangalore, "BAAHUBALI")
