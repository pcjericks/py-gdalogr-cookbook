### This returns the extent of the entire layer. See getEnvelope.py
### to get the bounding envelope for specific geometries

try:
    from osgeo import ogr
except ImportError:
    import ogr

def layerExtent(f):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    f = driver.Open(f,0)
    layer = f.GetLayer()
    extent = layer.GetExtent()
    return extent