import pygame
import copy
import random

BOARD_X_SIZE = 10
BOARD_Y_SIZE = 22

TIME_EVENT = pygame.USEREVENT+1

game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]

O_block = [[0, 0, 0, 0],[0, 2, 2, 0],[0, 3, 2, 0],[0, 0, 0, 0]]
I_block = [[0, 2, 0, 0],[0, 2, 0, 0],[0, 3, 0, 0],[0, 2, 0, 0]]
S_block = [[0, 0, 0, 0],[0, 0, 2, 0],[0, 3, 2, 0],[0, 2, 0, 0]]
Z_block = [[0, 0, 0, 0],[0, 2, 0, 0],[0, 3, 2 ,0],[0, 0, 2, 0]]
L_block = [[0, 0, 0, 0],[0, 2, 2, 0],[0, 3, 0, 0],[0, 2, 0, 0]]
J_block = [[0, 0, 0, 0],[0, 2, 0, 0],[0, 3, 0, 0],[0, 2, 2, 0]]
T_block = [[0, 0, 0, 0],[0, 2, 0, 0],[0, 3, 2, 0],[0, 2, 0, 0]]

def pick_random_block():
    a = random.randint(1, 7)
    if a == 1:
        return O_block
    elif a == 2:
        return I_block
    elif a == 3:
        return S_block
    elif a == 4:
        return Z_block
    elif a == 5:
        return L_block
    elif a == 6:
        return J_block
    elif a == 7:
        return T_block

def start_game():
    #Game state variables
    global current_x_position
    global current_y_position
    global game_exit
    global gameDisplay
    global current_block
    global next_block
    current_x_position = 2
    current_y_position = 2
    game_exit = False
    gameDisplay = pygame.display.set_mode((380, 445))
    current_block = pick_random_block()
    next_block = pick_random_block()

    pygame.init()
    pygame.display.set_caption('Tetris')
    pygame.time.set_timer(TIME_EVENT, 1000)
    global game_font
    game_font = pygame.font.SysFont("monospace", 18)

def start_new_round():
    global game_board
    global current_block
    global next_block
    global current_x_position
    global current_y_position
    for y in range(4):
        for x in range(4):
            if current_block[x][y] != 0:
                game_board[current_x_position + x][current_y_position + y] = 8
    current_block = next_block
    next_block = pick_random_block()
    current_x_position = 2
    current_y_position = 2

def print_game_board():
    gameDisplay.fill((0,0,0))
    label = game_font.render("Next block:", 1, (255,255,255))
    gameDisplay.blit(label, (240, 25))
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
                pygame.draw.rect(gameDisplay, (255, 0, 0), ((22*(x+1))-(x*2), (20*(y+1)-39), 18, 18), 0)
    for y in range(4):
        for x in range(4):
            if next_block[x][y] != 0:
                pygame.draw.rect(gameDisplay, (255, 0, 0), ((225 + 22*(x+1))-(x*2), (20*(y+1) + 20), 18, 18), 0)
    pygame.display.update()

def try_to_place_block(action, brick):
    global game_board
    global current_x_position
    global current_y_position
    taken_places_count = 0
    #Preparing temporary game board to check is move possible. Forbbiten places marked with 9
    temp_game_board = [[0 for x in range(BOARD_Y_SIZE + 2)] for x in range(BOARD_X_SIZE + 4)]
    for y in range(BOARD_Y_SIZE + 2):
        for x in range(BOARD_X_SIZE + 4):
            if x < 2 or x > 11 or y > 21:
                temp_game_board[x][y] = 9
    #Copping of actual game bord and counting taken places
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            temp_game_board[x+2][y] = game_board[x][y]
            if game_board[x][y] == 8:
                taken_places_count = taken_places_count + 1
    #Placing block in place according to event
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
    #Checking if performed move is correct
    temp_border_count = 0
    temp_taken_places_count = 0
    for y in range(BOARD_Y_SIZE + 2):
        for x in range(BOARD_X_SIZE + 4):
            if temp_game_board[x][y] == 9:
                temp_border_count = temp_border_count + 1
            if temp_game_board[x][y] == 8:
                temp_taken_places_count = temp_taken_places_count + 1
    if temp_border_count == 116 and temp_taken_places_count == taken_places_count:
    #Taking apropiate actions
        if action == 1:
            current_y_position = current_y_position + 1
        elif action == 2:
            current_x_position = current_x_position + 1
        elif action == 3:
            current_x_position = current_x_position - 1
    else:
        if action == 1:
            start_new_round()

    print temp_game_board

start_game()

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
