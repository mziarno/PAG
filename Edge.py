from tools import createEdgeId
from tools import convertVelocity
from tools import findDistance

class Edge:
    def __init__(self, s_node, e_node, road_class):
        self.s = s_node
        self.e = e_node
        self.speed_lmt = self.checkLimit(road_class)
        self.id = createEdgeId(s_node, e_node)
        self.dist = self.distance()
        self.time = self.timeOfDist()


    def checkLimit(self, road_class):
        road_classes = {"A": 120, "S": 100, "GP": 90, "G": 90, "Z": 60, "L": 50, "D": 30, "I": 30}
        speed_lmt = convertVelocity(road_classes[road_class])
        return speed_lmt

    def timeOfDist(self):
        time = self.speed_lmt*self.dist
        return time




