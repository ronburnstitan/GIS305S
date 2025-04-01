import arcpy


def intersect(layer_list, output_path):
    # Intersect the buffer layers and save to the output path
    arcpy.Intersect_analysis(layer_list, output_path)


def buffer_layer(input_gdb, input_layer, dist):
    # Add units to the distance
    units = " miles"
    dist = dist + units
    # Create buffer output path
    output_layer = r"C:\Users\rburn\Documents\APPS305\APPS305\APPS305.gdb\\" + input_layer + "_buf"
    buf_layer = input_gdb + input_layer
    arcpy.Buffer_analysis(buf_layer, output_layer, dist, "FULL", "ROUND", "ALL")
    return output_layer


def main():
    # Define workspace
    workspace = r"C:\Users\rburn\Documents\APPS305\APPS305\APPS305.gdb\\"
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True

    # === GET PARAMETERS ===
    river_dist = arcpy.GetParameterAsText(0)          # Param 0: River Buffer Distance
    cities_dist = arcpy.GetParameterAsText(1)         # Param 1: Cities Buffer Distance
    intersect_lyr_name = arcpy.GetParameterAsText(2)  # Param 2: Intersect Layer Name (e.g., model3)

    # Input GDB for base data
    input_gdb = r"C:\Users\rburn\Documents\APPS305\Admin\Admin\AdminData.gdb\USA\\"

    # Buffer cities and rivers
    buf_cities = buffer_layer(input_gdb, "cities", cities_dist)
    arcpy.AddMessage("Buffer layer " + buf_cities + " created.")

    buf_rivers = buffer_layer(input_gdb, "us_rivers", river_dist)
    arcpy.AddMessage("Buffer layer " + buf_rivers + " created.")

    # Intersect both buffers
    lyr_list = [buf_rivers, buf_cities]
    output_intersect = workspace + intersect_lyr_name
    intersect(lyr_list, output_intersect)
    arcpy.AddMessage(f"New intersect layer created: {output_intersect}")

    # Add to current map
    aprx = arcpy.mp.ArcGISProject(r"C:\Users\rburn\Documents\APPS305\APPS305\APPS305.aprx")
    map_doc = aprx.listMaps()[0]
    map_doc.addDataFromPath(output_intersect)
    aprx.save()


if __name__ == '__main__':
    main()
