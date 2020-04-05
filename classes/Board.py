from classes.User import User


class Board:
    """
    Manipulating the game board.
    """

    def __init__(self):
        self.board = [["   " for i in range(3)] for j in range(3)]

    def mark_box(self, player, x, y):
        self.board[x][y] = f' {player.symbol} '

    def __str__(self):
        result = []
        for i in self.board:
            result.append("|".join(i))
        return str(("\n" + "----" * 3 + "\n").join(result))


if __name__ == "__main__":
    board = Board()
    user = User("o")
    i, j = user.choose_box()
    board.mark_box(user, i, j)
    print(board)
