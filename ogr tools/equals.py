### This function checks two features in a file to see their geometries are
### equal. It takes 4 arguments, f1 for the first file, fid1 for the index of the
### first file's geometry, f2 for the second file, fid2 for the index of the
### second file's geometry. Returns whether the geometries are equal.

try:
    from osgeo import ogr
except ImportError:
    import ogr

import os, sys

def equals(f1,fid1,f2,fid2):
    driver = ogr.GetDriverByName("GeoJSON")
    
    file1 = driver.Open(f1,0)
    layer1 = file1.GetLayer()
    feat1 = layer1.GetFeature(fid1)
    geom1 = feat1.GetGeometryRef()

    file2 = driver.Open(f2,0)
    layer2 = file2.GetLayer()
    feat2 = layer2.GetFeature(fid2)
    geom2 = feat2.GetGeometryRef()

    if geom1.Equals(geom2) == 1:
        print "GEOMETRIES ARE EQUAL"
    else:
        print "GEOMETRIES ARE EQUAL"