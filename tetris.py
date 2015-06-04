import sys
import time
import os
import Tkinter as tk

print "Tetris"

game_board = [[0 for x in range(22)] for x in range(14)]

game_board[5][2] = 3

def print_game_board():
    for y in range(22):
        for x in range(14):
            sys.stdout.write(str(game_board[x][y]))
        print ""

def init_game_board():
    for y in range(22):
        for x in range(14):
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
root.mainloop()
