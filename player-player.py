import sys
import platform
from os import system

# Create dictionary representation of the board
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
            
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# return boolean
def checkWinner(board):
    # Check vertical winning positions
    if board['7'] == board['4'] and board['4'] == board['1'] and board['7'] != ' ':
        return True
    if board['8'] == board['5'] and board['5'] == board['2'] and board['8'] != ' ':
        return True
    if board['9'] == board['6'] and board['6'] == board['3'] and board['9'] != ' ':
        return True

    # Check horizontal winning positions
    if board['7'] == board['8'] and board['8'] == board['9'] and board['7'] != ' ':
        return True
    if board['4'] == board['5'] and board['5'] == board['6'] and board['4'] != ' ':
        return True
    if board['1'] == board['2'] and board['2'] == board['3'] and board['1'] != ' ':
        return True

    # Check diagonal winning positions
    if board['7'] == board['5'] and board['5'] == board['3'] and board['7'] != ' ':
        return True
    if board['9'] == board['5'] and board['5'] == board['1'] and board['9'] != ' ':
        return True
    
    else:
        return False

def clear():
    
    os_name = platform.system().lower()
    if os_name == 'windows':
        # Windows terminal 
        system('cls')
    else:
        # Everything else 
        system('clear')

def makeMove(board, first, second):
    # Total of 9 turns in Tic-Tac-Toe
    for turn in range(9):
        if turn % 2 == 0:
            place = first
        else:
            place = second

        move = input("Enter a move from position 1 to 9: ")
        
        if int(move) < 1 or int(move) > 9:
            print("The only positions to play are 1 to 9")
            while True:
                move = input("Enter a valid move from position 1 to 9: ")
                if 1 <= int(move) <= 9:
                    break

                else:
                    continue

        if board[move] == ' ':
            board[move] = place
            clear()
            printBoard(board)
            
            if checkWinner(board) == True:
                # The last person to play a move is the winner
                print("\nplayer {} is the winner".format(place))
                sys.exit() 
        
        elif board[move] != ' ':
            print("this position has already been played")
            while True:
                move = input("Enter a move from position 1 to 9: ")

                if int(move) < 1 or int(move) > 9:
                    print("The only positions to play are 1 to 9")
                    while True:
                        move = input("Enter a valid move from position 1 to 9: ")
                        if 1 <= int(move) <= 9:
                            break

                        else:
                            continue

                if board[move] == ' ':
                    board[move] = place
                    clear()
                    printBoard(board)

                    if checkWinner(board) == True:
                        print("\nplayer {} is the winner".format(place))
                        sys.exit()

                    break

                else:
                    print("this position has already been played")
                    continue

    if checkWinner(board) == False:
        print("\nCat game!")
        sys.exit()

if __name__ == '__main__':
    print("Playing Tic-Tac-Toe\n")
    print("Press Ctrl + c to terminate the game\n")
    
    player = input("Who makes the first move X or O: ")
    if player == 'X':
        secondPlayer = 'O'
        printBoard(theBoard)
        makeMove(theBoard, player, secondPlayer)

    elif player == 'O':
        secondPlayer = 'X'
        printBoard(theBoard)
        makeMove(theBoard, player, secondPlayer)
