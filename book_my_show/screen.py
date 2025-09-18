class Screen:
    def __init__(self, screen_id=None):
        self.screen_id = screen_id
        self.seats = []

    def get_screen_id(self):
        return self.screen_id

    def set_screen_id(self, screen_id):
        self.screen_id = screen_id

    def get_seats(self):
        return self.seats

    def set_seats(self, seats):
        self.seats = seats
