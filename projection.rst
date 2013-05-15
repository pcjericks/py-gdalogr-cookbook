Projection
==========

Create Projection From EPSG
---------------------------

.. code-block:: python

	from osgeo import osr
	spatialRef = osr.SpatialReference()
	spatialRef.ImportFromEPSG(2927)
