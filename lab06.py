 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  #
# lab06.py        #
# 4/2/2015        #
 #################

# The goal of this lab is to develop skills to create and modify geometries of geospatial data

import arcpy

print "imported"

#Setting up path variables
path = "C:/Users/smilburn/Desktop/lab06_data/"

#range of northern hemisphere
lat = range(0,90,10)
lon = range(-180,180,10)

grid = []

#creating polygon list
for y in lat:
    for x in lon:
        arr = []

        p1 = arcpy.Point(x, y)
        p2 = arcpy.Point(x+10, y)
        p3 = arcpy.Point(x, y+10)
        p4 = arcpy.Point(x+10, y+10)

        arr.append(p3)
        arr.append(p4)
        arr.append(p2)
        arr.append(p1)
        
        grid.append(arcpy.Polygon(arcpy.Array(arr)))
print "done for"

#making polylist into .shp
arcpy.CopyFeatures_management(grid, path + "grid.shp")
print "made grid.shp"

#DEFINING PROJECTION BASED OFF OF world.shp
arcpy.DefineProjection_management(path + "grid.shp", 4326)

#ADDING UID Field and populating with unique ids 
arcpy.AddField_management(path + "grid.shp", "UID", "LONG")
arcpy.CalculateField_management(path + "grid.shp", "UID", "!FID! + 1", "PYTHON")

#Intersecting shapes and getting areas
arcpy.Intersect_analysis([path + "grid.shp", path + "world.shp"], path + "intersect.shp")
arcpy.Dissolve_management()
arcpy.CalculateAreas_stats(path + "dissolved.shp", path + "dissolved_farea.shp")
