import sys
import os
import json
import geopandas as gpd

def intersect_shp(input_shapefile, intersect_shapefile):
    try:
        # Read the input and intersect shapefiles
        gdf_input = gpd.read_file(input_shapefile)
        gdf_intersect = gpd.read_file(intersect_shapefile)

        # Perform the intersection operation
        gdf_intersected = gpd.overlay(gdf_input, gdf_intersect, how='intersection')

        # Construct output file names in the current directory
        output_shapefile = os.path.join(os.getcwd(), "intersected_shapefile.shp")
        output_geojson = os.path.join(os.getcwd(), "intersected_shapefile.geojson")
        output_csv = os.path.join(os.getcwd(), "intersected_shapefile.csv")

        # Save the intersected shapefile
        gdf_intersected.to_file(output_shapefile)

        # Save the intersected GeoJSON
        gdf_intersected.to_file(output_geojson, driver='GeoJSON')

        # Save the intersected CSV
        gdf_intersected.to_csv(output_csv, index=False)

        return output_shapefile, output_geojson, output_csv  # Return the paths to the output files

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None  # Indicate failure

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python intersect_shapefile.py <input_shapefile> <intersect_shapefile>")
        sys.exit(1)

    input_shapefile = sys.argv[1]
    intersect_shapefile = sys.argv[2]

    output_shapefile, output_geojson, output_csv = intersect_shp(input_shapefile, intersect_shapefile)

    if output_shapefile and output_geojson and output_csv:
        print(f"Shapefile successfully intersected and saved as {output_shapefile}.")
        print(f"GeoJSON successfully intersected and saved as {output_geojson}.")
        print(f"CSV successfully intersected and saved as {output_csv}.")
    else:
        print(json.dumps({"error": "Intersection failed"}))
