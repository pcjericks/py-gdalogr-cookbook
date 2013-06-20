Layers
=============

Is Ogr Installed
----------------

.. code-block:: python

    try:
      from osgeo import ogr
      print 'Import of ogr from osgeo worked.  Hurray!\n'
    except:
      print 'Import of ogr from osgeo failed\n\n'

View Auto Generated Ogr Help
------------------------------      
    This code simply prints out the auto-generated help on the imported module.  In this case it's OGR.

.. code-block:: python
    
    import osgeo.ogr
    print help(osgeo.ogr)

Get List of Ogr Drivers Alphabetically (A- Z)
-------------------------------------

    It's always driven me a little nuts that the command line ogr2ogr --formats returns a 'random' list of drivers.  This code returns the list of OGR drivers alphabetically from A - Z.  .  
   
.. code-block:: python

    import ogr
    cnt = ogr.GetDriverCount()
    formatsList = []  # Empty List

    for i in range(cnt):
        driver = ogr.GetDriver(i)
        driverName = driver.GetName()
        if not driverName in formatsList:
            formatsList.append(driverName)

    formatsList.sort() # Sorting the messy list of ogr drivers 

    for i in formatsList:
        print i
     
Is Ogr Driver Available by Driver Name
------------------------------      
    This code shows if a particular OGR driver is available.  The exact names are the ones used on the OGR Vector Formats page in the "Code" column  ([`web site <http://www.gdal.org/ogr/ogr_formats.html>`_]).  This is the same names returned when you enter ``ogrinfo --formats`` on the command line.  
    
    Code Example Source: [`web site <http://www.gdal.org/ogr/ogr_apitut.html>`_]
    
.. code-block:: python
    
    from osgeo import ogr
    
    ## Shapefile available?
    driverName = "ESRI Shapefile"
    drv = ogr.GetDriverByName( driverName )
    if drv is None:
        print "%s driver not available.\n" % driverName
    else:
        print  "%s driver IS available.\n" % driverName
        
    ## PostgreSQL available?
    driverName = "PostgreSQL"
    drv = ogr.GetDriverByName( driverName )
    if drv is None:
        print "%s driver not available.\n" % driverName
    else:
        print  "%s driver IS available.\n" % driverName
        
    ## Is File GeoDatabase available?
    driverName = "FileGDB"
    drv = ogr.GetDriverByName( driverName )
    if drv is None:
        print "%s driver not available.\n" % driverName
    else:
        print  "%s driver IS available.\n" % driverName
        
    ## SDE available?
    driverName = "SDE"
    drv = ogr.GetDriverByName( driverName )
    if drv is None:
        print "%s driver not available.\n" % driverName
    else:
        print  "%s driver IS available.\n" % driverName
        
        
Get Shapefile Feature Count
---------------------------
    This code example opens a shapefile and returns the number of features in it.  Solution mined from: [`web site <http://www.gis.usu.edu/~chrisg/python/2009/lectures/ospy_slides1.pdf>`_] 



.. code-block:: python

    import os
    from osgeo import ogr

    daShapefile = r"C:\Temp\Voting_Centers_and_Ballot_Sites.shp"

    driver = ogr.GetDriverByName('ESRI Shapefile')

    dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

    # Check to see if shapefile is found.
    if dataSource is None:
        print 'Could not open %s' % (daShapefile)
    else:
        print 'Opened %s' % (daShapefile)
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()  
        print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)

        
    
Get All PostGIS layers in a PostgreSQL Database
---------------------------------------------

    This returns all the layers in a database of your choosing sorted in alphabetical order (of course).  Just fill in the missing information and it should work.  
    
.. code-block:: python

    from osgeo import ogr

    databaseServer = "<IP of database server OR Name of database server"
    databaseName = "<Name of database>"
    databaseUser = "<User name>"
    databasePW = "<User password>"


    connString = "PG: host=%s dbname=%s user=%s password=%s" %(databaseServer,databaseName,databaseUser,databasePW)

    conn = ogr.Open(connString)

    layerList = []
    for i in conn:
        daLayer = i.GetName()
        if not daLayer in layerList:
            layerList.append(daLayer)

    layerList.sort()

    for j in layerList:
        print j
        
    conn.Destroy()

    
        
Iterate over Features
---------------------
 
