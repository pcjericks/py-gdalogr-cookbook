### This returns the bounding envelope for a specific geometry. See layerExtent.py
### to get the entire extent of a layer

try:
    from osgeo import ogr
except ImportError:
    import ogr

    import sys

def getEnvelope(inFile,g): #inFile = file, g = geometry
    driver = ogr.GetDriverByName("ESRI Shapefile")
    f = driver.Open(inFile,0)
    layer = f.GetLayer()

    featCount = layer.GetFeatureCount()

    if g > featCount:
        print "Feature ", g, "does not exist in", inFile
        sys.exit(1)

    try:
        feature = layer.GetFeature(g)
    
        geom = feature.GetGeometryRef()
        envelope = geom.GetEnvelope()
        return envelope

    except:
        print "Could not obtain envelope"
        sys.exit(1)