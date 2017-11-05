from __future__ import print_function

from IPython.display import clear_output
#create the layout of the tic tac tow board using a list
def display_board(board):
    print
    print ' - - - - - - - - - '
    print '| ', board[0], ' | ', board[1], ' | ', board[2], '|'
    print ' - - - - - - - - - '
    print '| ', board[3], ' | ', board[4], ' | ', board[5], '|'
    print ' - - - - - - - - - '
    print '| ', board[6], ' | ', board[7], ' | ', board[8], '|'
    print ' - - - - - - - - - '

def player_input():
    #loop until the player selects the correct marker
    #find out what player one wants to be, then assign the other choice to player 2
    while True:
        print 'What marker does player 1 want [X] or [O]'
        answer = raw_input()
        if answer == 'X' or 'x':
            print '\nPlayer one is [X]'
            print 'Player two is [O]'
            P1_marker = 'X'
            break
        if answer == 'O' or 'o':
            print '\nPlayer one is [O]'
            print 'Player two is [X]'
            P1_marker = 'O'
            break
        #if the correct input was not entered, ask again
        else:
            print 'Incorrect input. Try Again'
            continue
    return P1_marker

def place_marker(board, marker, position):
    #determine if the position given is in the range of the list
    #insert the marker at said position then remove the previous
    #value in that space
    if int(position) in range(1,10):
        board.insert(int(position)-1, marker)
        board.remove(position)
    else:
        print 'Not in range'

def win_check(board,mark):
        #create a matrix of rows
        first_row = [board[0],board[1],board[2]]
        second_row = [board[3],board[4],board[5]]
        third_row = [board[6],board[7],board[8]]
        board_rows = [first_row, second_row, third_row]
        #check for horizontal win
        for x in board_rows:
            if x.count(mark) == 3:
                return True

        #create a column matrix
        first_col = [board[0],board[3],board[6]]
        second_col = [board[1],board[4],board[7]]
        third_col = [board[2],board[5],board[8]]
        board_cols = [first_col, second_col, third_col]
        #check for vertical win
        for x in board_cols:
            if x.count(mark) == 3:
                return True

        #create a diafonal matrix
        left_to_right = [board[0],board[4],board[8]]
        rigth_to_left = [board[2],board[4],board[6]]
        board_diagonal = [left_to_right, rigth_to_left]
        #check for diagonal wins
        for x in board_diagonal:
            if x.count(mark) == 3:
                return True

import random
def choose_first():
    #randomly select player 1 or 2 to go first
    if random.randint(1,2) == 1:
        first = 'Player 1'
    else:
        first = 'Player 2'
    return first

def space_check(board, position):
    #determine if a player has placed a marker in that space yet or not
    if 'X' in board[int(position)-1]:
        print '\nBad space.'
        print 'Choose again'
        return False

    if 'O' in board[int(position)-1]:
        print '\nBad space.'
        print 'Choose again'
        return False

    return True

def full_board_check(board):
    #determine if the board has become full and no winner has been determined yet
    for item in board:
        if item.isdigit() == True:
            return False

    return True

def player_choice(board):
    #retrive player desired position
    position = raw_input()
    #determine if the input is in the desired range or not
    if position in range(1,10):
        print 'Choose a number between 1 and 9'
    return position

def replay():
    #ask to play the game again come completed
    print 'Do you want play again? (y/n)'
    answer = raw_input()
    if answer == 'y':
        return True
    else:
        return False

#main game
print('Welcome to Tic Tac Toe!')

game_on = True
board = ['1','2','3','4','5','6','7','8','9'] #default board
P1_marker = player_input()
#need 2 marker variables X and O
if P1_marker == 'X':
    P2_marker = 'O'
else:
    P2_marker = 'X'
 #determine which player goes first
if choose_first() == 'Player 1':
    P1_first = True
else:
    P1_first = False

display_board(board)
while game_on:

    if P1_first == True:
        #Player1's turn
        print "Player 1's Turn"
        print 'Choose location on board'

        #loop until a marker is correctly placed on the board
        while True:
            position = player_choice(board)

            #check space and place on board if allowed
            if space_check(board,position) == True:
                place_marker(board, P1_marker,position)
                break

        display_board(board)
        #let player 2 go
        P1_first = False

        #check if player 1 has won
        if win_check(board, P1_marker) == True:
            print "Player 1 WINS!"
            #ask to replay the game
            if replay():
                board = ['1','2','3','4','5','6','7','8','9'] #reset board
                display_board(board)
            else:
                game_on = False
                break
################################################################################

    if P1_first == False:
        # Player2's turn.
        print "Player 2's Turn"
        print 'Choose location on board'

        #loop until a marker is correctly placed on the board
        while True:
            position = player_choice(board)
            #check space and place on board if allowed
            if space_check(board,position) == True:
                place_marker(board, P2_marker,position)
                break

        display_board(board)
        #let player 1 go
        P1_first = True
        #check if player 1 has won
        if win_check(board, P2_marker) == True:
            print "Player 2 WINS!"
            #ask to replay the game
            if replay():
                board = ['1','2','3','4','5','6','7','8','9'] #reset board
                display_board(board)
            else:
                game_on = False
                break

####################################################################################
    #determine if board is full
    if full_board_check(board) == True:
        print 'Board is full'
        print 'Cat game'
        #ask to play again
        if replay():
            board = ['1','2','3','4','5','6','7','8','9'] #reset board
            display_board(board)
        else:
            game_on = False
            break

print '\nThanks for planying!'
