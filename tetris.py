import sys

print "Tetris"

game_board = [[0 for x in range(22)] for x in range(14)]

game_board[5][2] = 3

def print_game_board():
    for y in range(0, 22):
        for x in range(0, 14):
            sys.stdout.write(str(game_board[x][y]))
        print ""

def init_game_board():
    for y in range(0, 22):
        for x in range(0, 14):
            if x == 0 or x == 1 or x == 12 or x == 13 or y == 20 or y == 21:
                game_board[x][y] = 1

                
    
init_game_board()
print_game_board()
