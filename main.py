# ---------Global Variables --------

# Game Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If game is still going
game_still_going = True

# who won? or Tie?
winner = None

# Who's turn is it?
current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# play game
def play_game():

    # print initial board
    display_board()

    #while game is still going
    while game_still_going:

        # Handle is a single turn for a arbituary player
        handle_turn(current_player)

        # check if game ended
        check_if_game_over()

        # Flip to other player
        flip_player()

    # GAME HAS ENDED
    if winner == "X" or winner == "O":
        print(winner + " WON")
    elif winner == None:
        print("TIE")

# handle a turn of arbitrary player
def handle_turn(player):

    print(player + "'s turn")
    position = input("Enter the posotion between 1-9: ")

    valid = False
    while not valid:

        # loop to check if user entered a valid input
        while position not in ["1","2","3","4","5","6","7","8","9"]:

            position = input("Enter the posotion between 1-9: ")

        position = int(position) -1

        if board[position]  == "-":
            valid = True
        else:
            print("you can't go there. Try again")


    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # global variables
    global winner

    # Check Rows
    row_winner = check_rows()

    # Check Columns
    column_winner = check_columns()

    # Check Diagnals
    diagnal_winner = check_diagnals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner = None

    return

def check_rows():

    #setup global variables
    global  game_still_going

    #check the rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if any row has a winner means there is a winner
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner ('X' or 'O')
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # setup global variables
    global game_still_going

    # check the column
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # if any column has a winner means there is a winner
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner ('X' or 'O')
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagnals():
    # setup global variables
    global game_still_going

    # check the diagnal
    diagnals_1 = board[0] == board[4] == board[8] != "-"
    diagnals_2 = board[6] == board[4] == board[2] != "-"


    # if any diagnal has a winner means there is a winner
    if diagnals_1 or diagnals_2:
        game_still_going = False

    # Return the winner ('X' or 'O')
    if diagnals_1:
        return board[0]
    elif diagnals_2:
        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return


def flip_player():

    global current_player

    if current_player == "X":
        current_player ="O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()