.. code-block:: python

    from osgeo import ogr
    import os

    shapefile = "states.shp"
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shapefile, 0)
    layer = dataSource.GetLayer()

    for i in range(0,layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        print feature.GetField("STATE_NAME")

Get Geometry from each Feature in a Layer
-----------------------------------------

.. code-block:: python

    from osgeo import ogr
    import os

    shapefile = "states.shp"
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shapefile, 0)
    layer = dataSource.GetLayer()

    for i in range(0,layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        geom = feature.GetGeometryRef()
        print geom.Centroid().ExportToWkt()

Filter by attribute
-------------------
 
.. code-block:: python  
     
    from osgeo import ogr
    import os

    shapefile = "states.shp"
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shapefile, 0)
    layer = dataSource.GetLayer()

    layer.SetAttributeFilter("SUB_REGION = 'Pacific'")

    feature = layer.GetNextFeature()
    while feature:
        print feature.GetField("STATE_NAME")
        feature = layer.GetNextFeature() 

Spatial Filter
--------------

.. code-block:: python  

    from osgeo import ogr
    import os

    shapefile = "states.shp"
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shapefile, 0)
    layer = dataSource.GetLayer()

    wkt = "POLYGON ((-103.81402655265633 50.253951270672125,-102.94583419409656 51.535568561879401,-100.34125711841725 51.328856095555651,-100.34125711841725 51.328856095555651,-93.437060743203844 50.460663736995883,-93.767800689321859 46.450441890315041,-94.635993047881612 41.613370178339181,-100.75468205106476 41.365315218750681,-106.12920617548238 42.564247523428456,-105.96383620242338 47.277291755610058,-103.81402655265633 50.253951270672125))"
    layer.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt))

    feature = layer.GetNextFeature()
    while feature:
        print feature.GetField("STATE_NAME")
        feature = layer.GetNextFeature()

Get Shapefile Fields - Get the user defined fields
---------------------------------------------------
 
    This code example returns the field names of the user defined (created) fields.  

.. code-block:: python
    
    from osgeo import ogr
    
    daShapefile = r"C:\Temp\Voting_Centers_and_Ballot_Sites.shp"

    dataSource = ogr.Open(daShapefile)
    daLayer = dataSource.GetLayer(0)
    layerDefinition = daLayer.GetLayerDefn()


    for i in range(layerDefinition.GetFieldCount()):
        print layerDefinition.GetFieldDefn(i).GetName() 

        
        
Get Shapefile Fields and Types - Get the user defined fields
------------------------------------------------------------

     This code example returns the field names of the user defined (created) fields and the data types they are.
     
.. code-block:: python    

    from osgeo import ogr

    daShapefile = r"C:\Temp\iDay\CWI_Wetlands.shp"

    dataSource = ogr.Open(daShapefile)
    daLayer = dataSource.GetLayer(0)
    layerDefinition = daLayer.GetLayerDefn()


    print "Name  -  Type  Width  Precision"
    for i in range(layerDefinition.GetFieldCount()):
        fieldName =  layerDefinition.GetFieldDefn(i).GetName()
        fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
        fieldType = ogr.GetFieldTypeName(fieldTypeCode)
        fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
        GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()

        print fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision)  
 

Create a new Layer from the extent of an existing Layer
-------------------------------------------------------   

.. image:: images/layer_extent.png

.. code-block:: python

    from osgeo import ogr
    import os

    # Get a Layer's Extent
    inShapefile = "states.shp"
    inDriver = ogr.GetDriverByName("ESRI Shapefile")
    inDataSource = inDriver.Open(inShapefile, 0)
    inLayer = inDataSource.GetLayer()
    extent = inLayer.GetExtent()

    # Create a Polygon from the extent tuple
    ring = ogr.Geometry(ogr.wkbLinearRing)
    ring.AddPoint(extent[0],extent[2]) 
    ring.AddPoint(extent[1], extent[2])
    ring.AddPoint(extent[1], extent[3])
    ring.AddPoint(extent[0], extent[3]) 
    ring.AddPoint(extent[0],extent[2]) 
    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(ring)

    # Save extent to a new Shapefile
    outShapefile = "states_extent.shp"
    outDriver = ogr.GetDriverByName("ESRI Shapefile")

    # Remove output shapefile if it already exists
    if os.path.exists(outShapefile):
        outDriver.DeleteDataSource(outShapefile)

    # Create the output shapefile
    outDataSource = outDriver.CreateDataSource(outShapefile)
    outLayer = outDataSource.CreateLayer("states_extent", geom_type=ogr.wkbPolygon)

    # Add an ID field
    idField = ogr.FieldDefn("id", ogr.OFTInteger)
    outLayer.CreateField(idField)

    # Create the feature and set values
    featureDefn = outLayer.GetLayerDefn()
    feature = ogr.Feature(featureDefn)
    feature.SetGeometry(poly)
    feature.SetField("id", 1)
    outLayer.CreateFeature(feature)

    # Close DataSource
    inDataSource.Destroy()
    outDataSource.Destroy()
    


Save centroids of input Layer to an output Layer
------------------------------------------------

