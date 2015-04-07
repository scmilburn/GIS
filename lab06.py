 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  #
# lab06.py        #
# 4/2/2015        #
 #################

# The goal of this lab is to develop skills  to create and modify geoetries of geospatial data

import arcpy

source = "R:/376/Spring15/Lab06/lab06_data/"
path = "C:/Users/smilburn/Desktop/lab06_data/"

size = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
feature_info = []

for x in size:
	for y in size:
		feature_info.append[x,y]

grid = []
for feature in feature_info:
	grid.append(
		arcpy.Polygon(
			arcpy.Array([arcpy.Point(*coords) for coords in feature])))

sp = arcpy.Describe(path + "world.shp").spatialReference
gcs = sp.GCSName

#DEFINING PROJECTION BASED OFF OF world.shp
arcpy.DefineProjection_management(grid, gcs)

#ADDING UID Field
arcpy.AddField_management(grid, "UID", int)

#Populating field with unique identifiers 



