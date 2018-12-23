#convert.py

#taken from: https://gist.github.com/jwass/6245313

import fiona
import fiona.crs

"""
def convert(f_in, f_out):
   # with fiona.open(f_in) as source:
		with fiona.open(
				f_out,
				'w',
				driver='GeoJSON',
				crs = fiona.crs.from_epsg(4326),
				schema=source.schema) as sink:

			for rec in source:
				sink.write(rec)
"""
with fiona.open('brac.shp') as source:
	with fiona.open(
				'brac.geojson',
				'w',
				driver='GeoJSON',
				crs = fiona.crs.from_epsg(4326),
				schema=source.schema) as sink:

			for rec in source:
				sink.write(rec)