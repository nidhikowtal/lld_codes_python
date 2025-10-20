from enum import Enum

# ----------------- Enums -----------------

class PieceType(Enum):
    X = "X"
    O = "O"


# ----------------- Models -----------------

class Player:
    def __init__(self, name, piece_type: PieceType):
        self.name = name
        self.piece_type = piece_type  # PieceType Enum

    def __str__(self):
        return f"{self.name} ({self.piece_type.value})"


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row, col, piece_type):
        if self.board[row][col] is not None:
            return False
        self.board[row][col] = piece_type
        return True

    def get_free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append((i, j))
        return free_cells

    def print_board(self):
        for i in range(self.size):
            row_display = []
            for j in range(self.size):
                if self.board[i][j]:
                    row_display.append(self.board[i][j].value)  # 👈 Enum value
                else:
                    row_display.append(" ")
            print(" | ".join(row_display))
            if i != self.size - 1:
                print("-" * (self.size * 4 - 3))
        print()


# ----------------- Game Logic -----------------

class TicTacToeGame:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.winner = None

    def play(self):
        while not self.winner:
            for player in self.players:
                valid_move = False
                while not valid_move:
                    self.board.print_board()

                    free_cells = self.board.get_free_cells()
                    if not free_cells:
                        print("Game ended in a tie!")
                        return

                    try:
                        move = input(f"{player} enter row,column: ")
                        if move.lower() in ["exit", "q"]:
                            print("Game exited by user.")
                            return
                        row, col = map(int, move.strip().split(","))
                    except:
                        print("Invalid input, enter row,column like '0,2'.")
                        continue

                    if not (0 <= row < self.board.size and 0 <= col < self.board.size):
                        print("Move out of bounds! Try again.")
                        continue

                    if not self.board.add_piece(row, col, player.piece_type):
                        print("Cell already occupied, choose another cell.")
                        continue

                    valid_move = True

                    if self.is_winner(row, col, player.piece_type):
                        self.board.print_board()
                        self.winner = player
                        print(f"🏆 Winner is {player.name} ({player.piece_type.value})")
                        return

    def is_winner(self, row, col, piece_type: PieceType):
        size = self.board.size

        # Check row
        if all(self.board.board[row][i] == piece_type for i in range(size)):
            return True

        # Check column
        if all(self.board.board[i][col] == piece_type for i in range(size)):
            return True

        # Check main diagonal
        if row == col:
            if all(self.board.board[i][i] == piece_type for i in range(size)):
                return True

        # Check anti-diagonal
        if row + col == size - 1:
            if all(self.board.board[i][size - 1 - i] == piece_type for i in range(size)):
                return True

        return False


# ------------------- Example Static Input -------------------

board = Board(size=3)
players = [
    Player("P1", PieceType.X),
    Player("P2", PieceType.O)
]

game = TicTacToeGame(board, players)
game.play()
