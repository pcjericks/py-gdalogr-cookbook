### This function creates a buffer for any file passed it, point, line, or
### polygon. It takes two arguments, InputFileName, for the file with which
### to create a buffer, and buf, specifying the size of the buffer.

try:
    from osgeo import ogr
except ImportError:
    import ogr

import os, sys

def bufferCalculation(InputFileName,buf):

    OutputFileName = "buffer_" + InputFileName
    
    driver = ogr.GetDriverByName('GeoJSON')
    inputDS = driver.Open(InputFileName, 0)
    if inputDS is None:
        print 'Could not open input file',InputFileName
        sys.exit(1)

    inputLayer = inputDS.GetLayer()

    if os.path.exists(OutputFileName):
        os.remove(OutputFileName)
    try:
        outputDS = driver.CreateDataSource(OutputFileName)
    except:
        print 'Could not create output file',OutputFileName
        sys.exit(1)

    newLayer = outputDS.CreateLayer('TestBuffer', geom_type=ogr.wkbPolygon,srs=inputLayer.GetSpatialRef())
    if newLayer is None:
        print "couldn't create layer for buffer in output DS"
        sys.exit(1)

    newLayerDef = newLayer.GetLayerDefn()
    featureID = 0
    oldFeature = inputLayer.GetNextFeature()
    while oldFeature:

        geometry = oldFeature.GetGeometryRef()
        bufferz = geometry.Buffer(buf,5)
        try:
            newFeature = ogr.Feature(newLayerDef)
            newFeature.SetGeometry(bufferz)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
        except:
            print "error adding buff"

        newFeature.Destroy()
        oldFeature.Destroy()
        oldFeature = inputLayer.GetNextFeature()
        featureID += 1


    print 'There are ', featureID, ' input features'

    inputDS.Destroy()
    outputDS.Destroy()