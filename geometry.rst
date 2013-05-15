Geometry
========

Create a Point
--------------

.. code-block:: python

    from osgeo import ogr
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(1198054.34, 648493.09)
    print point.ExportToWkt()

Create a LineString
-------------------

.. code-block:: python

    from osgeo import ogr
    line = ogr.Geometry(ogr.wkbLineString)
    line.AddPoint(1116651.439379124, 637392.6969887456)
    line.AddPoint(1188804.0108498496, 652655.7409537067)
    line.AddPoint(1226730.3625203592, 634155.0816022386) 
    line.AddPoint(1281307.30760719, 636467.6640211721)
    print line.ExportToWkt()




