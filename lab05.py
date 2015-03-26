 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  #
# lab05.py        #
# 3/21/2015       #
 #################

# This program practices loops to process datasets

import arcpy

source = "R:/376/Spring15/Lab05/lab05_data/"
path = "C:/Users/smilburn/Desktop/lab05_data/"

years = [2007]
months = range(1,13)

fire_path_list = []
sr = arcpy.SpatialReference(4326) #GCS_WGS_1984 projection

for y in years:
	for m in months:
		fire = "%d%02d_rfe.shp" % (y,m)
		fire_path = path + fire

		#copying files
		#arcpy.CopyFeatures_management(source + fire, fire_path)
		#defining projection for files
		arcpy.DefineProjection_management(fire_path, sr)
		#adding to list
		fire_path_list.append(fire_path)

# Merging monthly fire shapefiles into one
arcpy.Merge_management(fire_path_list, path + "merged.shp")

upper = arcpy.SearchCursor(path + "merged.shp", '"Conf" > 85')
middle = arcpy.SearchCursor(path + "merged.shp", '60 <= "Conf" AND "Conf" <= 85')
lower = arcpy.SearchCursor(path + "merged.shp", '"Conf" < 60')

total = int((arcpy.GetCount_management(merged)).getOutput(0))
upcount = int((arcpy.GetCount_management(upper)).getOutput(0))
midcount = int((arcpy.GetCount_management(middle)).getOutput(0))
lowcount = int((arcpy.GetCount_management(lower)).getOutput(0))

print "In 2007, %d percent of fires were detected with over 85 confidence interval.\n" % (round(upcount/total))
print "In 2007, %d percent of fires were detected within 60 to 85 confidence range.\n" % (round(midcount/total))
print "In 2007, %d percent of fires were detected with below 60 confidence interval.\n" % (round(lowcount/total))
print "DONE PROCESSING\n"
