cwlVersion: v1.2
class: CommandLineTool
 
hints:
  DockerRequirement:
    dockerPull: "eforoutan/intersect_shp:latest"
  NetworkAccess:
    networkAccess: true
 
inputs:
  input_shapefile:
    type: Directory
    inputBinding:
      position: 1
 
  intersect_shapefile:
    type: Directory
    inputBinding:
      position: 2

outputs:

  # clipped_shp:
  #   type: Directory  
  #   outputBinding:
  #     glob: "intersected_shapefile"

  intersect_GeoJSON:
    type: File  
    outputBinding:
      glob: "intersected_shapefile.geojson"

  intersect_csv:
    type: File  
    outputBinding:
      glob: "intersected_shapefile.csv"