from classes._Player import _Player


class User(_Player):
    @staticmethod
    def check_input(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    def choose_box(self):
        x = -1
        y = -1
        while not self.check_input(x, y):
            x, y = map(lambda i: int(i), input("Choose a box: ").split())
        return x, y


if __name__ == "__main__":
    user = User("o")
    print(user.choose_box())
