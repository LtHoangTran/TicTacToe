# Tic Tac Toe
# Fully done by yours truly, with various features incoporated from various sources
# A 3x3 TicTacToe game, with user capable of choosing X or O, the size of the Tic Tac Toe table, and the level of the computer
# Any idea on how to make sizeable field based on input (like 3x3, 4x4, 5x5...)? Or how to set if we can go first?

import random

name = ''
playerSymbol = ''
compSymbol = ''
turn = 0
board = [' ' for x in range(10)]
size = ''
level = ''

def fillInCell(letter, position):           # fill in a certain cell
    board[position] = letter

def spaceIsFree(position):
    return board[position] == ' '           # check if the space/cell is still free (if yes, will return true)

def printSmallBoard():
    print('Small board size has been selected')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

def printLargeBoard():
    print('Large board size has been selected')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def printRandomSizeBoard():
    global size
    size = random.randint(1,2)
    if size == 1:
        printLargeBoard()
    elif size == 2:
        printSmallBoard()
    size=str(size)

def printIndexBoard():                      # print an index board, to tell how the cells are number
    print('''
             1 | 2 | 3
             ---------
             4 | 5 | 6
             ---------
             7 | 8 | 9
             ''')

def playerMove():
    # handle the turn of the player
    global playerSymbol
    
    canRun = True                           # set the boolean variable
    while canRun:
        print('Turn of ' + name +'. With symbol ' + playerSymbol + '.')
        move = input('Please choose a position, anywhere between 1 and 9.\n')
        try:                                # just in case input is not an integer
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):       # check if the space/cell is still free (if yes, will return true)
                    canRun = False
                    fillInCell(playerSymbol, move)
                else:
                    print('The cell has been occupied. Please choose another.\n')
            else:
                print('Please input a number between 1 and 9.\n')
        except:
            print('Please input a number between 1 and 9.\n')

def compRandomMove():
    global compSymbol

    # for the x-th index of board, with value "letter", and (if the cell is blank, the index is not 0)
    # the 0-th index of the board is ignored in this script
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = random.choice(possibleMoves)
    return move

    
                
def compHardMove():
    # handle the turn of the computer at hard mode
    # use of a simple so-call "AI". Ask Tim the tech, not me. I'm impressed with his code.

    # for the x-th index of board, with value "letter", and (if the cell is blank, the index is not 0)
    # the 0-th index of the board is ignored in this script
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]            # Make a new copy of the current board, and work on that, actively fill in to win
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move                 # return the index of the cell to win

    cornersOpen = []                        # if no immediate win, check if corners are open
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)          
    if len(cornersOpen) > 0:
        move = random.choice(cornersOpen)   # if corners are open, fill in one cell randomly  
        return move

    if 5 in possibleMoves:                  # check the center
        move = 5
        return move

    edgesOpen = []                          # check the edges
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)         
    if len(edgesOpen) > 0:
        move = random.choice(edgesOpen)     # if edges are open, fill in one cell randomly
        return move
        
    return move   
    
    
def selectCompMove():
    level = random.randint(1,2)
    if level == 1:
        print('The computer will fill in randomly.')
        compRandomMove()
    elif level == 2:
        print('The computer will actively shaft you.')
        compHardMove()
    level = str(level)

def isWinner(bo,le):                                                    # check win condition, return True (if one has won) of False (if the game is still going)
    return (
           (bo[7] == le and bo[8] == le and bo[9] == le) or
           (bo[4] == le and bo[5] == le and bo[6] == le) or
           (bo[1] == le and bo[2] == le and bo[3] == le) or
           (bo[1] == le and bo[4] == le and bo[7] == le) or
           (bo[2] == le and bo[5] == le and bo[8] == le) or
           (bo[3] == le and bo[6] == le and bo[9] == le) or
           (bo[1] == le and bo[5] == le and bo[9] == le) or
           (bo[3] == le and bo[5] == le and bo[7] == le)
           )

def isBoardFull(board):                                                 # check if the board is full
    if board.count(' ') >1:
        return False
    else:
        return True

def initiateGame():
    # name, playerSymbol, compSymbol, size are all set as global variables
    global name
    global playerSymbol
    global compSymbol
    global size
    global level

    # asking for name and the selected symbol of the player
    printIndexBoard()
    print('Welcome to a Tic Tac Toe game.')
    print('Please input your name: ')
    name = input()
    
    while playerSymbol.upper() not in ['X', 'O']:
        print('Please input the correct symbol, X or O.')
        playerSymbol = input()

    # set symbol for the computer    
    playerSymbol = playerSymbol.upper()
    if playerSymbol == 'X':
        compSymbol = 'O'
    else:
        compSymbol = 'X'

    # select size of the Python board
    print('What is the size of the board? Input 1 for large, or 2 for small. Enter 3 for random.')
    size = input()
    while size not in ['1','2','3']:
        print('''Please input the correct value.
                   - 1 for large board
                   - 2 for small board
                   - 3 for random size
                   ''')
        size = input()
    if size == '1':
        printLargeBoard()
    elif size == '2':
        printSmallBoard()
    else:
        printRandomSizeBoard()

    # choosing level to play
    print('What is the level you want to play? 1 for easy/random/stupid computer, 2 for a hard one, 3 for random choosing.')
    level = input()
    while level not in ['1','2','3']:
        print('''Please input the correct value.
                   - 1 for a computer random filling in
                   - 2 for a tough computer, "remedy AI"
                   - 3 for random choosing
                   ''')
        level = input()
    if level == '1':
        print('The computer will fill in randomly.')
        compRandomMove()
    elif level == '2':
        print('The computer will actively shaft you. You need brain to defeat it.')  # Not impossible, but if you are able to defeat it once, you can do it again
        compHardMove()
    else:
        selectCompMove()

    print('')
    print('NOTE: In this game, you will go first.')     # Because I haven't figured out a nice and easy way to choose who to go first

    # game is ready to play at this point. Switch to fill and handle turn
    

def main():
    # The main part of the script
    global playerSymbol
    global compSymbol
    global size
    global name
    global level

    # set up the conditions
    initiateGame()
    while not(isBoardFull(board)):
        if not(isWinner(board, compSymbol)):
               playerMove()
               if size == '1':
                    printLargeBoard()
                    print('')
               else:
                    printSmallBoard()
                    print('')
        else:
            print('Sorry, the computer has won.')
            break

        if not(isWinner(board, playerSymbol)):
            if level == '1':
                move = compRandomMove()
            else:
                move = compHardMove()
            if move == 0:
                print('Tie Game!')
            else:
                fillInCell(compSymbol,move)
                print('Computer places an ' + compSymbol + ' in position: ',move)
                if size == '1':
                    printLargeBoard()
                    print('')
                else:
                    printSmallBoard()
                    print('')
        else:
            print('Congrat, ' + name + ' has won the game.')
            break               

while True:
    answer = input('Do you want to play again? (Y/N)\n')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        print('Thank you for playing.')
        input('Press enter to exit.')
        break
