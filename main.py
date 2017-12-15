import arcpy
import os
from Node import Node

arcpy.CheckOutExtension("spatial")

# udostepniam dostep do danych dla innych
path = os.path.dirname(os.path.abspath(__file__))
arcpy.env.workspace = path


arcpy.env.overwriteOutput = True

# slownik z wezlami
nodes = {}
prev_id = ""

with open("Output_points.txt") as f:

    for line in f:
        if line == "Next polyline\n":
            prev_id = ""
            continue
        list_coord = line.split(" ")
        pointX = float(list_coord[0])
        pointY = float(list_coord[1])
        node = Node(pointX, pointY )
        nodes[node.id] = node

# przypisywanie sasiadow
        if prev_id != "":
            node.neighbours.append(prev_id)
            nodes[prev_id].neighbours.append(node.id)

        prev_id = node.id

        print node.id
