import Functions

play_again = True
while play_again:
    matrix = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

    game_request = input(f'select option:\n'
                         f'[1]: Computer vs. Computer\n'
                         f'[2]: X vs. Computer\n'
                         f'[3]: O vs. Computer\n'
                         f'[4]: X vs. O\n')
    while game_request not in {"1", "2", "3", "4"}:
        print("I'm afraid I can't do that, Dave.")
        game_request = input(f'select option:\n'
                             f'[1]: Computer vs. Computer\n'
                             f'[2]: X vs. Computer\n'
                             f'[3]: O vs. Computer\n'
                             f'[4]: X vs. 0\n')
    if game_request == "1":
        turns = 0
        win = False
        while turns < 9 and not win:
            Functions.computer_player(matrix, "X")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("X wins!")
                win = True
                while play_again:
                    play_request = input("play again? [yes/no] ")
                    if play_request == "no":
                        quit()
                    elif play_request == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True

                break
            turns += 1
            if turns == 9:
                break

            Functions.computer_player(matrix, "O")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("0 wins!")
                win = True
                while play_again:
                    play_again = input("play again? [yes/no] ")
                    if play_again == "no":
                        quit()
                    elif play_again == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True

                break
            turns += 1
            if turns == 9:
                break

        if turns == 9 and not win:
            print("Strange Game. The only way to win...is not to play")
            while play_again:
                play_again = input("play again? [yes/no] ")
                if play_again == "no":
                    quit()
                elif play_again == 'yes':
                    break
                else:
                    print("I'm afraid I can't do that, Dave")
                    play_again = True

    if game_request == "2":
        turns = 0
        win = False
        while turns < 9:
            Functions.user_player(matrix, "X")

            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("X wins!")
                win = True
                while play_again:
                    play_request = input("play again? [yes/no] ")
                    if play_request == "no":
                        quit()
                    elif play_request == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True
                break
            turns += 1
            if turns == 9:
                break

            Functions.computer_player(matrix, "O")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("0 wins!")
                win = True
                while play_again:
                    play_again = input("play again? [yes/no] ")
                    if play_again == "no":
                        quit()
                    elif play_again == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True
                break
            turns += 1
            if turns == 9:
                break

        if turns == 9 and not win:
            print("Strange Game. The only way to win...is not to play")
            while play_again:
                play_again = input("play again? [yes/no] ")
                if play_again == "no":
                    quit()
                elif play_again == 'yes':
                    break
                else:
                    print("I'm afraid I can't do that, Dave")
                    play_again = True

    if game_request == "3":
        turns = 0
        win = False
        while turns < 9:
            Functions.computer_player(matrix, "X")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("X wins!")
                win = True
                while play_again:
                    play_request = input("play again? [yes/no] ")
                    if play_request == "no":
                        quit()
                    elif play_request == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True
                break
            turns += 1
            if turns == 9:
                break

            Functions.user_player(matrix, "O")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("0 wins!")
                win = True
                while play_again:
                    play_again = input("play again? [yes/no] ")
                    if play_again == "no":
                        quit()
                    elif play_again == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True
                break
            turns += 1
            if turns == 9:
                break

        if turns == 9 and not win:
            print("Strange Game. The only way to win...is not to play")
            while play_again:
                play_again = input("play again? [yes/no] ")
                if play_again == "no":
                    quit()
                elif play_again == 'yes':
                    break
                else:
                    print("I'm afraid I can't do that, Dave")
                    play_again = True

    if game_request == "4":
        turns = 0
        win = False
        while turns < 9:
            Functions.user_player(matrix, "X")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("X wins!")
                win = True
                while play_again:
                    play_request = input("play again? [yes/no] ")
                    if play_request == "no":
                        quit()
                    elif play_request == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True
                break
            turns += 1
            if turns == 9:
                break

            Functions.user_player(matrix, "O")
            Functions.grid_generator(matrix)
            if Functions.win_condition(matrix) or Functions.diagonal_win_condition(matrix):
                print("0 wins!")
                win = True
                while play_again:
                    play_again = input("play again? [yes/no] ")
                    if play_again == "no":
                        quit()
                    elif play_again == 'yes':
                        break
                    else:
                        print("I'm afraid I can't do that, Dave")
                        play_again = True
                break
            turns += 1
            if turns == 9:
                break

        if turns == 9 and not win:
            print("Strange Game. The only way to win...is not to play")
            while play_again:
                play_again = input("play again? [yes/no] ")
                if play_again == "no":
                    quit()
                elif play_again == 'yes':
                    break
                else:
                    print("I'm afraid I can't do that, Dave")
                    play_again = True
