import pygame
import block
import copy
import random
import dbus

BOARD_X_SIZE = 10
BOARD_Y_SIZE = 22

GRAVITY_TIME_EVENT = pygame.USEREVENT+1
KEY_TIME_EVENT = pygame.USEREVENT+2

def start_game():
    global game_board
    global current_x_position
    global current_y_position
    global current_block_type
    global current_block_rotation
    global next_block_type
    global game_exit
    global new_round
    global game_over
    global gameDisplay
    global score
    session_bus = dbus.SessionBus()
    game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]
    current_x_position = 2
    current_y_position = 2
    current_block_type = random.randint(1, 7)
    current_block_rotation = 0
    next_block_type = random.randint(1, 7)
    game_exit = False
    new_round = False
    game_over = False
    gameDisplay = pygame.display.set_mode((380, 445))
    score = 0
    pygame.init()
    pygame.display.set_caption('Tetris')
    pygame.time.set_timer(GRAVITY_TIME_EVENT, 600)
    pygame.time.set_timer(KEY_TIME_EVENT, 60)
    global game_font
    game_font = pygame.font.SysFont("monospace", 18)

def clear_full_lines():
    global game_board
    global score
    removed_line_counter = 0
    for y in range(BOARD_Y_SIZE):
        brick_count = 0
        for x in range(BOARD_X_SIZE):
            if game_board[x][y] != 0:
                brick_count += 1
        if brick_count == BOARD_X_SIZE:
            remove_line(y)
            removed_line_counter += 1
    if removed_line_counter == 1:
        score += 1
    elif removed_line_counter  == 2:
        score += 4
    elif removed_line_counter == 3:
        score += 8
    elif removed_line_counter == 4:
        score += 16

def remove_line(line):
    global game_board
    for y in range(line, 0, -1):
        for x in range(BOARD_X_SIZE):
            game_board[x][y] = game_board[x][y-1]

def start_new_round():
    global game_board
    global current_x_position
    global current_y_position
    global current_block_type
    global current_block_rotation
    global next_block_type
    global new_round
    temp_block = block.get_block(current_block_type, current_block_rotation)
    for y in range(4):
        for x in range(4):
            if temp_block[x][y] != 0:
                game_board[current_x_position + x][current_y_position + y] = 8
    clear_full_lines()
    current_block_type = next_block_type
    next_block_type = random.randint(1, 7)
    current_block_rotation = 0
    current_x_position = 2
    current_y_position = 2
    new_round = True

def print_game_board():
    global game_font
    gameDisplay.fill((0,0,0))
    label = game_font.render("Next block:", 1, (255,255,255))
    gameDisplay.blit(label, (240, 25))
    label = game_font.render("Score:", 1, (255, 255, 255))
    gameDisplay.blit(label, (240, 112))
    label = game_font.render(str(score), 1, (255,255,255))
    gameDisplay.blit(label, (240, 132))
    pygame.draw.line(gameDisplay, (0, 0, 255), (20, 20), (20, 420), 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (20, 420), (220, 420), 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (220, 420), (220, 20), 1)
    temp_game_board = copy.deepcopy(game_board)
    temp_block = block.get_block(current_block_type, current_block_rotation)
    for y in range(4):
        for x in range(4):
            if temp_block[x][y] != 0:
                temp_game_board[current_x_position + x][current_y_position + y] = temp_block[x][y]
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            if temp_game_board[x][y] != 0 and y > 1:
                pygame.draw.rect(gameDisplay, (255, 0, 0), ((22*(x+1))-(x*2), (20*(y+1)-39), 18, 18), 0)
    temp_block = block.get_block(next_block_type, 0)
    for y in range(4):
        for x in range(4):
            if temp_block[x][y] != 0:
                pygame.draw.rect(gameDisplay, (255, 0, 0), ((225 + 22*(x+1))-(x*2), (20*(y+1) + 20), 18, 18), 0)
    if game_over == True:
        game_font = pygame.font.SysFont("monospace", 25)
        label = game_font.render("GAME OVER", 1, (255,255,255))
        gameDisplay.blit(label, (120, 120))
    pygame.display.update()

def try_to_place_block(action):
    global game_board
    global current_block
    global current_x_position
    global current_y_position
    global current_block_type
    global current_block_rotation
    global new_round
    global game_over
    temp_block_rotation = current_block_rotation + 1
    taken_places_count = 0

    #Preparing temporary game board to check is move possible. Forbbiten places marked with 9

    temp_game_board = [[0 for x in range(BOARD_Y_SIZE + 2)] for x in range(BOARD_X_SIZE + 4)]
    for y in range(BOARD_Y_SIZE + 2):
        for x in range(BOARD_X_SIZE + 4):
            if x < 2 or x > 11 or y > 21:
                temp_game_board[x][y] = 9

    #Copping actual game board and counting taken places

    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            temp_game_board[x+2][y] = game_board[x][y]
            if game_board[x][y] == 8:
                taken_places_count += 1

    #Placing block in place according to event

    if action == 1:
        temp_block = block.get_block(current_block_type, current_block_rotation)
        for y in range(4):
            for x in range(4):
                if temp_block[x][y] is not 0:
                    temp_game_board[x + current_x_position + 2][y + current_y_position + 1] = temp_block[x][y]
    elif action == 2:
        temp_block = block.get_block(current_block_type, current_block_rotation)
        for y in range(4):
            for x in range(4):
                if temp_block[x][y] is not 0:
                    temp_game_board[x + current_x_position + 3][y + current_y_position] = temp_block[x][y]
    elif action == 3:
        temp_block = block.get_block(current_block_type, current_block_rotation)
        for y in range(4):
            for x in range(4):
                if temp_block[x][y] is not 0:
                    temp_game_board[x + current_x_position + 1][y + current_y_position] = temp_block[x][y]
    elif action == 4:
        if temp_block_rotation > 3:
            temp_block_rotation = 0
        temp_block = block.get_block(current_block_type, temp_block_rotation)
        for y in range(4):
            for x in range(4):
                if temp_block[x][y] is not 0:
                    temp_game_board[x + current_x_position + 2][y + current_y_position] = temp_block[x][y]

    #Checking if performed move is correct
    
    temp_border_count = 0
    temp_taken_places_count = 0
    for y in range(BOARD_Y_SIZE + 2):
        for x in range(BOARD_X_SIZE + 4):
            if temp_game_board[x][y] == 9:
                temp_border_count += 1
            if temp_game_board[x][y] == 8:
                temp_taken_places_count += 1
    if temp_border_count == 116 and temp_taken_places_count == taken_places_count:

    #Taking apropiate actions

        if action == 1:
            new_round = False
            current_y_position += 1
        elif action == 2:
            current_x_position += 1
        elif action == 3:
            current_x_position -= 1
        elif action == 4:
            current_block_rotation = temp_block_rotation
    else:
        if action == 1:
            if new_round == True:
                game_over = True
            else:
                start_new_round()

start_game()

while game_exit == False and game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == GRAVITY_TIME_EVENT:
            try_to_place_block(1)
        if event.type == KEY_TIME_EVENT:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                try_to_place_block(1)
            if keys[pygame.K_RIGHT]:
                try_to_place_block(2)
            if keys[pygame.K_LEFT]:
                try_to_place_block(3)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                try_to_place_block(4)
            if event.key == pygame.K_ESCAPE:
                game_exit = True
    print_game_board()
    pygame.time.wait(30)

while game_exit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_exit = True
    pygame.time.wait(30)

pygame.quit()
quit()
