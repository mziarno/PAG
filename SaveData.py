import arcpy
import os
from Node import Node

arcpy.CheckOutExtension("spatial")

# udostepniam dostep do danych dla innych
path = os.path.dirname(os.path.abspath(__file__))
arcpy.env.workspace = path

arcpy.env.overwriteOutput = True

# wczytuje warstwe i dodaje do obiektu
polylines = arcpy.CopyFeatures_management("Dane/miasto/L4_1_BDOT10k__OT_SKDR_L.shp", arcpy.Geometry())

with open("Output_points.txt", "w+") as text_file:

# przegladamy punkty, z ktorych skladaja sie linie
    for polyline in polylines:
        points = polyline.getPart(0)
        is_first = True
        prev_node = 0


        text_file.write("Next polyline\n")

    # wczytuje wspolrzedne punktow
        for point in points:
            text_file.write(str(point.X) + " " + str(point.Y) + "\n")




