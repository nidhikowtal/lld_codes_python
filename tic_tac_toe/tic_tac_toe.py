# ----------------- Models -----------------

class Player:
    def __init__(self, name, piece_type):
        self.name = name
        self.piece_type = piece_type  # 'X' or 'O'


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
                    row_display.append(self.board[i][j])
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
                while not valid_move:  # keep asking until a valid move
                    self.board.print_board()

                    free_cells = self.board.get_free_cells()
                    if not free_cells:
                        print("Game ended in a tie!")
                        return

                    try:
                        move = input(f"{player.name} ({player.piece_type}), enter row,column: ")
                        if move.lower() in ["exit", "q"]:
                            print("Game exited by user.")
                            return
                        row, col = map(int, move.strip().split(","))
                    except:
                        print("Invalid input, enter row,column like '0,2'.")
                        continue

                    if not self.board.add_piece(row, col, player.piece_type):
                        print("Cell already occupied, choose another cell.")
                        continue

                    valid_move = True  # valid move made

                    if self.is_winner(row, col, player.piece_type):
                        self.board.print_board()
                        self.winner = player
                        print(f"🏆 Winner is {player.name}")
                        return
                    
    def is_winner(self, row, col, piece_type):
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

# Create board and players before the game
board = Board(size=3)
players = [Player("P1", "X"), Player("P2", "O")]

# Initialize game
game = TicTacToeGame(board, players)

# Start game
game.play()
