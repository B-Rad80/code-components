#queryShapefiles.py

import fiona
import shapely
import pprint


# got this code from here: 
# https://stackoverflow.com/questions/7861196/check-if-a-geopoint-with-latitude-and-longitude-is-within-a-shapefile
# holy wow this fiona conda install is taking some time... it's worrisome...

# THIS METHOD assumes MULTIPLE POLYGONS in a shapefile
import shapefile
from shapely.geometry import point # Point class
from shapely.geometry import shape # shape() is a function to convert geo objects through the interface
from fiona import collection

from fiona.crs import from_string

#from shapely.geometry import point # Point class
#from shapely import geometry # shape() is a function to convert geo objects through the interface

box = fiona.open('brac.shp')
print(box.driver)
print(box)
pprint.pprint(box[1])
#print(len(box))

#for feat in fiona.open("brac.shp"):
#    print(feat.keys())

with fiona.open("brac.shp") as fiona_collection:
	# apparently the syntax below has been depreciated in favor of the following
    #shapefile_record = fiona_collection.next()
    shapefile_record = next(iter(fiona_collection))
    # Use Shapely to create the polygon
    # IT SEEMS asShape might be depreciated but has been replaced with Polygon (or polygon will work)
    shape = shapely.geometry.asShape( shapefile_record['geometry'] )

    point = shapely.geometry.Point(-65.686699, 18.212605) # longitude, latitude

    # Alternative: if point.within(shape)
    if shape.contains(point):
        print("Found shape for point.")
    else:
    	print("No dice Charlie.")