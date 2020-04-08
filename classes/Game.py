from classes.Board import Board
from classes.Bot import Bot, check_game_state
from classes.User import User


def _play_game(players, board):
    while True:
        for player in players:
            x, y = player.choose_box(board=board.board, player=player)
            board.mark_box(player, x, y)
            print(board, end="\n" * 3)
            status = check_game_state(board.board)
            if status is not None:
                return status


def _get_game_result(status, players):
    if status == "draw":
        print("DRAW")
    elif status == f' {players[0].symbol} ':
        print("THAT'S GREAT!! YOU WON ;)")
    else:
        print("YOU LOST :(")


def run():
    while True:
        player_symbol = input("Choose your symbol: X/O ?")
        if player_symbol == "O" or player_symbol == "X":
            print("Let's start!!")
            print("=" * 20)
            break
        print("Oops! Wrong input!! Try again")
    if player_symbol == "X":
        bot_symbol = "O"
    else:
        bot_symbol = "X"
    user = User(player_symbol)
    bot = Bot(bot_symbol)
    players = [user, bot]
    board = Board()
    _get_game_result(_play_game(players, board), players)
