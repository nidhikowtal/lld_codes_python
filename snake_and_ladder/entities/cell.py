from entities.jump import Jump

class Cell:
    def __init__(self):
        self.jump = None  # Can be a Jump object or None

    def get_jump(self):
        return self.jump

    def set_jump(self, jump: Jump):
        self.jump = jump
