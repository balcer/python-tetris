import time


class block:

    def get_block(type, rotation):
        if type == 1:
            return [[0, 0, 0, 0],[0, 2, 2, 0],[0, 2, 2, 0],[0, 0, 0, 0]]
        if type == 2:
            if rotation == 0 or rotation == 2:
                return [[0, 2, 0, 0],[0, 2, 0, 0],[0, 2, 0, 0],[0, 2, 0, 0]]
            else:
                return [[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 2],[0, 0, 0, 0]]
        if type == 3:
            if rotation == 0 or rotation == 2:
                return [[0, 0, 0, 0],[0, 0, 2, 0],[0, 2, 2, 0],[0, 2, 0, 0]]
            else:
                return [[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 0, 0],[0, 2, 2, 0]]
        if type == 4:
            if rotation == 0 or rotation == 2:
                return [[0, 0, 0, 0],[0, 2, 0, 0],[0, 2, 2 ,0],[0, 0, 2, 0]]
            else:
                return [[0, 0, 0, 0],[0, 0, 0, 0],[0, 2, 2, 0],[2, 2, 0, 0]]
        if type == 5:
            if rotation == 0:
                return [[0, 0, 0, 0],[0, 2, 2, 0],[0, 2, 0, 0],[0, 2, 0, 0]]
            elif rotation == 1:
                return [[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 0],[0, 0, 2, 0]]
            elif rotation == 2:
                return [[0, 0, 0, 0],[0, 2, 0, 0],[0, 2, 0, 0],[2, 2, 0, 0]]
            else:
                return [[0, 0, 0, 0],[2, 0, 0, 0],[2, 2, 2, 0],[0, 0, 0, 0]]
        if type == 6:
            if rotation == 0:
                return [[0, 0, 0, 0],[0, 2, 0, 0],[0, 2, 0, 0],[0, 2, 2, 0]]
            elif rotation == 1:
                return [[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 0],[2, 0, 0, 0]]
            elif rotation == 2:
                return [[0, 0, 0, 0],[2, 2, 0, 0],[0, 2, 0, 0],[0, 2, 0, 0]]
            else:
                return [[0 ,0 ,0 ,0],[0, 0, 2, 0],[2, 2, 2, 0],[0, 0, 0, 0]]
        if type == 7:
            if rotation == 0:
                return [[0, 0, 0, 0],[0, 2, 0, 0],[0, 2, 2, 0],[0, 2, 0, 0]]
            elif rotation == 1:
                return [[0, 0, 0, 0],[0, 0, 0, 0],[2, 2, 2, 0],[0, 2, 0, 0]]
            elif rotation == 2:
                return [[0, 0, 0, 0],[0, 2, 0, 0],[2, 2, 0, 0],[0, 2, 0, 0]]
            else:
                return [[0, 0, 0, 0],[0, 2, 0, 0],[2, 2, 2, 0],[0, 0, 0, 0]]
