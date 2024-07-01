print(r'''
.___________. __    ______    .___________.    ___       ______    .___________.  ______    _______
|           ||  |  /      |   |           |   /   \     /      |   |           | /  __  \  |   ____|
`---|  |----`|  | |  ,----'   `---|  |----`  /  ^  \   |  ,----'   `---|  |----`|  |  |  | |  |__
    |  |     |  | |  |            |  |      /  /_\  \  |  |            |  |     |  |  |  | |   __|
    |  |     |  | |  `----.       |  |     /  _____  \ |  `----.       |  |     |  `--'  | |  |____
    |__|     |__|  \______|       |__|    /__/     \__\ \______|       |__|      \______/  |_______|

''')

# Create a function that asks the player if they want to continue playing the game.
def play_again():

    while True:
        user_input = input('\n\nWould you like to play again?')
        if user_input == 'yes':
            tic_tac_toe()
        elif user_input == 'no':
            print('\n\nThank you for playing! Goodbye.')
            exit()
        else:
            print('Please type "yes" or "no".')

# Create a two player tic-tac-toe game function.
def tic_tac_toe():
    # Create and display tic-tac-toe board.
    game_on = True
    orig_board = ['\n', '|_1_|', '|_2_|', '|_3_|\n', '|_4_|', '|_5_|', '|_6_|\n', '|_7_|', '|_8_|', '|_9_|']

    for x in orig_board:
        print(x, end='')

    while game_on:
        player_1 = True
        player_2 = True

        #Create Player 1 and ask for input.
        while player_1:
            try:
                player_1_input = int(input(f'\n\nPlayer_1, where would you like to place your X?: '))

                #Depending on the input of Player 1, their input will be denied or accepted.
                while orig_board[player_1_input] == '|_X_|' or orig_board[player_1_input] == '|_X_|\n' or orig_board[
                        player_1_input] == '|_O_|' or orig_board[player_1_input] == '|_O_\n|':
                    player_1_input = int(input('Sorry, that spot has already been chosen. Please try again.'))
                    for x in orig_board:
                        print(x, end='')
                if player_1_input == 3 or player_1_input == 6 or player_1_input == 9:
                    orig_board[player_1_input] = '|_X_|\n'
                else:
                    orig_board[player_1_input] = '|_X_|'

                for x in orig_board:
                    print(x, end='')
                # Different ways Player 1 can win game.
                if orig_board[1] == '|_X_|' and orig_board[2] == '|_X_|' and orig_board[3] == '|_X_|\n' or \
                        orig_board[4] == '|_X_|' and orig_board[5] == '|_X_|' and orig_board[6] == '|_X_|\n' or \
                        orig_board[7] == '|_X_|' and orig_board[8] == '|_X_|' and orig_board[9] == '|_X_|\n' or \
                        orig_board[1] == '|_X_|' and orig_board[5] == '|_X_|' and orig_board[9] == '|_X_|\n' or \
                        orig_board[7] == '|_X_|' and orig_board[5] == '|_X_|' and orig_board[3] == '|_X_|\n' or \
                        orig_board[1] == '|_X_|' and orig_board[4] == '|_X_|' and orig_board[7] == '|_X_|' or \
                        orig_board[2] == '|_X_|' and orig_board[5] == '|_X_|' and orig_board[8] == '|_X_|' or \
                        orig_board[3] == '|_X_|\n' and orig_board[6] == '|_X_|\n' and orig_board[9] == '|_X_|\n':
                    print('\n\nPlayer_1 WINS!!!!!!')
                    print('GAME OVER')
                    play_again()
                # Indicate what a cats game is. Game over, player asked to play again.
                if orig_board[1] != '|_1_|' and orig_board[2] != '|_2_|' and orig_board[3] != '|_3_|\n' \
                        and orig_board[4] != '|_4_|' and orig_board[5] != '|_5_|' and orig_board[6] != '|_6_|\n' \
                        and orig_board[7] != '|_7_|' and orig_board[8] != '|_8_|' and orig_board[9] != '|_9_|\n':
                    print('\n\nCATS GAME')
                    print('GAME OVER')
                    play_again()
            # Catch errors
            except ValueError:
                print('Please choose a number between 1 and 9. Value Error')
                for x in orig_board:
                    print(x, end='')
            except IndexError:
                print('Please choose a number between 1 and 9. Index Error')
                for x in orig_board:
                    print(x, end='')
            # Player 1 turn ends. Player 2 turn begins.
            else:
                player_1 = False
        # Create player 2 and ask for input
        while player_2:
            try:
                player_2_input = int(input(f'\n\nPlayer_2, where would you like to place your O?: '))
                # Depending on the input of player 2, their input will be denied or accepted.
                while orig_board[player_2_input] == '|_O_|' or orig_board[player_2_input] == '|_O_|\n' or orig_board[
                        player_2_input] == '|_X_|' or orig_board[player_2_input] == '|_X_|\n':
                    player_2_input = int(input('Sorry, that spot has already been chosen. Please try again.'))
                    for x in orig_board:
                        print(x, end='')
                if player_2_input == 3 or player_2_input == 6 or player_2_input == 9:
                    orig_board[player_2_input] = '|_O_|\n'
                else:
                    orig_board[player_2_input] = '|_O_|'

                for x in orig_board:
                    print(x, end='')

                # Different ways Player 2 can win game.
                if orig_board[1] == '|_O_|' and orig_board[2] == '|_O_|' and orig_board[3] == '|_O_|\n' or \
                        orig_board[4] == '|_O_|' and orig_board[5] == '|_O_|' and orig_board[6] == '|_O_|\n' or \
                        orig_board[7] == '|_O_|' and orig_board[8] == '|_O_|' and orig_board[9] == '|_O_|\n' or \
                        orig_board[1] == '|_O_|' and orig_board[5] == '|_O_|' and orig_board[9] == '|_O_|\n' or \
                        orig_board[7] == '|_O_|' and orig_board[5] == '|_O_|' and orig_board[3] == '|_O_|\n' or \
                        orig_board[1] == '|_O_|' and orig_board[4] == '|_O_|' and orig_board[7] == '|_O_|' or \
                        orig_board[2] == '|_O_|' and orig_board[5] == '|_O_|' and orig_board[8] == '|_O_|' or \
                        orig_board[3] == '|_O_|\n' and orig_board[6] == '|_O_|\n' and orig_board[9] == '|_O_|\n':
                    print('\n\nPlayer_2 WINS!!!!!!')
                    print('GAME OVER')
                    play_again()
                # Cats game. Game over, player will be asked to play again.
                if orig_board[1] != '|_1_|' and orig_board[2] != '|_2_|' and orig_board[3] != '|_3_|\n' \
                        and orig_board[4] != '|_4_|' and orig_board[5] != '|_5_|' and orig_board[6] != '|_6_|\n' \
                        and orig_board[7] != '|_7_|' and orig_board[8] != '|_8_|' and orig_board[9] != '|_9_|\n':
                    print('\n\nCATS GAME')
                    print('GAME OVER')
                    play_again()
            # Catch errors
            except ValueError:
                print('Please choose a number between 1 and 9.')
                for x in orig_board:
                    print(x, end='')
            except IndexError:
                print('Please choose a number between 1 and 9.')
                for x in orig_board:
                    print(x, end='')
            # Player 2 turn ends. Player 1 turn begins.
            else:
                player_2 = False

# Call function to play game.
tic_tac_toe()











