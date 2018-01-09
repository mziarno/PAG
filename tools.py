def createEdgeId(nodeID1, nodeID2):
    decID1 = [float(nodeID1)]
    decID2 = [float(nodeID2)]
    if decID1 >= decID2:
        return nodeID1 + nodeID2
    if decID1 <= decID2:
        return nodeID2 + nodeID1

