board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None
not_over = True
#player1 = None
#player2 = None
current_player = 'X'



def play_game():
    #global current_player
    #global player1
    #global player2
    display_board()
    while not_over:
        turn(current_player)

        check_over()

        flip_player()

    if winner == 'X' or winner == 'O':
        print(winner + " won!")
    elif winner == None:
        print("It's a draw!")
    #play_again()



def display_board():
    print('| '+board[0]+' | '+board[1]+' | '+board[2]+' |'+'        | 1 | 2 | 3 |')
    print('| '+board[3]+' | '+board[4]+' | '+board[5]+' |'+'        | 4 | 5 | 6 |')
    print('| '+board[6]+' | '+board[7]+' | '+board[8]+' |'+'        | 7 | 8 | 9 |')

# def choose_sign():
#     global player1
#     global player2
#     player1=input('Choose your sign (X or O): ')
#     while True:
#         if player1.upper()=='X':
#             player2='O'
#             print("You've choosen " + player1.upper() + ". Player 2 will be " + player2)
#             return(player1.upper(),player2)
#         elif player1.upper()=='O':
#             player2='X'
#             print("You've choosen " + player1.upper() + ". Player 2 will be " + player2)
#             return(player1.upper(),player2)
#         else:
#             player1 = input('Wrong! Choose your sign (X or O): ')

def turn(player):
    #global player1
    #global player2
    print(player + "'s turn.")
    space=input('Your move! Choose a position from 1-9: ')
    valid = False
    while not valid:
        while space not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            space = input('Your move! Choose a position from 1-9: ')
        space=int(space)-1
        if board[space] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[space] = player
    display_board()


def check_over():
    check_win()
    check_draw()


def check_win():
    global winner
    row_win = row()
    column_win = column()
    diagonal_win = diagonal()
    if row_win:
        winner=row_win
    elif column_win:
        winner=column_win
    elif diagonal_win:
        winner=diagonal_win
    else:
        winner=None
    return


def check_draw():
    global not_over
    if '-' not in board:
        not_over = False
    return

def row():
    global not_over
    row1=board[0]==board[1]==board[2]!='-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        not_over=False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return

def column():
    global not_over
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        not_over = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return

def diagonal():
    global not_over
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        not_over = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return

def flip_player():
    global current_player
    #global player1
    #global player2
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

# def play_again():
#     global board
#     again = input('Do you wanna play again? (y/n): ')
#     if again.lower()=='y':
#         board = ['-']*10
#         check_over()
#         play_game()





play_game()