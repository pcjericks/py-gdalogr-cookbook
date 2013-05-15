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

Create a Polygon
----------------

.. code-block:: python
    
    from osgeo import ogr

    # Create ring
    ring = ogr.Geometry(ogr.wkbLinearRing)
    ring.AddPoint(1179091.1646903288, 712782.8838459781)
    ring.AddPoint(1161053.0218226474, 667456.2684348812)
    ring.AddPoint(1214704.933941905, 641092.8288590391)
    ring.AddPoint(1228580.428455506, 682719.3123998424) 
    ring.AddPoint(1218405.0658121984, 721108.1805541387) 
    ring.AddPoint(1179091.1646903288, 712782.8838459781)

    # Create polygon
    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(ring)

    print poly.ExportToWkt()

Create a Polygon with holes
----------------------------

.. code-block:: python

    from osgeo import ogr

    # Create outer ring
    outRing = ogr.Geometry(ogr.wkbLinearRing)
    outRing.AddPoint(1154115.274565847, 686419.4442701361)
    outRing.AddPoint(1154115.274565847, 653118.2574374934)
    outRing.AddPoint(1165678.1866605144, 653118.2574374934)
    outRing.AddPoint(1165678.1866605144, 686419.4442701361)
    outRing.AddPoint(1154115.274565847, 686419.4442701361)

    # Create inner ring
    innerRing = ogr.Geometry(ogr.wkbLinearRing)
    innerRing.AddPoint(1149490.1097279799, 691044.6091080031)
    innerRing.AddPoint(1149490.1097279799, 648030.5761158396)
    innerRing.AddPoint(1191579.1097525698, 648030.5761158396)
    innerRing.AddPoint(1191579.1097525698, 691044.6091080031)
    innerRing.AddPoint(1149490.1097279799, 691044.6091080031)

    # Create polygon
    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(outRing)
    poly.AddGeometry(innerRing)

    print poly.ExportToWkt()

Create a MultiPoint
-------------------

.. code-block:: python

    from osgeo import ogr

    multipoint = ogr.Geometry(ogr.wkbMultiPoint)

    point1 = ogr.Geometry(ogr.wkbPoint)
    point1.AddPoint(1251243.7361610543, 598078.7958668759)
    multipoint.AddGeometry(point1)

    point2 = ogr.Geometry(ogr.wkbPoint)
    point2.AddPoint(1240605.8570339603, 601778.9277371694)
    multipoint.AddGeometry(point2)

    point3 = ogr.Geometry(ogr.wkbPoint)
    point3.AddPoint(1250318.7031934808, 606404.0925750365)
    multipoint.AddGeometry(point3)

    print multipoint.ExportToWkt()

