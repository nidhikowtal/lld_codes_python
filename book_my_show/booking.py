class Booking:
    def __init__(self):
        self.show = None
        self.booked_seats = []
        self.payment = None

    def get_show(self):
        return self.show

    def set_show(self, show):
        self.show = show

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, booked_seats):
        self.booked_seats = booked_seats

    def get_payment(self):
        return self.payment

    def set_payment(self, payment):
        self.payment = payment
