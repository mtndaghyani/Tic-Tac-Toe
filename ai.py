from classes.Bot import Bot
from classes.Game import check_game_state
from classes.User import User


def evaluate_state(board, player):
    """Evaluates the value of the current state of the board"""
    current_state = check_game_state(board)
    if current_state == player.symbol:
        return 10
    elif current_state == "draw":
        return 0
    elif current_state is None:
        return None
    else:
        return -10


def minimax(board, player1, player2, last_row, last_col):
    """Finds the best choice among free boxes using MINIMAX algorithm"""
    current_state = evaluate_state(board, player2)
    if current_state is not None:
        return current_state, last_row, last_col
    x, y = 0, 0
    if player1.__class__ is Bot:
        score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "   ":
                    board[i][j] = player1.symbol
                    result = minimax(board, player2, player1, i, j)
                    if result[0] > score:
                        score = result[0]
                        x = result[1]
                        y = result[2]
                    board[i][j] = "   "
        return score, x, y
    else:
        score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "   ":
                    board[i][j] = player1.symbol
                    result = minimax(board, player2, player1, i, j)
                    if result[0] < score:
                        score = result[0]
                        x = result[1]
                        y = result[2]
                    board[i][j] = "   "
        return score, x, y


if __name__ == "__main__":

    print(minimax([[" O ", " X ", "   "], ["   ", " O ", "   "], ["   ", "   ", "   "]], Bot(" X "), User(" O "), 0, 0))
