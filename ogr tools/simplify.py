try:
    from osgeo import ogr
except ImportError:
    import ogr

import sys, os

def simplify(infile,tolerance):
    
    outFileName = 'simplify_' + infile
    
    driver = ogr.GetDriverByName("GeoJSON")
    infile = driver.Open(infile,0)

    if infile is None:
        print 'Could not open file ', infile
        sys.exit(1)

    oldLayer = infile.GetLayer()
    oldFeature = oldLayer.GetNextFeature()
    geom = oldFeature.GetGeometryRef()
    geomType = geom.GetGeometryType()

    ########Create output file############
    if os.path.exists(outFileName):
        os.remove(outFileName)

    try:
        output = driver.CreateDataSource(outFileName)
    except:
        print 'Could not create output file', outFileName
        sys.exit(1)

    newLayer = output.CreateLayer('Tolerance',geom_type=geomType,srs=oldLayer.GetSpatialRef())
    if newLayer is None:
        print 'Could not create layer for simplify in output file'
        sys.exit(1)

    newLayerDef = newLayer.GetLayerDefn()
    #######################################
    
    featureID = 0

    ####### Simplify geometry and add to output file #######
    while oldFeature:

        geometry = oldFeature.GetGeometryRef()
        simplifiedGeom = geometry.Simplify(tolerance)

        try:
            newFeature = ogr.Feature(newLayerDef)
            newFeature.SetGeometry(simplifiedGeom)
            newFeature.SetFID(featureID)
            newLayer.CreateFeature(newFeature)
        except:
            print "Error performing simplify"

        newFeature.Destroy()
        oldFeature.Destroy()
        oldFeature = oldLayer.GetNextFeature()
        featureID += 1
    ##########################################################

    infile.Destroy()
    output.Destroy()