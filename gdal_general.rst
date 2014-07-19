GDAL/OGR General
================

Is GDAL/OGR Installed
-----------------------
Imports python GDAL and exits the program if the modules are not found.

.. code-block:: python

    import sys
    try:
        from osgeo import ogr, osr, gdal
    except:
        sys.exit('ERROR: cannot find GDAL/OGR modules')


Check Version of GDAL/OGR installed
-------------------------------------
This code checks the version of the GDAL/OGR on the imported module

.. code-block:: python

    import sys
    from osgeo import gdal

    version_num = int(gdal.VersionInfo('VERSION_NUM'))
    if version_num < 1100000:
        sys.exit('ERROR: Python bindings of GDAL 1.10 or later required')


Enable python exceptions
--------------------------
By default the GDAL/OGR Python bindings do not raise exceptions when errors occur. Instead they return an error value
such as None and write an error message to sys.stdout. You can enable exceptions by calling the UseExceptions() function:
    
.. code-block:: python

    from osgeo import gdal
    
    # Enable GDAL/OGR exceptions
    gdal.UseExceptions()
    
    # open dataset that does not exist
    ds = gdal.Open('test.tif')
    # results in python RuntimeError exception that 
    # `test.tif' does not exist in the file system

You can disable using GDAL/OGR exceptions at any point during runtime using:

.. code-block:: python

    from osgeo import gdal
    gdal.DontUseExceptions()


