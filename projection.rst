Projection
==========

Create Projection
-----------------

.. code-block:: python


	from osgeo import osr
	spatialRef = osr.SpatialReference()
	spatialRef.ImportFromEPSG(2927) 	# from EPSG

Reproject a Geometry
--------------------

.. code-block:: python

    from osgeo import ogr
    from osgeo import osr

    source = osr.SpatialReference()
    source.ImportFromEPSG(2927)

    target = osr.SpatialReference()
    target.ImportFromEPSG(4326)

    transform = osr.CoordinateTransformation(source, target)

    point = ogr.CreateGeometryFromWkt("POINT (1120351.57 741921.42)")
    point.Transform(transform)

    print point.ExportToWkt()

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


Reproject a Layer
-----------------

.. code-block:: python

    import os
    from osgeo import ogr, osr
    
    # return more informative errors
    ogr.UseExceptions()

    # parameters
    inputShapefile = r'c:\data\spatial\basemap.shp'
    outputShapefile = r'c:\data\spatial\basemap_4326.shp'
    outLayerName = 'basemap_4326'
    
    driver = ogr.GetDriverByName('ESRI Shapefile')

    # input SpatialReference
    inSpatialRef = osr.SpatialReference()
    inSpatialRef.ImportFromEPSG(2927)

    # output SpatialReference
    outSpatialRef = osr.SpatialReference()
    outSpatialRef.ImportFromEPSG(4326)

    # create the CoordinateTransformation
    coordTrans = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

    # get the input layer
    inDataSet = driver.Open(inputShapefile)
    inLayer = inDataSet.GetLayer()

    # create the output layer
    if os.path.exists(outputShapefile):
        driver.DeleteDataSource(outputShapefile)
    outDataSet = driver.CreateDataSource(outputShapefile)
    outLayer = outDataSet.CreateLayer(outLayerName, geom_type=ogr.wkbMultiPolygon)

    # add fields
    inLayerDefn = inLayer.GetLayerDefn()
    for i in range(0, inLayerDefn.GetFieldCount()):
        fieldDefn = inLayerDefn.GetFieldDefn(i)
        outLayer.CreateField(fieldDefn)

    # get the output layer's feature definition
    outLayerDefn = outLayer.GetLayerDefn()

    # loop through the input features
    inFeature = inLayer.GetNextFeature()
    while inFeature:
        # get the input geometry
        geom = inFeature.GetGeometryRef()
        # reproject the geometry
        geom.Transform(coordTrans)
        # create a new feature
        outFeature = ogr.Feature(outLayerDefn)
        # set the geometry and attribute
        outFeature.SetGeometry(geom)
        for i in range(0, outLayerDefn.GetFieldCount()):
            outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
        # add the feature to the shapefile
        outLayer.CreateFeature(outFeature)
        # dereference the features and get the next input feature
        outFeature = None
        inFeature = inLayer.GetNextFeature()

    # Save and close the shapefiles
    inDataSet = None
    outDataSet = None

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
	
	
Create an ESRI.prj file
-----------------------

.. code-block:: python

	from osgeo import ogr, osr

	spatialRef = osr.SpatialReference()
	spatialRef.ImportFromEPSG(26912)

	spatialRef.MorphToESRI()
	file = open('yourshpfile.prj', 'w')
	file.write(spatialRef.ExportToWkt())
	file.close()







