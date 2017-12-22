from tools import createEdgeId

class Edge:
    def __init__(self, s_node, e_node, road_class):
        self.s = s_node
        self.e = e_node
        self.speed_lmt = self.checkLimit(road_class)
        self.id = createEdgeId(s_node, e_node)

    def checkLimit(self, road_class):
        road_classes = {"A": 120, "S": 100, "GP": 90, "G": 90, "Z": 60, "L": 50, "D": 30, "I": 30}
        speed_lmt = road_classes[road_class]
        return speed_lmt




