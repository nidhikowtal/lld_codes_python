from enums.seat_category import SeatCategory

class Seat:
    def __init__(self, seat_id=None, row=None, seat_category: SeatCategory=None):
        self.seat_id = seat_id
        self.row = row
        self.seat_category = seat_category

    def get_seat_id(self):
        return self.seat_id

    def set_seat_id(self, seat_id):
        self.seat_id = seat_id

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row

    def get_seat_category(self):
        return self.seat_category

    def set_seat_category(self, seat_category: SeatCategory):
        self.seat_category = seat_category
