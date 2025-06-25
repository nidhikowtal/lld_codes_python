from collections import deque
from entities.board import Board
from services.dice import Dice
from entities.player import Player

class Game:
    def __init__(self):
        self.board = None
        self.dice = None
        self.players_list = deque()
        self.winner = None
        self.initialize_game()

    def initialize_game(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self.add_players()

    def add_players(self):
        player1 = Player("p1", 0)
        player2 = Player("p2", 0)
        self.players_list.append(player1)
        self.players_list.append(player2)

    def start_game(self):
        # Main game loop runs until a player wins
        while self.winner is None:
            # Get the player whose turn it is
            player_turn = self.find_player_turn()
            print(f"player turn is: {player_turn.id} current position is: {player_turn.current_position}")

            # Roll the dice
            dice_number = self.dice.roll_dice()

            # Calculate tentative new position
            player_new_position = player_turn.current_position + dice_number

            # Check for any snake or ladder at the new position
            player_new_position = self.jump_check(player_new_position)

            # Update player's position
            player_turn.current_position = player_new_position

            print(f"player turn is: {player_turn.id} new position is: {player_new_position}")

            # Check if the player has reached or crossed the last cell
            if player_new_position >= self.board.cells.__len__() * self.board.cells.__len__() - 1:
                self.winner = player_turn

        print(f"WINNER IS: {self.winner.id}")

    def find_player_turn(self):
        # Rotate the player queue: remove first, re-add to end
        player_turn = self.players_list.popleft()
        self.players_list.append(player_turn)
        return player_turn

    def jump_check(self, player_new_position):
        board_limit = len(self.board.cells) * len(self.board.cells)

        # If position exceeds board limit, ignore and stay put
        if player_new_position > board_limit - 1:
            return player_new_position

        # Check if the cell has a jump (snake or ladder)
        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jump_by = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print(f"jump done by: {jump_by}")
            return cell.jump.end

        # No jump, return original position
        return player_new_position
