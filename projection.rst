Projection
==========

Create Projection
-----------------

.. code-block:: python


	from osgeo import osr
	spatialRef = osr.SpatialReference()
	spatialRef.ImportFromEPSG(2927) 	# from EPSG

	

Get Projection
--------------

.. code-block:: python

	from osgeo import ogr, osr
	driver = ogr.GetDriverByName('ESRI Shapefile')
	ds = driver.Open(r'c:\data\yourshpfile.shp')
	# from Layer
	layer = ds.GetLayer()
	spatialRef = layer.GetSpatialRef() 
	# from Geometry
	feature = layer.GetNextFeature()
	geom = feature.GetGeometryRef()
	spatialRef = geom.GetSpatialReference() 