API Tricks and Trapdoors
==========================

The official `GDAL/OGR Trac wiki <http://trac.osgeo.org/gdal>`_  has a must-read section on 
`Python gotchas <http://trac.osgeo.org/gdal/wiki/PythonGotchas>`_. The section lists some
common Python API tricks that will bite a developer more than once. Many of 
the gotchas can manifest themselves in very, very subtle ways. The purpose
of the list below is twofold. First, it will catalog gotchas that are too subtle 
for the official wiki. Secondly, it will highlight API areas that are
confusing or require unintuitive Python.

Filtered Features Are Only Respected Using `GetNextFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetNextFeature>`_
---------------------------------------------------------------------------------------------------------------------------------------

There are two ways to access a layer's features. 
You can use `GetFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetFeature>`_ and pass in a feature ID or use
`GetNextFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetNextFeature>`_ to pass back the next feature. If you are
using an attribute filter ( `SetAttributeFilter() <http://gdal.org/python/osgeo.ogr.Layer-class.html#SetAttributeFilter>`_ ) 
or spatial filter ( `SetSpatialFilter() <http://gdal.org/python/osgeo.ogr.Layer-class.html#SetSpatialFilter>`_ or `SetSpatialFilterRect() <http://gdal.org/python/osgeo.ogr.Layer-class.html#SetSpatialFilterRect>`_ ) then you have to use `GetNextFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetNextFeature>`_. 

If you read the documentation for any of the filter setters you will see the caveat about OGR_L_GetNextFeature(). This means that if you use `GetFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetFeature>`_, instead of `GetNextFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetNextFeature>`_, then you can still access and work with features from the layer that are not covered by the filter. `GetFeatureCount() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetFeatureCounty>`_ will respect the filter and show the correct number of features filtered. However, working with `GetFeatureCount() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetFeatureCounty>`_ in a loop can lead to some interesting results. Using the Layer object as a `feature iterator <https://github.com/pcjericks/py-gdalogr-cookbook/pull/54>`_ or using `GetNextFeature() <http://gdal.org/python/osgeo.ogr.Layer-class.html#GetNextFeature>`_ explicitly should be the default method for accessing features:

.. code-block:: python

    from osgeo import ogr
    inDataSource = ogr.Open( "parcels.shp" )
    lyr = inDataSource.GetLayer()
    lyr.SetAttributeFilter("PIN = '0000200001'")      # this is a unique attribute filter targeting only one record
    for i in range( 0, lyr.GetFeatureCount() ):       
        feat = lyr.GetFeature( i )
        print feat                                    # this will print one feat, but it's the first feat in the Layer and NOT our target filtered feat  

Iterating over features
.......................

You can treat a layer as an iterator, which calls GetNextFeature().  Iterating over a layer a second time will not work, unless you call `ResetReading() <http://gdal.org/python/osgeo.ogr.Layer-class.html#ResetReading>`_ first, like:

.. code-block:: python

    for feature in layer:
        print feature.GetField("STATE_NAME")
    layer.ResetReading()
    for feature in layer:
        print feature.GetField("STATE_NAME")

Features and Geometries Have a Relationship You Don't Want to Break
-----------------------------------------------------------------------

The official gotchas have a good section on why `Python crashes when deleting features <http://trac.osgeo.org/gdal/wiki/PythonGotchas#Pythoncrashesifyouuseanobjectafterdeletinganobjectithasarelationshipwith>`_ that still have geometry references in use. They even talk about how this translates to the underlying C++ references. More subtle cases happen when you loose reference to the feature without deleting it as the example below shows.

.. code-block:: python

    from osgeo import ogr
    dSource = ogr.Open( "parcel_address.shp" )
    if dSource is None:
        print "[ ERROR ]: datasource cannot be opened"
    layer = dSource.GetLayer()
    geom_collection = []

    #
    #  collect just the geometries
    #  notice that we are losing reference
    #  each geometry's parent feat though
    #
    for feat in layer:
        geom = feat.GetGeometryRef()
        geom_collection.append( geom )

    #
    #  try to print the 
    #  geometries collected
    #
    for g in geom_collection: 
        print g.ExportToWkt()

        <..PYTHON CRASHES..>








