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
sr = arcpy.SpatialReference(4326)

for y in years:
	for m in months:
		fire = "%d%02d_rfe.shp" % (y,m)
		fire_path = path + fire
		arcpy.CopyFeatures_management(source + fire, fire_path) #copying files
                
		fire_path_list.append(fire_path) #adding to list
		arcpy.DefineProjection_management(fire_path, sr) #defining projection for files

# MERGED INTO ONE
arcpy.Merge_management(fire_path_list, path + "merged.shp")

total = int((arcpy.GetCount_management(path + "merged.shp")).getOutput(0))

#Merge layer
arcpy.MakeFeatureLayer_management(path + "merged.shp", "merge_lyr")

low = ["0", "60", "86"]
up = ["59", "85", "100"]

for i in range(0,3):
        exp = '("Conf" >= ' + low[i] + ') AND ("Conf" <= ' + up[i] + ')'
        arcpy.SelectLayerByAttribute_management("merge_lyr", "", exp)
        ct = float((arcpy.GetCount_management("merge_lyr")).getOutput(0))
        percent = int(round((ct/total)*100))
        print "In 2007, %d percent of fires were detected in %s to %s confidence interval.\n" % (percent, low[i], up[i])

print "DONE PROCESSING\n"