Inspired by: http://www.kralidis.ca/blog/2010/04/28/batch-centroid-calculations-with-python-and-ogr/

.. image:: images/layer_centroids.png

.. code-block:: python

    from osgeo import ogr
    import os

    # Get the input Layer
    inShapefile = "states.shp"
    inDriver = ogr.GetDriverByName("ESRI Shapefile")
    inDataSource = inDriver.Open(inShapefile, 0)
    inLayer = inDataSource.GetLayer()

    # Create the output Layer
    outShapefile = "states_centroids.shp"
    outDriver = ogr.GetDriverByName("ESRI Shapefile")

    # Remove output shapefile if it already exists
    if os.path.exists(outShapefile):
        outDriver.DeleteDataSource(outShapefile)

    # Create the output shapefile
    outDataSource = outDriver.CreateDataSource(outShapefile)
    outLayer = outDataSource.CreateLayer("states_centroids", geom_type=ogr.wkbPoint)

    # Add input Layer Fields to the output Layer
    inLayerDefn = inLayer.GetLayerDefn()
    for i in range(0, inLayerDefn.GetFieldCount()):
        fieldDefn = inLayerDefn.GetFieldDefn(i)
        outLayer.CreateField(fieldDefn)

    # Get the output Layer's Feature Definition
    outLayerDefn = outLayer.GetLayerDefn()

    # Add features to the ouput Layer
    for i in range(0, inLayer.GetFeatureCount()):
        # Get the input Feature
        inFeature = inLayer.GetFeature(i)
        # Create output Feature
        outFeature = ogr.Feature(outLayerDefn)
        # Add field values from input Layer
        for i in range(0, outLayerDefn.GetFieldCount()):
            outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
        # Set geometry as centroid    
        geom = inFeature.GetGeometryRef()
        centroid = geom.Centroid()
        outFeature.SetGeometry(centroid)
        # Add new feature to output Layer
        outLayer.CreateFeature(outFeature)

    # Close DataSources
    inDataSource.Destroy()
    outDataSource.Destroy()
    
Create a New Shapefile and Add Data
-----------------------------------

This recipe parses a delimited text file of volcano location data and creates a shapefile.
The CSV file ``volcano_data.txt`` contains the following fields, separated by a tab character (\\t):

*  Name
*  Region
*  Latitude
*  Longitude
*  Elevation

`Taken from The Geospatial Desktop book.`

.. code-block:: python

  # Parse a delimited text file of volcano data and create a shapefile 

  import osgeo.ogr as ogr 
  import osgeo.osr as osr

  # use a dictionary reader so we can access by field name
  reader = csv.DictReader(open("volcano_data.txt","rb"), 
      delimiter='\t',     
      quoting=csv.QUOTE_NONE)

  # set up the shapefile driver
  driver = ogr.GetDriverByName("ESRI Shapefile") 

  # create the data source
  data_source = driver.CreateDataSource("volcanoes.shp") 

  # create the spatial reference, WGS84
  srs = osr.SpatialReference() 
  srs.ImportFromEPSG(4326)

  # create the layer
  layer = data_source.CreateLayer("volcanoes", srs, ogr.wkbPoint) 

  # Add the fields we're interested in
  field_name = ogr.FieldDefn("Name", ogr.OFTString) 
  field_name.SetWidth(24) 
  layer.CreateField(field_name) 
  field_region = ogr.FieldDefn("Region", ogr.OFTString)
  field_region.SetWidth(24)
  layer.CreateField(field_region)
  layer.CreateField(ogr.FieldDefn("Latitude", ogr.OFTReal)) 
  layer.CreateField(ogr.FieldDefn("Longitude", ogr.OFTReal))
  layer.CreateField(ogr.FieldDefn("Elevation", ogr.OFTInteger)) 

  # Process the text file and add the attributes and features to the shapefile
  for row in reader: 
    # create the feature
    feature = ogr.Feature(layer.GetLayerDefn()) 
    # Set the attributes using the values from the delimited text file
    feature.SetField("Name", row['Name']) 
    feature.SetField("Region", row['Region'])
    feature.SetField("Latitude", row['Latitude'])
    feature.SetField("Longitude", row['Longitude'])
    feature.SetField("Elevation", row['Elev']) 

    # create the WKT for the feature using Python string formatting
    wkt = "POINT(%f %f)" %  (float(row['Longitude']) , float(row['Latitude'])) 

    # Create the point from the Well Known Txt
    point = ogr.CreateGeometryFromWkt(wkt)  

    # Set the feature geometry using the point
    feature.SetGeometry(point) 
    # Create the feature in the layer (shapefile)
    layer.CreateFeature(feature) 
    # Destroy the feature to free resources
    feature.Destroy() 

  # Destroy the data source to free resources
  data_source.Destroy() 
   

