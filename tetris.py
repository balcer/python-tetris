import sys
import time
import os
import Tkinter as tk

print "Tetris"

BOARD_X_SIZE = 14
BOARD_Y_SIZE = 22

game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]
temp_game_board = [[0 for x in range(BOARD_Y_SIZE)] for x in range(BOARD_X_SIZE)]

I_block = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[2, 2, 3, 2, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
T_block = [[0, 2, 0],[2, 3, 2]]

def place_new_block():
    for y in range(5):
        for x in range(5):
            pass

def screen_update():
    print_game_board()
    root.after(2000, screen_update)

def print_game_board():
    os.system('clear')
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            sys.stdout.write(str(game_board[x][y]))
        print ""

def init_game_board():
    for y in range(BOARD_Y_SIZE):
        for x in range(BOARD_X_SIZE):
            if x == 0 or x == 1 or x == 12 or x == 13 or y == 20 or y == 21:
                game_board[x][y] = 1

def on_key_press(event):
    pressed_key = event.char
    if event.keysym == 'Escape':
        root.quit()
    text.insert('end', 'You pressed %s\n' % (event.char, ))

init_game_board()

root = tk.Tk()
root.geometry('400x300')
text = tk.Text(root)
text.pack()
root.bind('<Key>', on_key_press)
root.after(0, screen_update)
root.mainloop()
