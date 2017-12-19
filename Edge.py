from tools import createEdgeId

class Edge:
    def __init__(self, s_node, e_node):
        self.s = s_node
        self.e = e_node
        self.speed_lmt = 0
        self.road_class = 'D'
        self.id = createEdgeId(s_node, e_node)


