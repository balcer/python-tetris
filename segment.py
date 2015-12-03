class Segment:

    def __init__(self, addr):
        self.addr = addr
        self.content = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def set(self, valueList = []):
        self.content = list(valueList)
