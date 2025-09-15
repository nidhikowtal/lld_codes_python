import random

class Dice:
    def roll(self):
        return random.randint(1, 6)


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0  # all players start at position 0 (off the board)


class Board:
    def __init__(self, size, snakes, ladders):
        self.size = size              # total number of cells (e.g., 30)
        self.snakes = snakes          # dictionary: snake head -> tail
        self.ladders = ladders        # dictionary: ladder start -> end

    def get_new_position(self, pos):
        """
        Check if the new position has a snake or a ladder.
        - If it's a snake head: move player down to snake's tail.
        - If it's a ladder start: move player up to ladder's end.
        - Otherwise: return the same position.
        """
        if pos in self.snakes:
            print(f"Oops! Snake at {pos}, go down to {self.snakes[pos]}")
            return self.snakes[pos]
        elif pos in self.ladders:
            print(f"Yay! Ladder at {pos}, climb up to {self.ladders[pos]}")
            return self.ladders[pos]
        return pos


class Game:
    def __init__(self):
        # Hardcoding some snakes and ladders
        snakes = {17: 4, 19: 7, 21: 9, 27: 1}
        ladders = {3: 22, 5: 8, 11: 26, 20: 29}

        # Create board of size 30 (positions from 0 to 30)
        self.board = Board(30, snakes, ladders)

        # One dice for the game
        self.dice = Dice()

        # Two players hardcoded
        self.players = [Player("P1"), Player("P2")]

        # Initially, no winner
        self.winner = None

    def play(self):
        """
        Main game loop:
        - Players take turns rolling the dice.
        - Their positions are updated according to snakes/ladders.
        - First player to reach the last cell (size) wins.
        """
        while not self.winner:
            # Each player takes turn in sequence
            for player in self.players:
                # Roll the dice
                roll = self.dice.roll()
                print(f"{player.name} rolled a {roll}")

                # Tentative new position
                new_pos = player.position + roll

                # If roll exceeds board size, player stays in place
                if new_pos > self.board.size:
                    new_pos = player.position
                else:
                    # Otherwise check for snake or ladder
                    new_pos = self.board.get_new_position(new_pos)

                # Update player's position
                player.position = new_pos
                print(f"{player.name} is now at {player.position}\n")

                # Check win condition
                if player.position == self.board.size:
                    self.winner = player
                    break  # stop loop once we have a winner

        print(f"🏆 Winner is {self.winner.name}")


if __name__ == "__main__":
    game = Game()
    game.play()
