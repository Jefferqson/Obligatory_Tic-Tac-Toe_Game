import Functions
import random

matrix = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]

turns = 0
win = False
while turns < 9:
    user_input = input("enter coordinates, e.g. 01 or 21: ")
    x, y = user_input
    while matrix[int(x)][int(y)] in {"X", "O"}:
        print("That spot is taken. No stealing!")
        user_input = input("enter coordinates, e.g. 01 or 21: ")
        x, y = user_input
    else:
        matrix[int(x)][int(y)] = "X"

    if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
        print("X wins!")
        win = True
        break
    turns += 1
    if turns == 9:
        break
    Functions.grid_generator(matrix)

    try:
        x, y = Functions.check_for_self_win_O(matrix)
    except TypeError:
        try:
            x, y = Functions.check_for_opponent_win_o(matrix)
        except TypeError:
            r = random.randint(0, 2)
            rr = random.randint(0, 2)
            while matrix[r][rr] in {"X", "O"}:
                r = random.randint(0, 2)
                rr = random.randint(0, 2)
            matrix[r][rr] = "O"
        else:
            matrix[x][y] = "O"

    if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
        win = True
        print("O wins!")
        break
    turns += 1
    Functions.grid_generator(matrix)

if turns == 9 and not win:
    print("Strange Game. The only way to win...is not to play")
Functions.grid_generator(matrix)
