 ################
# Simon Milburn  #
# UID: 112385125 #
# GEOG376 - 0102 #
# lab02.py       #
# 2/5/2015       #
 ################

# This program automatically creates buffers, clips fire data to the
# new buffers, and counts the fire points within each buffer

import arcpy
from random import randint

feature_names = ["roads", "utilities", "urban", "railroad"] # list of shapefile names that will be processed
months = ["January: ", "February: ", "March: ", "April: ", "May: ", "June: ",
          "July: ", "August: ", "September: ", "October: ", "November: ", "December: "]

print "Start of processing\n"

for x in feature_names: # iterates through the possible filenames    
    path = "/Users/Simon/Desktop/lab02_data/" + x + ".shp" 
    
    print "Processing " + x.capitalize() + ' buffer...\n' # buffer status update
    buffer_out = "/Users/Simon/Desktop/out/buffer_" + x + ".shp" # buffer output path
    arcpy.Buffer_analysis(path, buffer_out, "1000 Meters")

    random = str(randint(1,12)) # generating random int to determine month
    if (len(random) == 1): # if single digit random int is generated, add a 0 to front
        random  = "0" + random
        
    print "Clipping fire data to " + x.capitalize() + ' buffer...\n' # clip status update
    fire_pts = "/Users/Simon/Desktop/lab02_data/2007_" + random + "ignitions.shp" # fire points path
    clip_out = "/Users/Simon/Desktop/out/clip_" + x + ".shp" # clip output path 
    arcpy.Clip_analysis(fire_pts, buffer_out, clip_out) 

    result = arcpy.GetCount_management(path)
    count = int(result.getOutput(0))
    print months[int(random)] + str(count) + " fire ignitions in the 1 km buffer of " + x
    
print "End of processing\n"
