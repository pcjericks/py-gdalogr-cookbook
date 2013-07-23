### This program returns a list of all unique values within a specified
### field. It takes two arguments, 'f' for the filename (including extension)
### and 'field' for the desired field. Both arguments passed to the function
### should be strings.

from osgeo import ogr
import os, sys

def uniqueValues(f,field):
    driver = ogr.GetDriverByName("GeoJSON")
    inFile = driver.Open(f,0)
    layer = inFile.GetLayer()
    noExt = f[:-4]

    uniqueValues = "select distinct " + field + " from " + noExt
    
    result = inFile.ExecuteSQL(uniqueValues)
    resultFeat = result.GetNextFeature()

    uniqueFieldList = []
    
    while resultFeat:
        field = resultFeat.GetField(0)
        
        uniqueFieldList.append(field)

        resultFeat = result.GetNextFeature()

    print uniqueFieldList