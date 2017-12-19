class Node:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.id = self.createID()
        self.neighbours = []
        self.f = 99999999999
        self.g = 0
        self.h = 0
        self.parent = ""

    def createID(self):
        id = str(self.x) + str(self.y)
        id = id.translate(None, '.')
        return id
