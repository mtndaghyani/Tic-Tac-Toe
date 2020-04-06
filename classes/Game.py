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
