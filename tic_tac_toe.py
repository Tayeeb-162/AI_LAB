import math

board = []

for i in range(3):
    board.append(input().split())

computer = input().upper()

if computer == "X":
    human = "O"
else:
    human = "X"

MAX = computer
MIN = human


def terminal_test(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            return True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return True

    for row in board:
        if "_" in row:
            return False

    return True


def utility(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == MAX:
                return 1
            if board[i][0] == MIN:
                return -1

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == MAX:
                return 1
            if board[0][i] == MIN:
                return -1

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == MAX:
            return 1
        if board[0][0] == MIN:
            return -1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == MAX:
            return 1
        if board[0][2] == MIN:
            return -1

    return 0


def actions(board):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                moves.append((i, j))

    return moves


def result(board, action, player):
    new_board = [row[:] for row in board]
    i, j = action
    new_board[i][j] = player
    return new_board


def max_value(board):
    if terminal_test(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action, MAX)))

    return v


def min_value(board):
    if terminal_test(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action, MIN)))

    return v


def minimax_decision(board):
    best_action = None
    best_value = -math.inf

    for action in actions(board):
        value = min_value(result(board, action, MAX))

        if value > best_value:
            best_value = value
            best_action = action

    return best_action


def print_board(board):
    for row in board:
        print(" ".join(row))


move = minimax_decision(board)

if move is not None:
    row, col = move
    board[row][col] = computer

    print("Computer places", computer, "in position", (row + 1, col + 1))

print_board(board)

score = utility(board)

if score == 1:
    print("Computer Wins")
elif score == -1:
    print("Human Wins")
else:
    if len(actions(board)) == 0:
        print("Game Draw")
    else:
        if computer == "O":
            print("Human's winning move is blocked.")
        else:
            print("Human's winning move is blocked.")
