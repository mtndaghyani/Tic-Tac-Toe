from classes._Player import _Player


def check_game_state(board):
    # Checking rows
    for row in board:
        if row[0] == row[1] == row[2] != "   ":
            return row[0]
    # Checking columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != "   ":
            return board[0][column]
    # Checking diameters:
    if board[0][0] == board[1][1] == board[2][2] != "   ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "   ":
        return board[0][2]
    # Checking draw state
    for row in board:
        if any([x == "   " for x in row]):
            return None
    return "draw"


def evaluate_state(board, player, depth):
    """Evaluates the value of the current state of the board"""
    current_state = check_game_state(board)
    if current_state == player.symbol == " X ":
        return 10 - depth
    elif current_state == "draw":
        return 0
    elif current_state is None:
        return None
    else:
        return -10 + depth


def minimax(board, player1, player2, last_row=0, last_col=0, depth = 0):
    """Finds the best choice among free boxes using MINIMAX algorithm"""
    current_state = evaluate_state(board, player2, depth)
    if current_state is not None:
        return current_state, last_row, last_col
    x, y = 0, 0
    if player1.__class__ is Bot:
        score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "   ":
                    board[i][j] = f' {player1.symbol} '
                    result = minimax(board, player2, player1, i, j, depth + 1)
                    if result[0] > score:
                        score = result[0]
                        x = i
                        y = j
                    board[i][j] = "   "
        return score, x, y
    else:
        score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "   ":
                    board[i][j] = f' {player1.symbol} '
                    result = minimax(board, player2, player1, i, j, depth + 1)
                    if result[0] < score:
                        score = result[0]
                        x = i
                        y = j
                    board[i][j] = "   "
        return score, x, y


class Bot(_Player):
    def choose_box(self, board, player):
        """Find an optimal box using minimax algorithm"""
        best_move = minimax(board, self, player)
        return best_move[1], best_move[2]
