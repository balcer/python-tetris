from enum import Enum

class PxType(Enum):
    free = 0
    forrbidden = 1
    placed = 2
    moving = 3


class TetrisCore(object):

    BOARD_MARGIN = 2

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.game_board = [[0 for x in range(self.y_size + self.BOARD_MARGIN * 2)] for x in range(self.x_size + self.BOARD_MARGIN * 2)]

my_tetris = TetrisCore(10, 22)
