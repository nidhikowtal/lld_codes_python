class Show:
    def __init__(self, show_id=None, movie=None, screen=None, show_start_time=None):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.show_start_time = show_start_time
        self.booked_seat_ids = []  # list of seat IDs

    def get_show_id(self):
        return self.show_id

    def set_show_id(self, show_id):
        self.show_id = show_id

    def get_movie(self):
        return self.movie

    def set_movie(self, movie):
        self.movie = movie

    def get_screen(self):
        return self.screen

    def set_screen(self, screen):
        self.screen = screen

    def get_show_start_time(self):
        return self.show_start_time

    def set_show_start_time(self, show_start_time):
        self.show_start_time = show_start_time

    def get_booked_seat_ids(self):
        return self.booked_seat_ids

    def set_booked_seat_ids(self, booked_seat_ids):
        self.booked_seat_ids = booked_seat_ids
