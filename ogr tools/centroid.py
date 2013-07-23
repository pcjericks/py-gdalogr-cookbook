try:
    from osgeo import ogr
except ImportError:
    import ogr

import os, sys

def centroid(inputFile):

    outputFileName = "centroid_" + inputFile

    driver = ogr.GetDriverByName("GeoJSON")
    inputDS = ogr.Open(inputFile,0)

    if inputDS is None:
        print "Could not open input file", inputFile
        sys.exit(1)

    layer = inputDS.GetLayer()

    #create output file
    if os.path.exists(outputFileName):
        os.remove(outputFileName)
    try:
        outputDS = driver.CreateDataSource(outputFileName)
    except:
        print 'Could not create output file', outputDS
        sys.exit(1)

    newLayer = outputDS.CreateLayer('centroid',geom_type=ogr.wkbPoint,srs=layer.GetSpatialRef())

    if newLayer is None:
        print "Couldn't create layer for buffer in output DS"
        sys.exit(1)

    newLayerDef = newLayer.GetLayerDefn()
    featureID = 0
    oldFeature = layer.GetNextFeature()
    
    while oldFeature:
        geometry = oldFeature.GetGeometryRef()
        centroid = geometry.Centroid()
        try:
            newFeature = ogr.Feature(newLayerDef)
            newFeature.SetGeometry(centroid)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
        except:
            print "Error computing centroid for feature", featureID

        newFeature.Destroy()
        oldFeature.Destroy()
        oldFeature = layer.GetNextFeature()
        featureID += 1

    inputDS.Destroy()
    outputDS.Destroy()