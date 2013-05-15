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