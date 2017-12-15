class Node:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.id = self.createID()
        self.neighbours = []

    def createID(self):
        id = str(self.x) + str(self.y)
        id = id.translate(None, '.')
        return id
