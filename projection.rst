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
	dataset = driver.Open(r'c:\data\yourshpfile.shp')
	
	# from Layer
	layer = dataset.GetLayer()
	spatialRef = layer.GetSpatialRef() 
	# from Geometry
	feature = layer.GetNextFeature()
	geom = feature.GetGeometryRef()
	spatialRef = geom.GetSpatialReference() 


Project a Geometry
------------------

.. code-block:: python

	from osgeo import ogr, osr

	driver = ogr.GetDriverByName('ESRI Shapefile')

	# input SpatialReference
	inSpatialRef = osr.SpatialReference()
	inSpatialRef.ImportFromEPSG(4269)

	# output SpatialReference
	outSpatialRef = osr.SpatialReference()
	outSpatialRef.ImportFromEPSG(26912)

	# create the CoordinateTransformation
	coordTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

	inDataSet = driver.Open(r'c:\data\in_yourshpfile.shp')
	inLayer = inDataSet.GetLayer()

	outDataSet = driver.Open(r'c:\data\out_yourshpfile.shp')
	outLayer = outDataSet.GetLayer()

	# loop through the input features
	inFeature = inLayer.GetNextFeature()
	while inFeature:
	# get the input geometry
	geom = inFeature.GetGeometryRef()
	# reproject the geometry
	geom.Transform(coordTrans)
	# create a new feature
	outFeature = ogr.Feature(featureDefn)
	# set the geometry and attribute
	outFeature.SetGeometry(geom)
	outFeature.SetField('name', inFeature.GetField('name'))
	# add the feature to the shapefile
	outLayer.CreateFeature(outFeature)
	# destroy the features and get the next input feature
	outFeature.Destroy
	inFeature.Destroy
	inFeature = inLayer.GetNextFeature()

	# close the shapefiles
	inDataSet.Destroy()
	outDataSet.Destroy()
	

Export Projection
-----------------

.. code-block:: python

	from osgeo import ogr, osr
	driver = ogr.GetDriverByName('ESRI Shapefile')
	dataset = driver.Open(r'c:\data\yourshpfile.shp')
	layer = dataset.GetLayer()
	spatialRef = layer.GetSpatialRef() 
	
	spatialRef.ExportToWkt()
	spatialRef.ExportToPrettyWkt()
	spatialRef.ExportToPCI()
	spatialRef.ExportToUSGS()
	spatialRef.ExportToXML()
	
	











