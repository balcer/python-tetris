import sys

print "Tetris"

game_board = [[0 for x in range(22)] for x in range(14)]

game_board[5][2] = 3

def print_game_board():
    for y in range(0, 22):
        for x in range(0, 14):
            sys.stdout.write(str(game_board[x][y]))
        print ""

print_game_board()
