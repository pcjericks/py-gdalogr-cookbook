Python OGR/GDAL Cookbook
------------------------
A cookbook of recipes for using the Python GDAL/OGR bindings.

Setup
-----
Create a project folder **py-gdalorg-cookbook** and then create **source** and **build\html** subfolders.

project
 |
 |-source 
 |
 |-build
    |
    |-html

In the **source** folder run::

    git clone https://github.com/pcjericks/py-gdalogr-cookbook.git .

In the **build\html** folder run::

     git clone -b gh-pages https://github.com/pcjericks/py-gdalogr-cookbook.git .

Now you have a functioning Sphinx project.  You can run **make html** from the **source** folder and the HTML will 
be created in the **build\html** folder.

Example command line code::

    mkdir py-gdalogr-cookbook
    cd py-gdalogr-cookbook
    mkdir source
    mkdir build
    cd source 
    git clone https://github.com/pcjericks/py-gdalogr-cookbook.git .
    cd ..
    cd build
    mkdir html
    git clone -b gh-pages https://github.com/pcjericks/py-gdalogr-cookbook.git .

License
-------
The Python OGR/GDAL Cookbook is open source and licensed under the MIT license.