class Player:
    def __init__(self, player_id, current_position):
        self.id = player_id
        self.current_position = current_position

    def get_id(self):
        return self.id

    def set_id(self, player_id):
        self.id = player_id

    def get_current_position(self):
        return self.current_position

    def set_current_position(self, position):
        self.current_position = position
