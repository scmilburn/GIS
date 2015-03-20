 ################ 
# Simon Milburn  #
# UID: 112385125 #
# GEOG376 - 0102 #
# lab04.py       #
# 2/26/15        #
 ################

# Practice with creative use of strings in developing queries and subsetting data

import arcpy

source = "R:/376/Spring15/Lab04/lab04_data/line_features.shp"
path = "C:/Users/smilburn/Desktop/lab04_data/"
parent_path = path + "line_features.shp" #path of main shapefile

arcpy.CopyFeatures_management(source, parent_path) #copying over shapefile in my directory

#SELECTING BASED ON SOURCETHM
arcpy.Select_analysis(parent_path, path + "CA_roads.shp", " \"SOURCETHM\" LIKE 'Cardlines'")
arcpy.Select_analysis(parent_path, path + "CA_railroads.shp"," \"SOURCETHM\" LIKE 'Carrlines'" )
arcpy.Select_analysis(parent_path, path + "AZ_roads.shp", " \"SOURCETHM\" LIKE 'Azrdlines'")
arcpy.Select_analysis(parent_path, path + "AZ_railroads.shp", " \"SOURCETHM\" LIKE 'Azrrlines'")

#GETTING RECORD COUNT
result = arcpy.GetCount_management(path + "AZ_roads.shp")
AZ_rd = int(result.getOutput(0))
result = arcpy.GetCount_management(path + "AZ_railroads.shp")
AZ_rr = int(result.getOutput(0))
result = arcpy.GetCount_management(path + "CA_roads.shp")
CA_rd = int(result.getOutput(0))
result = arcpy.GetCount_management(path + "CA_railroads.shp")
CA_rr = int(result.getOutput(0))

#PRINTING RECORD COUNTgh
print "There are {AZ_rd} number of records for roads in Arizona\n".format(AZ_rd=AZ_rd)
print "There are {AZ_rr} number of records for railroads in Arizona\n".format(AZ_rr=AZ_rr)
print "There are {CA_rd} number of records for roads in California\n".format(CA_rd=CA_rd)
print "There are {CA_rr} number of records for railroads in California\n".format(CA_rr=CA_rr)