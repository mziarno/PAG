class Edge:
    def __init__(self, s_node, e_node):
        self.s = s_node
        self.e = e_node
        self.speed_lmt = 0
        self.surface_type = 'Aa'
        self.id = self.createID()

    def createID(self):
        id = self.s.id + self.e.id
        return id
