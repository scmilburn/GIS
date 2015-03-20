 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  # 
# lab01.py        #
# 1/29/2015       #
 #################

# This program utilizes dataset properties and prints to screen selected parameters

import arcpy #importing arcpy module

shp_path = "C:/Users/Simon Milburn/Desktop/lab01_data/wwf_terr_ecos.shp"
grid_path = "C:/Users/Simon Milburn/Desktop/lab01_data/forests_sa"

desc_shp = arcpy.Describe(shp_path) #description of the shapefile
desc_grid = arcpy.Describe(grid_path) #description of the grid

sr_shp = desc_shp.spatialReference #spatial reference for the shapefile
sr_grid = desc_grid.spatialReference #spatial reference for the grid

#Shapefile Description
print "Dataset properties: "
print "Dataset type: " + desc_shp.datasetType
print "Feature type: " + desc_shp.featureType
print "Shape type: " + desc_shp.shapeType
print "Projection name: {}{} ".format(sr_shp.PCSName, sr_shp.GCSName)
print "Dataset Extent: {}, {}, {}, {}\n\n".format(desc_shp.extent.XMin, 
desc_shp.extent.XMax, desc_shp.extent.YMin, desc_shp.extent.YMax)

#Grid Description
print "Dataset gridname properties: "
print "Dataset type: " + desc_grid.datasetType
print "Grid format: " + desc_grid.format
print "Number of bands: " + str(desc_grid.bandcount) #casting to a string because return type is an integer
print "Projection name: " + sr_grid.PCSName
print "Dataset extent: xmin {}, xmax {}, ymin {}, ymax {}".format(desc_grid.extent.XMin,
desc_grid.extent.XMax, desc_grid.extent.YMin, desc_grid.extent.YMax)
print "\n\nEnd of dataset description" #last line with two newlines
