# TIC TAC TOE IN PYTHON
# Developed by Mahshid Ahmadi


import os

# defined variables
w, h = 4, 4
global board
board = [['_' for x in range(w)] for y in range(h)]
global player
player = 'x'
global plays
plays = 0
global winner
winner = ""


# Give initial values to the matrix
def init():
    for i in range(w):
        for j in range(h):
            print('_', end=" ")
        print('\n')


# Clearing the screen
def clearscreen():
    os.system("clear")


# checking the inputs if it's right or not
def validate(number):
    number = int(number)
    if number >= 1 and number <= 3:
        return True
    else:
        print("please pick a value between 1 to 3")
        return False


# understanding who is the winner
def gameover():
    global plays
    global winner
    plays += 1
    if plays > 5:
        if board[1][1] == board[1][2] and board[1][2] == board[1][3] and board[1][2] != '_':
            print("is the winner ", winner)
            return True
        elif board[2][1] == board[2][2] and board[2][2] == board[2][3] and board[2][2] != '_':
            print("is the winner ", winner)
            return True
        elif board[3][1] == board[3][2] and board[3][2] == board[3][3] and board[3][2] != '_':
            print("is the winner ", winner)
            return True
        elif board[1][1] == board[2][1] and board[2][1] == board[3][1] and board[2][1]:
            print("is the winner ", winner)
            return True
        elif board[1][2] == board[2][2] and board[2][2] == board[3][2] and board[2][2] != '_':
            print("is the winner ", winner)
            return True
        elif board[1][3] == board[2][3] and board[2][3] == board[3][3] and board[2][3] != '_':
            print("is the winner ", winner)
            return True
        elif board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[2][2] != '_':
            print("is the winner ", winner)
            return True
        elif board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[2][2] != '_':
            print("is the winner ", winner)
            return True
    return False


# process of the game
def showBoard():
    global player
    while not gameover():
        print('x') if player == 'x' else print('o')
        clearscreen()
        row = 0
        col = 0
        print("it's", player, "'s turn", "\n")
        # printing column numbers
        print("\t")
        for i in range(1, 4):
            print(" ", i, end=" ")
        print("\n")
        # print numbers and _s
        for i in range(1, 4):
            print(i, end="  ")
            for j in range(1, 4):
                print(board[i][j], end="  ")
            print("\n")
        # getting the row and column
        while not validate(row):
            row = int(input("In what row would you like to play? =>"))
        while not validate(col):
            col = int(input("In what column would you like to play? => "))

        # putting the parameter in right place
        board[row][col] = player
        print('x') if player == 'x' else print('o')
        player = 'o' if player == 'x' else 'x'


# main function
def main():
    plays = 0
    print("Welcome to Tic-Tac-Toe game")
    init()
    showBoard()


# start the GAME
main()
