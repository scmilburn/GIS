 ################ 
# Simon Milburn  #
# UID: 112385125 #
# GEOG376 - 0102 #
# lab03.py       #
# 2/12/15        #
 ################

# Practice with control of flow using if/elif/else branching in order to define and project files

import arcpy

source_path = "R:/376/Spring15/Lab03/lab03_data/"
work_path = "C:/Users/smilburn/Desktop/lab03_data/"
shapes = ["AK_tundra", "AK_taiga", "2004perimeters"] #list of the 3 incorrect 
arcpy.CopyFeatures_management(source_path + '2004_af.shp', work_path + '2004_af.shp') #copying 2004_af.shp seperately because not in loop
coord_system = arcpy.Describe(work_path + '2004_af.shp').spatialReference #getting the correct coordinate system

#PROJECTING
for x in shapes: #checking projection of 3 out of 4 shapefiles
    arcpy.CopyFeatures_management(source_path + x + '.shp', work_path + x + '.shp') #copying files from R: to C:

    if arcpy.Describe(work_path + x + '.shp').spatialReference.Name == "Unknown": #missing a projection
        arcpy.DefineProjection_management(work_path + x + '.shp', coord_system)
    else:
        arcpy.Project_management(work_path + x + '.shp', work_path + x + '_projected.shp', coord_system, "WGS_1984_(ITRF00)_To_NAD_1983")

#CLIPPING
arcpy.Clip_analysis(work_path + "2004_af.shp", work_path + "AK_taiga_projected.shp", work_path + "AK_taiga_clip1.shp")
result = arcpy.GetCount_management(work_path + "AK_taiga_clip1.shp")
taiga_count = int(result.getOutput(0))

arcpy.Clip_analysis(work_path + "2004_af.shp", work_path + "AK_tundra_projected.shp", work_path + "AK_tundra_clip1.shp")
result = arcpy.GetCount_management(work_path + "AK_tundra_clip1.shp")
tundra_count = int(result.getOutput(0))

result = arcpy.GetCount_management(work_path + "2004_af.shp")
total_af = int(result.getOutput(0))
result = arcpy.GetCount_management(work_path + "2004perimeters.shp")
total_scars = int(result.getOutput(0))
avg_fr_per_scars = total_af/total_scars

arcpy.Clip_analysis(work_path + "2004perimeters.shp", work_path + "AK_taiga_projected.shp", work_path + "AK_taiga_clip2.shp")
result = arcpy.GetCount_management(work_path + "AK_taiga_clip2.shp")
tundra_scarcount = int(result.getOutput(0))

arcpy.Clip_analysis(work_path + "2004perimeters.shp", work_path + "AK_tundra_projected.shp", work_path + "AK_tundra_clip2.shp")
result = arcpy.GetCount_management(work_path + "AK_tundra_clip2.shp")
taiga_scarcount = int(result.getOutput(0))

#OUTPUTS
print "How many active fires were detected in tundra?\n"
print str(tundra_count) + " active fires were detected in tundra during the summer of 2004\n"

print "How many active fires were detected in taiga?\n"
print str(taiga_count) + " active fires were detected in taiga during summer of 2004\n"

print "How many active fires per burn scar were detected on average in Interior Alaska?\n"
print str(avg_fr_per_scars) + " active fires per burn scar were detected on average in Interior Alaska in summer 2004\n"

print "How many active fires per burn scar were detected on average in tundra?\n"
print str(tundra_scarcount/total_scars) + " active fires per burn scar were detected on average in tundra in summer 2004\n"

print "How many active fires per burn scar were detected on average in taiga?\n"
print str(taiga_scarcount/total_scars) + " active fires per burn scar were detected on average in taiga in summer 2004\n"