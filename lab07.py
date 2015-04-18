 #################
# Simon Milburn   #
# UID: 112385125  #
# GEOG376 - 0102  #
# lab07.py        #
# 4/14/2015       #
 #################

# The goal of this lab is to develop proficiency in using cursor objects 
# for aspect of geospatial relationship analysis

import arcpy

path = "C:/Users/smilburn/Desktop/lab07_data/"

arcpy.CalculateAreas_stats(path + "ten_deg_grid.shp", path + "f_area.shp")

arcpy.AddField_management(path + "f_area.shp", "lat", "DOUBLE")
arcpy.AddField_management(path + "f_area.shp", "lon", "DOUBLE")
arcpy.AddField_management(path + "f_area.shp", "Percentage", "DOUBLE")

cursor = arcpy.UpdateCursor(path + "f_area.shp")

for row in cursor:
    centroid = row.shape.centroid
    row.lat = centroid.Y
    row.lon = centroid.X
    cursor.updateRow(row)
del row
del cursor

arcpy.AddField_management(path + "f_area.shp", "land", "DOUBLE")

search_cursor = arcpy.SearchCursor(path + "world_ten_deg_area.shp", fields="UID; Land_fr")

for sc in search_cursor:
    #grab land fractioon and uid world ten
    #takes over to grid
    exp = '"UID" = %s' % sc.UID
    cursor = arcpy.UpdateCursor(path + "f_area.shp")
    for r in cursor:
        if sc.UID == r.UID:
            r.land = sc.Land_fr
            r.Percentage = (sc.Land_fr/r.F_AREA)
            cursor.updateRow(r)

del sc
del search_cursor
del r
del cursor

print "done"
