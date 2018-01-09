from cmath import sqrt

def createEdgeId(nodeID1, nodeID2):
    decID1 = [float(nodeID1)]
    decID2 = [float(nodeID2)]
    if decID1 >= decID2:
        return nodeID1 + nodeID2
    if decID1 <= decID2:
        return nodeID2 + nodeID1

def convertVelocity(kmh):
    return kmh / 3.6

def findDistance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    d = sqrt(x**2 + y**2).real
    return d
