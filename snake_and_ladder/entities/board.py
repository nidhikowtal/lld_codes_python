import random
from entities.cell import Cell
from entities.jump import Jump

class Board:
    def __init__(self, board_size, number_of_snakes, number_of_ladders):
        self.cells = []
        self.initialize_cells(board_size)

        self.add_snakes_ladders(number_of_snakes, number_of_ladders)

    def initialize_cells(self, board_size):
        self.cells = [[Cell() for _ in range(board_size)] for _ in range(board_size)]

    def add_snakes_ladders(self, number_of_snakes, number_of_ladders):
        board_size = len(self.cells)
        total_cells = board_size * board_size

        # Add snakes randomly on the board
        while number_of_snakes > 0:
            snake_head = random.randint(1, total_cells - 1)
            snake_tail = random.randint(1, total_cells - 1)

            # Snake must go down, so head should be greater than tail
            if snake_tail >= snake_head:
                continue

            # Create a snake jump and attach it to the head cell
            snake_obj = Jump()
            snake_obj.start = snake_head
            snake_obj.end = snake_tail

            cell = self.get_cell(snake_head)
            cell.jump = snake_obj

            number_of_snakes -= 1

        # Add ladders randomly on the board
        while number_of_ladders > 0:
            ladder_start = random.randint(1, total_cells - 1)
            ladder_end = random.randint(1, total_cells - 1)

            # Ladder must go up, so start should be less than end
            if ladder_start >= ladder_end:
                continue

            # Create a ladder jump and attach it to the starting cell
            ladder_obj = Jump()
            ladder_obj.start = ladder_start
            ladder_obj.end = ladder_end

            cell = self.get_cell(ladder_start)
            cell.jump = ladder_obj

            number_of_ladders -= 1

    def get_cell(self, player_position):
        # Convert linear position to 2D board coordinates and return the cell
        board_row = player_position // len(self.cells)
        board_column = player_position % len(self.cells)
        return self.cells[board_row][board_column]
