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

Create a MultiLineString
------------------------

.. code-block:: python

    from osgeo import ogr

    multiline = ogr.Geometry(ogr.wkbMultiLineString)

    line1 = ogr.Geometry(ogr.wkbLineString)
    line1.AddPoint(1214242.4174581182, 617041.9717021306)
    line1.AddPoint(1234593.142744733, 629529.9167643716)
    multiline.AddGeometry(line1)

    line1 = ogr.Geometry(ogr.wkbLineString)
    line1.AddPoint(1184641.3624957693, 626754.8178616514)
    line1.AddPoint(1219792.6152635587, 606866.6090588232)
    multiline.AddGeometry(line1)

    print multiline.ExportToWkt()

Create a MultiPolygon
---------------------

.. code-block:: python

    from osgeo import ogr

    multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)

    # Create ring #1
    ring1 = ogr.Geometry(ogr.wkbLinearRing)
    ring1.AddPoint(1204067.0548148106, 634617.5980860253)
    ring1.AddPoint(1204067.0548148106, 620742.1035724243)
    ring1.AddPoint(1215167.4504256917, 620742.1035724243)
    ring1.AddPoint(1215167.4504256917, 634617.5980860253)
    ring1.AddPoint(1204067.0548148106, 634617.5980860253) 

    # Create polygon #1
    poly1 = ogr.Geometry(ogr.wkbPolygon)
    poly1.AddGeometry(ring1)
    multipolygon.AddGeometry(poly1)

    # Create ring #2
    ring2 = ogr.Geometry(ogr.wkbLinearRing)
    ring2.AddPoint(1179553.6811741155, 647105.5431482664)
    ring2.AddPoint(1179553.6811741155, 626292.3013778647) 
    ring2.AddPoint(1194354.20865529, 626292.3013778647)
    ring2.AddPoint(1194354.20865529, 647105.5431482664) 
    ring2.AddPoint(1179553.6811741155, 647105.5431482664)

    # Create polygon #2
    poly2 = ogr.Geometry(ogr.wkbPolygon)
    poly2.AddGeometry(ring2)
    multipolygon.AddGeometry(poly2)

    print multipolygon.ExportToWkt()

Create Geometry from WKT
------------------------

.. code-block:: python

    from osgeo import ogr

    wkt = "POINT (1120351.5712494177 741921.4223245403)"
    point = ogr.CreateGeometryFromWkt(wkt)
    print "%d,%d" % (point.GetX(), point.GetY())

Create Geometry from GeoJSON
----------------------------

.. code-block:: python

    from osgeo import ogr

    geojson = """{"type":"Point","coordinates":[108420.33,753808.59]}"""
    point = ogr.CreateGeometryFromJson(geojson)
    print "%d,%d" % (point.GetX(), point.GetY())

Create Geometry from GML
------------------------

.. code-block:: python

    from osgeo import ogr

    gml = """<gml:Point xmlns:gml="http://www.opengis.net/gml"><gml:coordinates>108420.33,753808.59</gml:coordinates></gml:Point>"""
    point = ogr.CreateGeometryFromGML(gml)
    print "%d,%d" % (point.GetX(), point.GetY())

Create Geometry from WKB
------------------------

.. code-block:: python

    from osgeo import ogr
    from base64 import b64decode

    wkb = b64decode("AIAAAAFBMkfmVwo9cUEjylouFHrhAAAAAAAAAAA=")
    point = ogr.CreateGeometryFromWkb(wkb)
    print "%d,%d" % (point.GetX(), point.GetY())

Count Points in a Geometry
--------------------------

.. code-block:: python

    from osgeo import ogr

    wkt = "LINESTRING (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
    geom = ogr.CreateGeometryFromWkt(wkt)
    print "Geometry has %i points" % (geom.GetPointCount())

County Geometries in a Geometry
-------------------------------

.. code-block:: python

    from osgeo import ogr

    wkt = "MULTIPOINT (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
    geom = ogr.CreateGeometryFromWkt(wkt)
    print "Geometry has %i geometries" % (geom.GetGeometryCount())

Iterate over Geometries in a Geometry
-------------------------------------

.. code-block:: python

    from osgeo import ogr

    wkt = "MULTIPOINT (1181866.263593049 615654.4222507705, 1205917.1207499576 623979.7189589312, 1227192.8790041457 643405.4112779726, 1224880.2965852122 665143.6860159477)"
    geom = ogr.CreateGeometryFromWkt(wkt)
    for i in range(0, geom.GetGeometryCount()):
        g = geom.GetGeometryRef(i)
        print "%i). %s" %(i, g.ExportToWkt())