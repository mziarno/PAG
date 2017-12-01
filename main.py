import arcpy
import os

arcpy.CheckOutExtension("spatial")

#udostepniam dostep do danych dla innych
path = os.path.dirname(os.path.abspath(__file__))
arcpy.env.workspace = path

arcpy.env.overwriteOutput = True

#wczytuje warstwe i dodaje do obiektu
polylines = arcpy.CopyFeatures_management("Dane/miasto/L4_1_BDOT10k__OT_SKDR_L.shp", arcpy.Geometry())

#przegladamy punkty, z ktorych skladaja sie linie
for polyline in polylines:
    points = polyline.getPart(0)

#wczytuje wspolrzedne punktow
    for point in points:
        point.X
        point.Y

        print point.X

