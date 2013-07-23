### This program appends the data from one file to another. It takes two
### arguments, f1 and f2, which should be the files used for appending.

from osgeo import ogr
import sys, subprocess

#syntax for ogr2ogr w/ append: ogr2ogr -f "output format" -append outputDS inputDS

def append(f1,f2):
    
   noExt = f1[:-4]
    subprocess.call(["ogr2ogr","-f","GeoJSON","-append","-nln",noExt,f1,f2,"-update"])