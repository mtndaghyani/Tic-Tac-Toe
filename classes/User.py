from classes._Player import _Player


class User(_Player):
    @staticmethod
    def check_input(x, y, board):
        """Checks if the user's input is in correct form"""
        return 0 <= x < 3 and 0 <= y < 3 and board[x][y] == "   "

    def choose_box(self, board, **kwargs):
        x = -1
        y = -1
        while not self.check_input(x, y, board):
            try:
                x, y = map(lambda i: int(i), input("Choose a box: ").split())
            except ValueError:
                print("Invalid input")

        return x, y

