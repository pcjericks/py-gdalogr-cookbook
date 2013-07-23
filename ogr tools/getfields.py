### This program returns all fields within a specific file. It takes one
### argument, f, for the name of the file with which the fields are desired
### to be known.

from osgeo import ogr
import sys

def getFields(f):

    driver = ogr.GetDriverByName("GeoJSON")
    inFile = driver.Open(f,0)

    if inFile is None:
        print 'Could not open file', f, 'to read fields'
        sys.exit(1)

    layer = inFile.GetLayer()
    feat = layer.GetNextFeature()
    featDefn = feat.GetDefnRef()
    
    fieldCount = feat.GetFieldCount()

    try:
        i = 0
        while i < fieldCount:
            fieldDefn = featDefn.GetFieldDefn(i)
            fieldName = fieldDefn.GetNameRef()
            print fieldName
            i += 1

    except:
        print "Unable to read fields from", f