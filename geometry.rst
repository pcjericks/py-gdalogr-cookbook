Geometry
========

Create a Point
--------------

.. code-block:: python

    from osgeo import ogr
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(1198054.34, 648493.09)
    print point.ExportToWkt()



