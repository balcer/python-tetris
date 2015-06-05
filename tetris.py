import sys
import time
import os
import copy
import pygame

BOARD_X_SIZE=10
BOARD_Y_SIZE=22

TIME_EVENT = pygame.USEREVENT+1

game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]

game_exit = False

pygame.init()
        
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Tetris')

def print_game_board():
    pygame.draw.line(gameDisplay, (0, 0, 255), (20, 20), (20, 420), 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (20, 420), (220, 420), 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (220, 420), (220, 20), 1)
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            if game_board[x][y] == 0 and y > 1:
                pygame.draw.rect(gameDisplay, (255, 0 , 0), ((22*(x+1))-(x*2), (20*(y+1)-39), 18, 18), 1)
    pygame.display.update()

pygame.time.set_timer(TIME_EVENT, 1000)

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == TIME_EVENT:
            print "Time"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print "Lewo"
            elif event.key == pygame.K_RIGHT:
                print "Prawo"
            elif event.key == pygame.K_DOWN:
                print "Dol"
            elif event.key == pygame.K_SPACE:
                print "Rotacja"
            elif event.key == pygame.K_ESCAPE:
                game_exit = True
    print_game_board()

pygame.quit()
quit()

temp_game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]
actual_x_position = 4
actual_y_position = 5

I_block = [[0, 0, 2, 0, 0],[0, 0, 2, 0, 0],[0, 0, 3, 0, 0],[0, 0, 2, 0, 0],[0, 0, 0, 0, 0]]
T_block = [[0, 0, 0, 0, 0],[0, 0, 2, 0, 0],[0, 0, 3, 2, 0],[0, 0, 2, 0, 0],[0, 0, 0, 0, 0]]
Current_block = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

def try_to_place_block(block, x, y):
    global game_board
    global temp_game_board
    temp_game_board = copy.deepcopy(game_board)
    for i in range(5):
        for j in range(5):
            if block[j][i] != 0:
                temp_game_board[j+x][i+y] = T_block[j][i]
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            if x == 0 or x == 1 or x == BOARD_X_SIZE-2 or x == BOARD_X_SIZE-1 or y == BOARD_Y_SIZE-2 or y == BOARD_Y_SIZE-1:
                if temp_game_board[x][y] != 1:
                    return 0

def screen_update():
    try_to_place_block(T_block, 5, 4)
    print_game_board()
    root.after(500, screen_update)

def init_game_board():
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            if x == 0 or x == 1 or x == BOARD_X_SIZE-2 or x == BOARD_X_SIZE-1 or y == BOARD_Y_SIZE-2 or y == BOARD_Y_SIZE-1:
                game_board[x][y] = 1

def on_key_press(event):
    pressed_key = event.char
    if event.keysym == 'Escape':
        root.quit()
    text.insert('end', 'You pressed %s\n' % (event.char, ))

init_game_board()

