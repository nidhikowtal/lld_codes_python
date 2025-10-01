class Movie:
    def __init__(self, movie_id, name):
        self.movie_id = movie_id
        self.name = name


class Theater:
    def __init__(self, theater_id, name, total_seats):
        self.theater_id = theater_id
        self.name = name
        self.total_seats = total_seats


class Show:
    def __init__(self, show_id, movie, theater, start_time, end_time):
        self.show_id = show_id
        self.movie = movie
        self.theater = theater
        self.start_time = start_time
        self.end_time = end_time
        self.booked_seats = set()  # keeps track of booked seats

    def view_available_seats(self):
        available_seats = []  # list to store unbooked seats

        # iterate over all seat numbers from 1 to total_seats
        for i in range(1, self.theater.total_seats + 1):
            if i not in self.booked_seats:
                available_seats.append(i)

        return available_seats

    def book_seats(self, seat_ids):
        # check if any seat already booked
        for seat in seat_ids:
            if seat in self.booked_seats:
                raise Exception(f"Seat {seat} is already booked!")
        # otherwise add them to booked seats
        for seat in seat_ids:
            self.booked_seats.add(seat)


class Booking:
    def __init__(self, booking_id, user_id, show, seat_ids):
        self.booking_id = booking_id
        self.user_id = user_id
        self.show = show
        self.seat_ids = seat_ids


class BookingSystem:
    def __init__(self):
        self.movies = {}    # movie_id -> Movie
        self.theaters = {}  # theater_id -> Theater
        self.shows = {}     # show_id -> Show
        self.bookings = {}  # booking_id -> Booking

    # -------- APIs ----------
    def add_movie(self, movie_id, name):
        movie = Movie(movie_id, name)
        self.movies[movie_id] = movie
        return movie

    def add_theater(self, theater_id, name, total_seats):
        theater = Theater(theater_id, name, total_seats)
        self.theaters[theater_id] = theater
        return theater

    def create_show(self, show_id, movie_id, theater_id, start_time, end_time):
        movie = self.movies[movie_id]
        theater = self.theaters[theater_id]
        show = Show(show_id, movie, theater, start_time, end_time)
        self.shows[show_id] = show
        return show

    def view_available_seats(self, show_id):
        return self.shows[show_id].view_available_seats()

    def book_seats(self, booking_id, user_id, show_id, seat_ids):
        show = self.shows[show_id]
        show.book_seats(seat_ids)
        booking = Booking(booking_id, user_id, show, seat_ids)
        self.bookings[booking_id] = booking
        return booking

    def cancel_booking(self, booking_id):
        booking = self.bookings.get(booking_id)
        if not booking:
            return False
        for seat in booking.seat_ids:
            booking.show.booked_seats.remove(seat)
        del self.bookings[booking_id]
        return True


# ----------------- Demo Flow -----------------
if __name__ == "__main__":
    system = BookingSystem()

    movie = system.add_movie("M1", "Inception")  # {movie_id, name}

    theater = system.add_theater("T1", "PVR", 10)  # {theater_id, name, total_seats}

    show = system.create_show("S1", "M1", "T1", "7:00 PM", "10:00 PM")  # {show_id, movie_id, theater_id, start_time, end_time}

    print("Available seats:", system.view_available_seats("S1"))

    # 5. User1 books seats [2,3]
    booking1 = system.book_seats("B1", "U1", "S1", [2, 3])  # {booking_id, user_id, show_id, seat_ids}
    print("User1 booked:", booking1.seat_ids)

    # 6. User2 tries to book [3,4] (fails for 3)
    try:
        booking2 = system.book_seats("B2", "U2", "S1", [3, 4])  # {booking_id, user_id, show_id, seat_ids}
        print("User2 booked:", booking2.seat_ids)
    except Exception as e:
        print("User2 booking failed:", e)

    system.cancel_booking("B1")  
    print("After cancellation, available:", system.view_available_seats("S1"))
