import sys
import time
import os
import pygame
import copy
BOARD_X_SIZE = 10
BOARD_Y_SIZE = 22

TIME_EVENT = pygame.USEREVENT+1

game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]

I_block = [[0, 0, 2, 0],[0, 0, 2, 0],[0, 0, 3, 0],[0, 0, 2, 0],[0, 0, 0, 0]]
T_block = [[0, 0, 0, 0],[0, 0, 2, 0],[0, 0, 3, 2],[0, 0, 2, 0],[0, 0, 0, 0]]

current_block = T_block

current_x_position = 0
current_y_position = 3
actual_rotation = 0

game_exit = False

pygame.init()
        
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Tetris')

def print_game_board():
    gameDisplay.fill((0,0,0))
    pygame.draw.line(gameDisplay, (0, 0, 255), (20, 20), (20, 420), 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (20, 420), (220, 420), 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (220, 420), (220, 20), 1)
    temp_game_board = copy.deepcopy(game_board)
    for y in range(4):
        for x in range(4):
            if current_block[x][y] != 0:
                temp_game_board[current_x_position + x][current_y_position + y] = current_block[x][y]
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            if temp_game_board[x][y] != 0 and y > 1:
                pygame.draw.rect(gameDisplay, (255, 0 , 0), ((22*(x+1))-(x*2), (20*(y+1)-39), 18, 18), 0)
    pygame.display.update()

def try_to_place_block(action, brick):
    global game_board
    global current_x_position
    global current_y_position
    taken_places_count = 0
    temp_game_board = [[0 for x in range(BOARD_Y_SIZE + 2)] for x in range(BOARD_X_SIZE + 4)]
    for y in range(BOARD_Y_SIZE + 2):
        for x in range(BOARD_X_SIZE + 4):
            if x < 2 or x > 11 or y > 21:
                temp_game_board[x][y] = 9
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            temp_game_board[x+2][y] = game_board[x][y]
            if game_board[x][y] != 0:
                taken_places_count = taken_places_count + 1
    for y in range(4):
        for x in range(4):
            if action == 1:
                if brick[x][y] is not 0:
                    temp_game_board[x + current_x_position + 2][y + current_y_position + 1] = brick[x][y]
            elif action == 2:
                if brick[x][y] is not 0:
                    temp_game_board[x + current_x_position + 3][y + current_y_position] = brick[x][y]
            elif action == 3:
                if brick[x][y] is not 0:
                    temp_game_board[x + current_x_position + 1][y + current_y_position] = brick[x][y]

    temp_border_count = 0
    for y in range(BOARD_Y_SIZE + 2):
        for x in range(BOARD_X_SIZE + 4):
            if temp_game_board[x][y] == 9:
                temp_border_count = temp_border_count + 1
    if temp_border_count == 116:
        print "Border OK"
        if action == 1:
            current_y_position = current_y_position + 1
        elif action == 2:
            current_x_position = current_x_position + 1
        elif action == 3:
            current_x_position = current_x_position - 1
    print temp_game_board

pygame.time.set_timer(TIME_EVENT, 1000)

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == TIME_EVENT:
            print "Time"
            try_to_place_block(1, current_block)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print "Lewo"
                try_to_place_block(3, current_block)
            elif event.key == pygame.K_RIGHT:
                print "Prawo"
                try_to_place_block(2, current_block)
            elif event.key == pygame.K_DOWN:
                print "Dol"
                try_to_place_block(1, current_block)
            elif event.key == pygame.K_SPACE:
                print "Rotacja"
            elif event.key == pygame.K_ESCAPE:
                game_exit = True
    print_game_board()

pygame.quit()
quit()

def screen_update():
    try_to_place_block(T_block, 5, 4)
    print_game_board()
    root.after(500, screen_update)

def on_key_press(event):
    pressed_key = event.char
    if event.keysym == 'Escape':
        root.quit()
    text.insert('end', 'You pressed %s\n' % (event.char, ))


