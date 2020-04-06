class _Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        return self.symbol == other.symbol

