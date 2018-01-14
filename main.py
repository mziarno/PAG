import arcpy
import os

from AStar import Astar
from Node import Node
from Edge import Edge
from tools import createEdgeId

arcpy.CheckOutExtension("spatial")

# udostepniam dostep do danych dla innych
path = os.path.dirname(os.path.abspath(__file__))
arcpy.env.workspace = path

arcpy.env.overwriteOutput = True

# slownik z wezlami
nodes = {}
prev_id = ""
edges = {}

with open("Output_points.txt") as f:

    for line in f:
        if line == "Next polyline\n":
            prev_id = ""
            continue
        list_coord = line.split(" ")
        pointX = float(list_coord[0])
        pointY = float(list_coord[1])
        road_class = str(list_coord[2])
        road_class = road_class.replace("\n", "")
        direct = int(list_coord[3])
        node = Node(pointX, pointY)
        if node.id not in nodes:
            nodes[node.id] = node

# przypisywanie sasiadow

        if prev_id != "":
            if direct == 0:
                nodes[node.id].neighbours.append(prev_id)
                nodes[prev_id].neighbours.append(node.id)
            elif direct == 1:
                nodes[prev_id].neighbours.append(node.id)
            elif direct == 2:
                nodes[node.id].neighbours.append(prev_id)
            # elif direct == 3

            edge = Edge(prev_id, node.id, road_class, nodes )

            if edge.id not in edges:
                edges[edge.id] = edge
        prev_id = node.id

# korki

edges[createEdgeId('4748663157196187', '475007657208723')].traffic = 230
edges[createEdgeId('4750264757210177', '4751250357218008')].traffic = 230
edges[createEdgeId('4752339257226212', '4752929857230758')].traffic = 230


path = Astar(nodes, edges, "480564555748327", "4754340256999086")

pathPoints = []

for pointId in path:
    node = nodes[pointId]
    pathPoints.append(arcpy.Point(node.x, node.y))

    startPoint = pathPoints[-1]
    endPoint = pathPoints[0]


result = arcpy.Polyline(arcpy.Array(pathPoints))
result2 = arcpy.PointGeometry(startPoint)
result3 = arcpy.PointGeometry(endPoint)

arcpy.CopyFeatures_management(result, "TRASA.shp")
arcpy.CopyFeatures_management(result2, "START.shp")
arcpy.CopyFeatures_management(result3, "END.shp")






