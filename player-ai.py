from math import inf as infinity
from random import choice 
import time
from os import system
import platform

HUMAN = -1 # human is the min
AI = +1 # bot is the max
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

def evaluateState(state):
    if wins(state, AI):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):
    winning_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
    ]

    if [player, player, player] in winning_state:
        return True
    else:
        return False

def gameOver(state):
    return wins(state, HUMAN) or wins(state, AI)

def findEmptyCells(state):
    empty_cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                empty_cells.append([x,y])

    return empty_cells

def findValidMove(x, y):
    if [x,y] in findEmptyCells(board):
        return True
    else:
        return False

def setMove(x, y, player):
    if findValidMove(x, y):
        board[x][y] = player
        return True
    else:
        return False

def calculateMinimax(state, depth, player):
    if player == AI:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or gameOver(state):
        score = evaluateState(state)
        return [-1, -1, score]

    for cell in findEmptyCells(state):
        x = cell[0]
        y = cell[1]
        state[x][y] = player
        score = calculateMinimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0] = x
        score[1] = y

        if player == AI:
            if score[2] > best[2]:
                best = score

        else:
            if score[2] < best[2]:
                best = score

    return best

def cleanConsole():
    os = platform.system().lower()
    if 'windows' in os:
        system('cls')
    else:
        system('clear')

def renderBoard(state, ai_choice, human_choice):
    chars = {
        -1: human_choice,
        +1: ai_choice,
        0: ' ',
    }

    line = '---------------'
    print('\n' + line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + line)

def aiTurn(ai_choice, human_choice):
    depth = len(findEmptyCells(board))
    if depth == 0 or gameOver(board):
        return

    cleanConsole()

    print(f'Computer turn [{ai_choice}]')
    renderBoard(board, ai_choice, human_choice)

    if depth == 9:
        x = choice([0,1,2])
        y = choice([0,1,2])
    else:
        move = calculateMinimax(board, depth, AI)
        x = move[0]
        y = move[1]

    setMove(x, y, AI)
    time.sleep(1)

def humanTurn(ai_choice, human_choice):
    depth = len(findEmptyCells(board))
    if depth == 0 or gameOver(board):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    cleanConsole()
    print(f'Human turn [{human_choice}]')
    renderBoard(board, ai_choice, human_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = setMove(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

def main():
    cleanConsole()
    ai_choice = ''
    human_choice = ''
    first = ''

    while human_choice != 'O' and human_choice != 'X':
        try:
            print('')
            human_choice = input('Choose X or O')
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if human_choice == 'X':
        ai_choice = 'O'
    else:
        ai_choice = 'X'

    cleanConsole()

    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(findEmptyCells(board)) > 0 and not gameOver(board):
        if first == 'N':
            aiTurn(ai_choice, human_choice)
            first = ''

        humanTurn(ai_choice, human_choice)
        aiTurn(ai_choice, human_choice)

    # Game over message
    if wins(board, HUMAN):
        cleanConsole()
        print(f'Human turn [{human_choice}]')
        renderBoard(board, ai_choice, human_choice)
        print('YOU WIN!')
    elif wins(board, AI):
        cleanConsole()
        print(f'Computer turn [{ai_choice}]')
        renderBoard(board, ai_choice, human_choice)
        print('YOU LOSE!')
    else:
        cleanConsole()
        renderBoard(board, ai_choice, human_choice)
        print('DRAW!')

    exit()

if __name__ == '__main__':
    main()
