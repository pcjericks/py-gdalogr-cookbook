try:
    from osgeo import ogr
except ImportError:
    import ogr

import sys, os

def difference(f1,f2):
    outputFileName = 'difference_' + f1
    
    driver = ogr.GetDriverByName("ESRI Shapefile")

    f1 = driver.Open(f1,0)
    layer1 = f1.GetLayer()
    feature1 = layer1.GetNextFeature()

    if f1 is None:
        print "Could not open file ", f1
        sys.exit(1)

    f2 = driver.Open(f2,0)
    layer2 = f2.GetLayer()
   # feature2 = layer2.GetNextFeature()

    if f2 is None:
        print "Could not open file ", f2

    ### Create output file ###
    if os.path.exists(outputFileName):
        os.remove(outputFileName)
    try:
        output = driver.CreateDataSource(outputFileName)
    except:
        print 'Could not create output datasource ', outputFileName
        sys.exit(1)

    newLayer = output.CreateLayer('SymmetricDifference',geom_type=ogr.wkbPolygon,srs=layer1.GetSpatialRef())

    if newLayer is None:
        print "Could not create output layer"
        sys.exit(1)

    newLayerDef = newLayer.GetLayerDefn()
    ##############################

    featureID = 0

    while feature1:

        layer2.ResetReading()
        geom1 = feature1.GetGeometryRef()
        feature2 = layer2.GetNextFeature()

        while feature2:

            geom2 = feature2.GetGeometryRef()
            
            if geom1.Overlaps(geom2) == 1:
                newgeom = geom1.Difference(geom2)
                newFeature = ogr.Feature(newLayerDef)
                newFeature.SetGeometry(newgeom)
                newFeature.SetFID(featureID)
                newLayer.CreateFeature(newFeature)
                featureID += 1
                newFeature.Destroy()
            
            else:
                newFeature1 = ogr.Feature(newLayerDef)
                newFeature1.SetGeometry(geom1)
                newFeature1.SetFID(featureID)
                newLayer.CreateFeature(newFeature1)

                featureID += 1
                newFeature2 = ogr.Feature(newLayerDef)
                newFeature2.SetGeometry(geom2)
                newFeature2.SetFID(featureID)
                newLayer.CreateFeature(newfeature2)
                featureID += 1
            
                newFeature1.Destroy()
                newFeature2.Destroy()
            
            feature2.Destroy()
            feature2 = layer2.GetNextFeature()
        
        feature1.Destroy()
        feature1 = layer1.GetNextFeature()
        
    f1.Destroy()
    f2.Destroy()