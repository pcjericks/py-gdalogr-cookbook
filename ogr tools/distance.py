### This function returns the distance between two geometries.
### It takes 4 arguments, f1 for the first file, fid1 for the index of the
### first file's geometry, f2 for the second file, fid2 for the index of the
### second file's geometry.

try:
    from osgeo import ogr
except ImportError:
    import ogr

import os, sys

def distance(f1,fid1,f2,fid2):
    driver = ogr.GetDriverByName("GeoJSON")
    
    file1 = driver.Open(f1,0)
    layer1 = file1.GetLayer()
    feat1 = layer1.GetFeature(fid1)
    geom1 = feat1.GetGeometryRef()

    file2 = driver.Open(f2,0)
    layer2 = file2.GetLayer()
    feat2 = layer2.GetFeature(fid2)
    geom2 = feat2.GetGeometryRef()

    return geom1.Distance(geom2)
    