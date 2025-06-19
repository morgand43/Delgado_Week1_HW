#### Homework Assignment # 1

import arcpy
arcpy.env.overwriteOutput = True

# Set the workspace environment setting
arcpy.env.workspace = r"C:\GIS4085- PythonII\Week 1\GIS4085_Week1_Data\Week1-homework.gdb"

# Create a selection of counties
    #arcpy.analysis.Select(in_features, out_feature_class, {where_clause})
where_clause = "NAME20 IN ('Adams', 'Arapahoe', 'Broomfield', 'Denver', 'Douglas', 'Jefferson')"
cnty_sel= arcpy.analysis.Select("ColoradoCounties", "in_memory/temp_output", where_clause)

# Set up datasets to clip

in_data = ["Blocks2020", "BlockGroups2020"]

# Loop through both layers to clip them to the correct counties

for layer in in_data:
    arcpy.analysis.PairwiseClip(layer, cnty_sel, f"{layer}_Clip")

print ("analysis complete")

#clean up

arcpy.Delete_management("temp_output")
