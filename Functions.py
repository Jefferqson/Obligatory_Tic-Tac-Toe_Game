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


def check_for_opponent_win_x(matrix):
    check_box = matrix.copy()
    for row in range(len(check_box)):
        for column in range(len(check_box)):
            if check_box[row][column] != "X" and check_box[row][column] != "O":
                check_box[row][column] = "O"
                if win_condition(check_box) or diagonal_win_condition(check_box):
                    print("I will stop you")
                    matrix[row][column] = "X"
                    return row, column
                else:
                    check_box[row][column] = "-"
    return False


def check_for_opponent_win_o(matrix):
    check_box = matrix.copy()
    for row in range(len(check_box)):
        for column in range(len(check_box)):
            if check_box[row][column] != "X" and check_box[row][column] != "O":
                check_box[row][column] = "X"
                if win_condition(check_box) or diagonal_win_condition(check_box):
                    print("I will stop you")
                    matrix[row][column] = "O"
                    return row, column
                else:
                    check_box[row][column] = "-"
    return False


def check_for_self_win_O(matrix):
    check_box = matrix.copy()
    for row in range(len(check_box)):
        for column in range(len(check_box)):
            if check_box[row][column] != "X" and check_box[row][column] != "O":
                check_box[row][column] = "O"
                if win_condition(check_box) or diagonal_win_condition(check_box):
                    print("Victory is Mine!")
                    matrix[row][column] = "O"
                    return row, column
                else:
                    check_box[row][column] = "-"
    return False

def check_for_self_win_X(matrix):
    check_box = matrix.copy()
    for row in range(len(check_box)):
        for column in range(len(check_box)):
            if check_box[row][column] != "X" and check_box[row][column] != "O":
                check_box[row][column] = "X"
                if win_condition(check_box) or diagonal_win_condition(check_box):
                    print("Victory is Mine!")
                    matrix[row][column] = "X"
                    return row, column
                else:
                    check_box[row][column] = "-"
    return False