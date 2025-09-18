from enums.city import City

class Theatre:
    def __init__(self, theatre_id=None, address=None, city: City=None):
        self.theatre_id = theatre_id
        self.address = address
        self.city = city
        self.screens = []  # list of Screen
        self.shows = []    # list of Show

    def get_theatre_id(self):
        return self.theatre_id

    def set_theatre_id(self, theatre_id):
        self.theatre_id = theatre_id

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_screens(self):
        return self.screens

    def set_screens(self, screens):
        self.screens = screens

    def get_shows(self):
        return self.shows

    def set_shows(self, shows):
        self.shows = shows

    def get_city(self):
        return self.city

    def set_city(self, city: City):
        self.city = city
