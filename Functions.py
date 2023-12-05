import random


def same_list(test_list):
    for item in test_list:
        if not test_list[0] == test_list[1] == test_list[2]:
            return False
        elif item == test_list[0] == "-":
            return False
        else:
            pass
    return True


def win_condition(matrix):
    i = 0
    while i <= 2:
        temp_list = [column[i] for column in matrix]
        temp_list_2 = matrix[i]
        if same_list(temp_list) or same_list(temp_list_2):
            return True
        else:
            i += 1
    return False


def diagonal_win_condition(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != "-":
        return True
    elif matrix[0][2] == matrix[1][1] == matrix[2][0] != "-":
        return True
    else:
        return False


def grid_generator(matrix):
    output_string_1 = ""
    output_string_2 = ""
    output_string_3 = ""
    for item in matrix[0]:
        output_string_1 += " " + item
    for item in matrix[1]:
        output_string_2 += " " + item
    for item in matrix[2]:
        output_string_3 += " " + item
    print(f'{output_string_1} \n'
          f'{output_string_2} \n'
          f'{output_string_3}\n')


def check_for_opponent_win(matrix, side):
    if side == "O":
        opp_side = "X"
    else:
        opp_side = "O"
    check_box = matrix.copy()
    for row in range(len(check_box)):
        for column in range(len(check_box)):
            if check_box[row][column] != "X" and check_box[row][column] != "O":
                check_box[row][column] = opp_side
                if win_condition(check_box) or diagonal_win_condition(check_box):
                    print("I will stop you")
                    matrix[row][column] = side
                    return row, column
                else:
                    check_box[row][column] = "-"
    return False


def check_for_self_win(matrix, side):
    check_box = matrix.copy()
    for row in range(len(check_box)):
        for column in range(len(check_box)):
            if check_box[row][column] != "X" and check_box[row][column] != "O":
                check_box[row][column] = side
                if win_condition(check_box) or diagonal_win_condition(check_box):
                    print("Victory is Mine!")
                    matrix[row][column] = side
                    return row, column
                else:
                    check_box[row][column] = "-"
    return False


def computer_player(matrix, side):
    try:
        x, y = check_for_self_win(matrix, side)
        matrix[x][y] = side
    except TypeError:
        try:
            x, y = check_for_opponent_win(matrix, side)
            matrix[x][y] = side
        except TypeError:
            r = random.randint(0, 2)
            rr = random.randint(0, 2)
            while matrix[r][rr] in {"X", "O"}:
                r = random.randint(0, 2)
                rr = random.randint(0, 2)
            matrix[r][rr] = side


def user_player(matrix, side):
    user_input = input("enter coordinates, e.g. 01 or 21: ")
    x, y = user_input
    while matrix[int(x)][int(y)] in {"X", "O"}:
        print("That spot is taken. No stealing!")
        user_input = input("enter coordinates, e.g. 01 or 21: ")
        x, y = user_input
    else:
        matrix[int(x)][int(y)] = side
