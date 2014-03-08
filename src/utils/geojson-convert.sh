# Bulk convert shapefiles to geojson using ogr2ogr

#geojson conversion
function shp2geojson() {
  ogr2ogr -f GeoJSON -t_srs crs:84 "$1.geojson" "$1.shp"
}
 
#convert all shapefiles
for var in *.shp; do shp2geojson ${var%\.*}; done
 
